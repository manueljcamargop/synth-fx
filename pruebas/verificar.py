"""QA reproducible. Requiere Python 3 + Playwright; no es dependencia de la app.
Uso: python verificar.py [--webkit] (Chrome instalado por defecto).
Las exposiciones __qa se inyectan SOLO en memoria durante las pruebas.
"""
import json, re, sys, math, wave, array, threading, functools, http.server
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'pruebas'/'resultados'; OUT=OUT/'webkit' if '--webkit' in sys.argv else OUT; OUT.mkdir(parents=True,exist_ok=True)
HOOKS={1:'{go,synth,params,wavBytes,questions,stop:stopScene}',2:'{go,renderMotor,getParams,wavBytes,presets,comparisons,quiz,stop:stopScene}',3:'{go,makePCM,makeScenePCM,settings,defaults,exercises,quiz,current:()=>settings[selected],stop:stopScene}',4:'{go:setStep,synth,config,pristine,controls,sceneMix,current:()=>config[layer],exercises,quiz:quizQuestions,stop:()=>{stopAllAudio();stopVisual();}}'}
INIT='''window.__starts=[];window.__nodes=[];window.__errors=[];window.addEventListener('unhandledrejection',e=>window.__errors.push(String(e.reason)));const create=AudioContext.prototype.createBufferSource;AudioContext.prototype.createBufferSource=function(){const src=create.call(this);const start=src.start.bind(src),stop=src.stop.bind(src);src.start=(...args)=>{window.__starts.push({buffer:src.buffer,when:args[0],now:this.currentTime,node:src});window.__nodes.push(src);return start(...args)};src.stop=(...args)=>{src.__stopped=true;return stop(...args)};src.addEventListener('ended',()=>src.__ended=true);return src;};'''
MEASURE='''async()=>{const result=[];for(const s of window.__starts){const b=s.buffer;let peak=0,power=0;for(let c=0;c<b.numberOfChannels;c++){for(const x of b.getChannelData(c)){if(!Number.isFinite(x))throw Error('PCM no finito');peak=Math.max(peak,Math.abs(x));power+=x*x;}}const off=new OfflineAudioContext(b.numberOfChannels,b.length,b.sampleRate);const node=off.createBufferSource();node.buffer=b;node.connect(off.destination);node.start();const rendered=await off.startRendering();let energy=0;for(const x of rendered.getChannelData(0))energy+=x*x;result.push({duration:b.duration,rate:b.sampleRate,channels:b.numberOfChannels,peak,rms:Math.sqrt(power/b.length/b.numberOfChannels),offlineEnergy:energy,delay:s.when-s.now});}window.__starts=[];return result;}'''
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a): pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
report={'browser':'WebKit automatizado' if '--webkit' in sys.argv else 'Google Chrome headless en macOS','controls':[],'missions':[],'wav':[],'failures':[],'variants':[],'sliders':[]}
def check(ok,msg):
 if not ok: report['failures'].append(msg)
def stats(data):
 samples=array.array('h',data);peak=max(map(abs,samples),default=0)/32768; rms=math.sqrt(sum(x*x for x in samples)/max(1,len(samples)))/32768
 return peak,rms
