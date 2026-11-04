"""Pruebas de interacción de perillas; Python + Playwright, Chrome y WebKit."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
R=Path(__file__).resolve().parents[1];O=R/'pruebas/resultados';report=[]
with sync_playwright() as p:
 for engine in ['chrome','webkit']:
  browser=p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless=True) if engine=='chrome' else p.webkit.launch(headless=True)
  ctx=browser.new_context(viewport={'width':1280,'height':1000},has_touch=True)
  page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.add_init_script('''window.__signals=[];const orig=AudioBufferSourceNode.prototype.start;AudioBufferSourceNode.prototype.start=function(...args){let peak=0;for(const x of this.buffer.getChannelData(0))peak=Math.max(peak,Math.abs(x));__signals.push({peak,duration:this.buffer.duration});return orig.apply(this,args);};''')
  for m,f in enumerate(sorted(R.glob('Mision_*.html')),1):
   page.goto(f.resolve().as_uri());attr='data-go' if m<3 else 'data-step';tested=[]
   for stage in range(5):
    page.locator(f'[{attr}="{stage}"]').first.click();page.wait_for_timeout(50)
    knobs=page.locator('.active .sfx-knob')
    if stage==2:assert knobs.count()>0
    for i in range(knobs.count()):
     knob=knobs.nth(i);sid=knob.get_attribute('data-control-id');native=page.locator('#'+sid);original=native.input_value()
     knob.focus();knob.press('Home');assert float(native.input_value())==float(native.get_attribute('min'))
     knob.press('End');assert float(native.input_value())==float(native.get_attribute('max'))
     knob.press('ArrowDown');assert float(native.input_value())<float(native.get_attribute('max'))
     assert float(knob.get_attribute('aria-valuenow'))==float(native.input_value())
     assert knob.get_attribute('aria-label')
     native.evaluate('(e,v)=>{e.value=v;e.dispatchEvent(new Event("input",{bubbles:true}));}',original)
     tested.append(sid)
   page.locator(f'[{attr}="2"]').first.click()
   first=page.locator('.active .sfx-knob').first;first.scroll_into_view_if_needed();first.focus();first.press('Home');page.wait_for_timeout(100);rect=first.bounding_box();x=rect['x']+rect['width']/2;y=rect['y']+rect['height']/2
   page.mouse.move(x,y);page.mouse.down();page.mouse.move(x,y-65,steps=8);page.mouse.up()
   assert float(first.get_attribute('aria-valuenow'))>float(first.get_attribute('aria-valuemin'))
   # Cambio de preset o regeneración de controles conserva la indicación de posición.
   variants=['classic','heavy','soft'] if m==1 else ['exploradora','carguero','interceptora'] if m==2 else ['encendido','zumbido','movimiento','choque','apagado'] if m==3 else ['amb','ui','alarm']
   for v in variants:
    selector=f'[data-preset="{v}"]' if m<3 else f'[data-cue="{v}"]' if m==3 else f'[data-layer="{v}"]'
    page.locator(selector).click();page.wait_for_timeout(40)
    assert page.locator('.active input[type=range]').count()==page.locator('.active .sfx-knob').count()
    for k in page.locator('.active .sfx-knob').all():
     value=page.locator('#'+k.get_attribute('data-control-id')).input_value()
     assert float(k.get_attribute('aria-valuenow'))==float(value)
   # La síntesis sigue recibiendo valores cambiados por la perilla.
   page.evaluate('__signals=[]');page.locator('#'+['playCustom','hearEngine','playFull','playLayer'][m-1]).click();page.wait_for_timeout(100)
   assert page.evaluate('__signals.some(s=>s.peak>0&&s.peak<1)')
   page.set_viewport_size({'width':390,'height':844});page.wait_for_timeout(100)
   knob=page.locator('.active .sfx-knob').first;knob.scroll_into_view_if_needed();knob.focus();knob.press('Home');rect=knob.bounding_box()
   # Toque real en el extremo superior derecho del aro.
   page.touchscreen.tap(rect['x']+rect['width']*.73,rect['y']+rect['height']*.27)
   assert float(knob.get_attribute('aria-valuenow'))>float(knob.get_attribute('aria-valuemin'))
   if engine=='chrome':
    knob.press('Home');rect=knob.bounding_box();x=rect['x']+rect['width']/2;y=rect['y']+rect['height']/2
    cdp=ctx.new_cdp_session(page)
    cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]})
    cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':[{'x':x,'y':y-50}]})
    cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]})
    assert float(knob.get_attribute('aria-valuenow'))>float(knob.get_attribute('aria-valuemin'))
   assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
   page.screenshot(path=str(O/f'perillas_{engine}_M{m}_390.png'),full_page=True,animations='disabled')
   page.set_viewport_size({'width':1280,'height':1000})
   assert not errors,errors
   report.append({'engine':engine,'mission':m,'keyboardControls':tested,'variants':variants,'mouseDrag':True,'touchTap':True,'touchDragEmulated':engine=='chrome','audio':page.evaluate('__signals'),'jsErrors':list(errors)})
   print(engine,m,'ok',len(tested),'perillas',flush=True)
  browser.close()
(O/'perillas.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
