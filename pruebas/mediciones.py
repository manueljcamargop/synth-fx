"""Medición del grafo real de salida y análisis de espectro, WAV y sincronía.
Uso: python mediciones.py. Requiere Playwright y Google Chrome en macOS.
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import json,math,base64,wave,array
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'pruebas'/'resultados'
INIT='''window.meters=[];window.starts=[];const original=AudioNode.prototype.connect;AudioNode.prototype.connect=function(dest,...args){if(dest instanceof AudioDestinationNode&&this.context instanceof AudioContext){const a=this.context.createAnalyser();a.fftSize=2048;original.call(this,a);const mute=this.context.createGain();mute.gain.value=0;original.call(a,mute);original.call(mute,dest);window.meters.push(a);}return original.call(this,dest,...args);};const origStart=AudioBufferSourceNode.prototype.start;AudioBufferSourceNode.prototype.start=function(when,...args){window.starts.push({buffer:this.buffer,when,ctx:this.context});return origStart.call(this,when,...args);};'''
report={'output':[],'spectrum':[],'exportMatch':[],'sync':[],'failures':[]}
def check(ok,msg):
 if not ok:report['failures'].append(msg)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless=True)
 page=b.new_page();page.add_init_script(INIT)
 for m,f in enumerate(sorted(ROOT.glob('Mision_*.html')),1):
  page.goto(f.resolve().as_uri())
  nav='data-go' if m<3 else 'data-step'
  page.locator(f'[{nav}="2"]').first.click()
  # Medición del grafo de audio conectado a AudioDestinationNode, no solo datos PCM.
  play=['playCustom','hearEngine','playFull','playLayer'][m-1]
  page.locator('#'+play).click();page.wait_for_timeout(160)
  meters=page.evaluate('''()=>meters.map(a=>{const d=new Float32Array(a.fftSize);a.getFloatTimeDomainData(d);return {rms:Math.sqrt(d.reduce((s,x)=>s+x*x,0)/d.length),peak:d.reduce((s,x)=>Math.max(s,Math.abs(x)),0)};})''')
  check(any(a['rms']>1e-5 for a in meters),f'M{m}: salida sin energía')
  report['output'].append({'mission':m,'meters':meters})
  # Para M2, M3 y M4 el WAV de la misma escucha debe coincidir dentro del paso de cuantización.
  export=['downloadWav','exportEngine','exportPack','exportLayer'][m-1]
  with page.expect_download() as dl:page.locator('#'+export).click()
  path=OUT/f'comparacion_M{m}.wav';dl.value.save_as(path)
  with wave.open(str(path),'rb') as w:
   n=w.getnframes();channels=w.getnchannels();rate=w.getframerate();samples=list(array.array('h',w.readframes(n)))
  match=page.evaluate('''({samples,rate,channels})=>{const b=starts[starts.length-1].buffer;if(b.sampleRate!==rate||b.length*channels!==samples.length)return {comparable:false,rate:b.sampleRate,length:b.length};let maxError=0;for(let i=0;i<b.length;i++)for(let c=0;c<channels;c++){const x=b.getChannelData(c)[i];maxError=Math.max(maxError,Math.abs(x-samples[i*channels+c]/32768));}return {comparable:true,maxError};}''',{'samples':samples,'rate':rate,'channels':channels})
  check(match.get('comparable') and match['maxError']<2/32768,f'M{m}: WAV no coincide {match}')
  report['exportMatch'].append({'mission':m,**match})
  # Sincronía: reloj visual y tiempo programado se verifican antes y después de un inicio.
  page.locator(f'[{nav}="3"]').first.click()
  align=['alignSync','syncHelp','showGuide','autoSync'][m-1]
  page.locator('#'+align).click()
  if m==3:
   for key,v in {'encendido':1.3,'zumbido':2.1,'movimiento':5.6,'choque':8.4,'apagado':11.7}.items():page.locator('#time_'+key).evaluate('(e,v)=>{e.value=v;e.dispatchEvent(new Event("input",{bubbles:true}));}',str(v))
  run=['playSynced','play3','scenePlay','playScene'][m-1]
  page.evaluate('starts=[]');page.locator('#'+run).click();page.wait_for_timeout(90)
  timing=page.evaluate('''m=>{const s=starts[0];const id=m===1?'time3':m===2?'clock3':m===3?'clock':'clockSync';const elapsed=s.ctx.currentTime-(s.when-(m===1?6.2:m===2?2.4:0));return {elapsed,visual:document.getElementById(id).textContent,bufferDuration:s.buffer.duration,delay:s.when-s.ctx.currentTime};}''',m)
  check(-.1<timing['elapsed']<.4,f'M{m}: relojes desalineados {timing}')
  report['sync'].append({'mission':m,**timing})
  # Fotograma original MP4 para inspección visual y decodificación real.
  page.locator('summary').click();page.evaluate('''async()=>{const v=document.querySelector('video');await v.play();v.pause();v.currentTime=3;await new Promise(r=>v.onseeked=r);}''');page.locator('video').screenshot(path=str(OUT/f'M{m}_video.png'))
  print('Medición misión',m,flush=True)
 # DFT sobre periodos completos de las funciones realmente utilizadas por el motor compartido.
 spectrum=page.evaluate('''()=>{const N=4096;return ['sine','triangle','square','saw'].map(w=>{const a=Float64Array.from({length:N},(_,i)=>SynthFX.wave(w,2*Math.PI*i/N,44100/N,44100));const amps=[1,2,3,4,5].map(h=>{let re=0,im=0;for(let i=0;i<N;i++){re+=a[i]*Math.cos(2*Math.PI*h*i/N);im+=a[i]*Math.sin(2*Math.PI*h*i/N);}return 2*Math.hypot(re,im)/N;});return {wave:w,relative:amps.map(x=>x/amps[0])};});}''')
 for row in spectrum:
  h=row['relative'];w=row['wave'];check(h[1]<.001 if w!='saw' else abs(h[1]-.5)<.001,'Armónico 2 '+w)
  expected={'sine':0,'triangle':1/9,'square':1/3,'saw':1/3}[w];check(abs(h[2]-expected)<.001,'Armónico 3 '+w)
 report['spectrum']=spectrum
 b.close()
(OUT/'mediciones.json').write_text(json.dumps(report,indent=2,ensure_ascii=False));print(json.dumps(report,indent=2,ensure_ascii=False))
assert not report['failures'],report['failures']