with sync_playwright() as pw:
 browser=pw.webkit.launch(headless=True) if '--webkit' in sys.argv else pw.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless=True)
 report['version']=browser.version
 context=browser.new_context(accept_downloads=True,viewport={'width':1440,'height':1000})
 page=context.new_page();page.add_init_script(INIT)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.on('dialog',lambda d:(report['failures'].append('Diálogo: '+d.message),d.dismiss()))
 downloads=[]
 def save(d):
  dest=OUT/d.suggested_filename;d.save_as(dest);downloads.append(dest)
 page.on('download',save)
 for mission,f in enumerate(sorted(ROOT.glob('Mision_*.html')),1):
  if '--mission' in sys.argv and mission!=int(sys.argv[sys.argv.index('--mission')+1]):continue
  def route(r):
   html=f.read_text(); hook='window.__qa='+HOOKS[mission]+';'
   if mission<4: html=html.replace('})();',hook+'\n})();')
   else: html=html.replace('</script>',hook+'</script>')
   r.fulfill(status=200,content_type='text/html',body=html)
  page.route('**/'+f.name,route);page.goto(f'http://127.0.0.1:{server.server_port}/{f.name}');page.wait_for_timeout(100)
  check(page.evaluate('!!window.__qa'),f'{mission}: inicialización')
  check('Audio Pedagógico' in page.title(),f'{mission}: título')
  # Todos los botones originales y añadidos de cada etapa; navegación se prueba aparte.
  for step in range(5):
   page.evaluate('(n)=>__qa.go(n)',step)
   buttons=page.locator('button').evaluate_all('''bs=>bs.filter(b=>b.getClientRects().length&&!b.disabled&&!b.matches('[data-go],[data-step],[data-next],#back,#forward,#prevStep,#nextStep,#begin,#restart')).map(b=>({text:b.textContent.trim(),id:b.id,aria:b.getAttribute('aria-label'),attrs:[...b.attributes].filter(a=>a.name.startsWith('data-')).map(a=>[a.name,a.value])}))''')
   for desc in buttons:
    selector='#'+desc['id'] if desc['id'] else ''.join('['+k+'='+json.dumps(v)+']' for k,v in desc['attrs'])
    loc=page.locator(selector) if selector else page.get_by_role('button',name=desc['aria'] or desc['text'],exact=True)
    if not loc.count() or not loc.first.is_visible():continue
    page.evaluate('window.__starts=[]')
    try:
     loc.first.click(timeout=2500);page.wait_for_timeout(45)
     signals=page.evaluate(MEASURE)
     label=desc['text']
     sound=bool(re.search(r'Escuchar|\bProbar|Reproducir|▶ Núcleo|▶ Textura|▶ Chispa|▶ Mezcla',label,re.I)) and not re.search('sin sonido|muda|mudo',label,re.I)
     check(not sound or bool(signals),f'M{mission} {label}: no genera señal')
     for sig in signals:check(0<sig['peak']<1 and sig['offlineEnergy']>0,f'M{mission} {label}: silencio o clipping')
     report['controls'].append({'mission':mission,'step':step,'selector':selector or label,'label':label,'signals':signals,'ok':not sound or bool(signals)})
    except Exception as e:report['failures'].append(f'M{mission} {selector or desc["text"]}: {str(e)[:250]}')
  # Variantes de todos los eventos/capas y cada slider: diferencia numérica contra señal de referencia.
  extra=page.evaluate('''(m)=>{const q=__qa,rows=[];const measure=a=>a.reduce((v,x)=>v+x*x,0);const diff=(a,b)=>{let d=0;for(let i=0;i<Math.min(a.length,b.length);i++)d+=(a[i]-b[i])**2;return d/Math.min(a.length,b.length)};
  let variants=m===1?[q.params()]:m===2?Object.values(q.presets):m===3?Object.values(q.defaults):Object.entries(q.pristine).map(([id,c])=>({...c,id}));
  for(const p of variants){const render=x=>m===1?q.synth(x):m===2?q.renderMotor(x).L:m===3?q.makePCM(x,x.duration):q.synth(x.id,x,x.id==='ui'?x.decay:2);if(m===3){p.lfo=p.lfo||4;p.depth=p.depth||.3;}const base=render(p);rows.push({case:p.id||p.wave,energy:measure(base),duration:base.length/(m===2?32000:44100)});
  for(const [k,v]of Object.entries(p)){if(typeof v!=='number'||['duration'].includes(k))continue;const val=v===0?.2:v*.55;const b=render({...p,[k]:val});rows.push({parameter:k,case:p.id||p.wave,difference:diff(base,b)});}}
  return rows;}''',mission)
  for row in extra:
   if 'difference' in row:check(row['difference']>1e-14,f'M{mission}: parámetro sin efecto {row}')
   if 'energy' in row:check(row['energy']>0,f'M{mission}: caso silencioso {row}')
  # Escucha y exportación de cada preset, evento y capa, con parámetros restaurados.
  page.evaluate('()=>__qa.go(2)')
  variants=['default'] if mission==1 else ['exploradora','carguero','interceptora'] if mission==2 else ['encendido','zumbido','movimiento','choque','apagado'] if mission==3 else ['amb','ui','alarm']
  for variant in variants:
   if mission==2:page.locator(f'[data-preset="{variant}"]').click()
   if mission==3:
    page.locator(f'[data-cue="{variant}"]').click();page.locator('#restore').click()
   if mission==4:
    page.locator(f'[data-layer="{variant}"]').click();page.locator('#restoreLayer').click()
   ids=['playCustom'] if mission==1 else ['hearEngine'] if mission==2 else ['playTone','playNoise','playSpark','playFull','waveListen'] if mission==3 else ['playLayer','hearWave']
   for playid in ids:
    page.evaluate('__starts=[]');page.locator('#'+playid).click();page.wait_for_timeout(40);signals=page.evaluate(MEASURE)
    check(bool(signals) and all(0<x['peak']<1 and x['offlineEnergy']>0 for x in signals),f'M{mission} {variant} {playid}: señal inválida')
    report['variants'].append({'mission':mission,'case':variant,'button':playid,'signals':signals})
   exportid=['downloadWav','exportEngine','exportPack','exportLayer'][mission-1]
   page.locator('#'+exportid).click();page.wait_for_timeout(50)
   # Cada deslizador de síntesis actualiza el valor y genera señal finita en ambos extremos.
   for slider in page.locator('.active input[type=range]').all():
    sid=slider.get_attribute('id');original=slider.input_value()
    for bound in ['min','max']:
     value=slider.get_attribute(bound)
     slider.evaluate('(e,v)=>{e.value=v;e.dispatchEvent(new Event("input",{bubbles:true}));}',value)
     result=page.evaluate("""m=>{const q=__qa,p=m===1?q.params():m===2?q.getParams():q.current();const a=m===1?q.synth(p):m===2?q.renderMotor(p).L:m===3?q.makePCM(p,p.duration):q.synth(document.querySelector('[data-layer].selected').dataset.layer,p,1);let peak=0;for(const x of a){if(!Number.isFinite(x))throw Error('no finito');peak=Math.max(peak,Math.abs(x));}return {peak,params:p};}""",mission)
     check(result['peak']<1,f'M{mission} {variant} {sid} {bound}: clipping')
     report['sliders'].append({'mission':mission,'case':variant,'slider':sid,'bound':bound,'value':value,'peak':result['peak']})
    slider.evaluate('(e,v)=>{e.value=v;e.dispatchEvent(new Event("input",{bubbles:true}));}',original)
  # Las cuatro formas se seleccionan y producen audio en el motor de cada misión.
  for w in ['sine','triangle','square','saw']:
   if mission<3:page.select_option('#wave','tri' if mission==2 and w=='triangle' else w)
   else:page.locator(f'[data-wave="{w}"]').click()
   page.evaluate('__starts=[]');page.locator('#'+['playCustom','hearEngine','waveListen','hearWave'][mission-1]).click();page.wait_for_timeout(40)
   signals=page.evaluate(MEASURE);check(bool(signals) and signals[0]['offlineEnergy']>0,f'M{mission} onda {w}')
  # Regresar al estado inicial para las demás comprobaciones.
  page.evaluate('()=>__qa.stop()')
  # Opciones de respuesta: todas reciben explicación; respuestas correctas del modelo deben marcar good.
  page.evaluate('()=>__qa.go(4)')
  quizrows=page.evaluate('''m=>{const qs=m===1?__qa.questions:__qa.quiz;return qs.map((q,i)=>({i,right:q.right??q.a??q.correct}));}''',mission)
  for q in quizrows:
   selector= f'[data-quiz="{q["i"]}"][data-opt="{q["right"]}"]' if mission==1 else f'[data-q="{q["i"]}"][data-c="{q["right"]}"]' if mission==2 else f'[data-quiz="{q["i"]}"][data-choice="{q["right"]}"]' if mission==3 else f'[data-q="{q["i"]}"][data-a="{q["right"]}"]'
   page.locator(selector).click()
  good=page.locator('.active .feedback.good').count();check(good>=len(quizrows),f'M{mission}: respuestas correctas no validadas')
  # Navegación real de los cinco pasos.
  nav='[data-go]' if mission<3 else '[data-step]'
  for step in range(5):page.locator(f'{nav}[data-{ "go" if mission<3 else "step"}="{step}"]').first.click()
  # Stop frente a solicitudes simultáneas y frente a resume pendiente.
  page.evaluate('()=>__qa.go(2)')
  playid=['playCustom','hearEngine','playFull','playLayer'][mission-1]
  page.evaluate('''id=>{document.getElementById(id).click();document.getElementById(id).click();__qa.stop();}''',playid);page.wait_for_timeout(100)
  active=page.evaluate('window.__nodes.filter(n=>!n.__stopped&&!n.__ended).length');check(active==0,f'M{mission}: fuentes activas tras detener rápido: {active}')
  # Video: metadatos, avance real y seek próximo al evento principal.
  page.locator('summary').click()
  video=page.evaluate('''async()=>{const v=document.querySelector('video');await new Promise((res,rej)=>{if(v.readyState)res();else{v.onloadedmetadata=res;v.onerror=()=>rej(Error('MP4 inválido'));}});await v.play();await new Promise(r=>setTimeout(r,220));const advanced=v.currentTime;v.pause();await new Promise(r=>setTimeout(r,300));v.currentTime=Math.min(v.duration-0.1,8.7);await new Promise(r=>v.onseeked=r);return {duration:v.duration,width:v.videoWidth,height:v.videoHeight,advanced,seek:v.currentTime,error:v.error};}''')
  check(video['advanced']>0 and not video['error'],f'M{mission}: video no reproduce')
  # Capturas escritorio y teléfono emulado; desbordamiento en cada etapa.
  layouts=[]
  for width in [1440,390]:
   page.set_viewport_size({'width':width,'height':1000 if width==1440 else 844})
   for step in range(5):
    page.evaluate('(n)=>__qa.go(n)',step);page.wait_for_timeout(300)
    size=page.evaluate('({width:innerWidth,content:document.documentElement.scrollWidth})');layouts.append({'step':step,**size});check(size['content']<=width+1,f'M{mission}: desbordamiento {width}px etapa {step}')
    if step==2:page.screenshot(path=str(OUT/f'M{mission}_{width}.png'),full_page=True)
  report['missions'].append({'mission':mission,'parameters':extra,'quizCorrect':len(quizrows),'video':video,'layouts':layouts,'jsErrors':errors+page.evaluate('__errors')})
  check(not errors and not page.evaluate('__errors'),f'M{mission}: errores JS {errors}')
  errors.clear();page.unroute('**/'+f.name,route)
  print('Misión',mission,'completada; fallos acumulados:',len(report['failures']),flush=True)
 # Smoke sin interceptar, file:// y offline.
 context.set_offline('--webkit' not in sys.argv)
 report['localMode']='file:// con emulación offline' if '--webkit' not in sys.argv else 'file:// sin emulación offline: WebKit rechaza file:// con set_offline(True)'
 for f in sorted(ROOT.glob('*.html')):
  page.goto(f.resolve().as_uri());page.wait_for_timeout(100);check('Audio Pedagógico' in page.title(),'file offline '+f.name)
 context.set_offline(False)
 browser.close()
for f in set(downloads):
 if f.suffix!='.wav':continue
 with wave.open(str(f),'rb') as w:
  peak,rms=stats(w.readframes(w.getnframes()));row={'file':f.name,'channels':w.getnchannels(),'sampleRate':w.getframerate(),'bits':w.getsampwidth()*8,'frames':w.getnframes(),'duration':w.getnframes()/w.getframerate(),'peak':peak,'rms':rms};report['wav'].append(row)
  check(0<peak<1 and rms>0 and row['bits']==16,'WAV inválido '+f.name)
name='webkit' if '--webkit' in sys.argv else 'chrome'
if '--mission' in sys.argv:name+='_m'+sys.argv[sys.argv.index('--mission')+1]
(OUT/f'{name}.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
print(json.dumps({'controls':len(report['controls']),'wav':len(report['wav']),'failures':report['failures']},ensure_ascii=False,indent=2))
server.shutdown()
sys.exit(bool(report['failures']))
