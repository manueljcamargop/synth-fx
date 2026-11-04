"""Navegación completa, MP4 local y humo offline en Chrome y WebKit.
Requiere Playwright. Registra pruebas de motores en macOS, no dispositivos físicos.
"""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'pruebas'/'resultados';report=[]
with sync_playwright() as p:
 for name in ['chrome','webkit']:
  b=p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless=True) if name=='chrome' else p.webkit.launch(headless=True)
  ctx=b.new_context(viewport={'width':390,'height':844});ctx.set_offline(name=='chrome');page=ctx.new_page()
  for m,f in enumerate(sorted(ROOT.glob('Mision_*.html')),1):
   errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   page.goto(f.resolve().as_uri());attr='data-go' if m<3 else 'data-step'
   # Pulsar cada botón de navegación visible, incluyendo flechas y entradas a la misión.
   actions=[]
   for stage in range(5):
    page.locator(f'[{attr}="{stage}"]').first.click()
    if m<3:
     locs=page.locator('[data-go]');descs=locs.evaluate_all('bs=>bs.filter(b=>b.getClientRects().length).map(b=>({go:b.dataset.go,text:b.textContent.trim()}))')
     for d in descs:
      page.locator(f'[{attr}="{stage}"]').first.click()
      page.locator('[data-go="'+d['go']+'"]').filter(has_text=d['text']).last.click()
      actions.append(d)
    else:
     for sid in (['back','forward'] if m==3 else ['prevStep','nextStep']):
      page.locator(f'[{attr}="{stage}"]').first.click();button=page.locator('#'+sid)
      if button.is_enabled():button.click();actions.append({'id':sid,'stage':stage})
   page.locator(f'[{attr}="0"]').first.click()
   start=page.locator('[data-next]') if m==3 else page.locator('#begin') if m==4 else None
   if start is not None:start.click();actions.append({'start':True})
   # MP4 desde file://: avance, búsquedas exactas y reproducción hasta ended a velocidad 16x.
   page.locator('summary').click()
   media=page.evaluate('''async()=>{const v=document.querySelector('video');v.muted=true;await v.play();await new Promise(r=>setTimeout(r,400));v.pause();const progress=v.currentTime;const positions=[];for(const t of [1,3,v.duration-.4]){await new Promise(resolve=>{v.onseeked=resolve;v.currentTime=t;});positions.push(v.currentTime);}v.playbackRate=16;const ended=new Promise((resolve,reject)=>{v.onended=resolve;v.onerror=()=>reject(Error('MP4'));setTimeout(()=>reject(Error('ended timeout')),10000);});await v.play();await ended;return {duration:v.duration,width:v.videoWidth,height:v.videoHeight,progress,positions,ended:v.ended};}''')
   assert media['ended'] and media['progress']>0 and abs(media['positions'][1]-3)<.1,(name,m,media)
   page.evaluate('()=>{const v=document.querySelector("video");v.currentTime=3;}');page.wait_for_timeout(100)
   if name=='chrome':page.locator('video').screenshot(path=str(OUT/f'M{m}_video.png'))
   page.locator(f'[{attr}="2"]').first.click();page.wait_for_timeout(350)
   page.screenshot(path=str(OUT/f'M{m}_{name}_final_390.png'),full_page=True,animations='disabled')
   # Humo de audio con los archivos finales, sin instrumentación ni hooks de prueba.
   page.locator('#'+['playCustom','hearEngine','playFull','playLayer'][m-1]).click();page.wait_for_timeout(100)
   page.locator(f'[{attr}="4"]').first.click()
   assert not errors,errors
   report.append({'browser':name,'version':b.version,'mission':m,'navigationActions':len(actions),'video':media,'jsErrors':errors,'offlineEmulation':name=='chrome'})
   print(name,m,'ok',flush=True)
  b.close()
(OUT/'compatibilidad.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
