/* Synth FX v0.5.0-rc2 · perillas accesibles sobre los controles originales. */
(()=>{
 'use strict';
 const knobs=new Map();
 function enhance(){
  for(const [input,ui] of knobs){if(!input.isConnected){knobs.delete(input);continue;}refresh(input,ui);}
  document.querySelectorAll('input[type="range"]:not(.sfx-knob-native)').forEach(input=>{
   const ui=document.createElement('div');ui.className='sfx-knob';ui.tabIndex=0;ui.setAttribute('role','slider');ui.setAttribute('aria-orientation','vertical');ui.dataset.controlId=input.id;
   const label=input.labels?.[0]?.cloneNode(true);label?.querySelectorAll('output').forEach(e=>e.remove());ui.setAttribute('aria-label',input.getAttribute('aria-label')||label?.textContent.trim()||'Parámetro');
   ui.title='Arrastra hacia arriba o a la derecha para aumentar. Flechas para ajustar; Mayús para ajuste fino.';
   ui.innerHTML='<svg viewBox="0 0 100 100" aria-hidden="true"><path class="sfx-knob-track" d="M25.25 74.75 A35 35 0 1 1 74.75 74.75" pathLength="100"/><path class="sfx-knob-progress" d="M25.25 74.75 A35 35 0 1 1 74.75 74.75" pathLength="100"/><circle class="sfx-knob-face" cx="50" cy="50" r="26"/><g class="sfx-knob-pointer"><path d="M50 31V42"/></g><circle class="sfx-knob-hub" cx="50" cy="50" r="3"/></svg>';
   input.before(ui);input.classList.add('sfx-knob-native');input.tabIndex=-1;input.setAttribute('aria-hidden','true');ui.append(input);knobs.set(input,ui);
   const limits=()=>({min:Number(input.min||0),max:Number(input.max||100),step:input.step==='any'?0:Number(input.step||1)});
   const set=value=>{const {min,max,step}=limits();const bounded=Math.max(min,Math.min(max,value));input.value=String(step?min+Math.round((bounded-min)/step)*step:bounded);input.dispatchEvent(new Event('input',{bubbles:true}));refresh(input,ui);};
   input.addEventListener('input',()=>refresh(input,ui));input.addEventListener('change',()=>refresh(input,ui));input.addEventListener('focus',()=>ui.focus());
   ui.addEventListener('keydown',e=>{const {min,max,step}=limits(),increment=step||(max-min)/100;let value=Number(input.value);switch(e.key){case 'ArrowUp':case 'ArrowRight':value+=increment;break;case 'ArrowDown':case 'ArrowLeft':value-=increment;break;case 'PageUp':value+=increment*10;break;case 'PageDown':value-=increment*10;break;case 'Home':value=min;break;case 'End':value=max;break;default:return;}e.preventDefault();set(value);input.dispatchEvent(new Event('change',{bubbles:true}));});
   let drag=null;
   ui.addEventListener('pointerdown',e=>{if(e.button!==0||drag||input.disabled)return;e.preventDefault();ui.focus();ui.setPointerCapture(e.pointerId);drag={id:e.pointerId,x:e.clientX,y:e.clientY,value:Number(input.value),distance:0};ui.classList.add('is-dragging');});
   ui.addEventListener('pointermove',e=>{if(!drag||drag.id!==e.pointerId)return;const dx=e.clientX-drag.x,dy=e.clientY-drag.y;drag.distance=Math.max(drag.distance,Math.hypot(dx,dy));if(drag.distance<3)return;const {min,max}=limits();set(drag.value+(dx-dy)*(max-min)/(e.shiftKey?1800:180));});
   const end=e=>{if(!drag||drag.id!==e.pointerId)return;if(e.type==='pointerup'&&drag.distance<3){const r=ui.getBoundingClientRect(),angle=Math.atan2(e.clientX-r.left-r.width/2,-(e.clientY-r.top-r.height/2))*180/Math.PI,{min,max}=limits();set(min+(Math.max(-135,Math.min(135,angle))+135)/270*(max-min));}drag=null;ui.classList.remove('is-dragging');if(ui.hasPointerCapture(e.pointerId))ui.releasePointerCapture(e.pointerId);input.dispatchEvent(new Event('change',{bubbles:true}));};
   ui.addEventListener('pointerup',end);ui.addEventListener('pointercancel',end);ui.addEventListener('lostpointercapture',()=>{drag=null;ui.classList.remove('is-dragging');});refresh(input,ui);
  });
 }
 function refresh(input,ui){const min=Number(input.min||0),max=Number(input.max||100),value=Number(input.value),ratio=max>min?(value-min)/(max-min):0;ui.style.setProperty('--knob-angle',`${-135+270*ratio}deg`);ui.style.setProperty('--knob-fill',String(Math.max(0,Math.min(100,ratio*100))));ui.setAttribute('aria-valuemin',String(min));ui.setAttribute('aria-valuemax',String(max));ui.setAttribute('aria-valuenow',String(value));const text=input.labels?.[0]?.querySelector('output')?.textContent||document.getElementById('timeval_'+input.dataset.time)?.textContent||String(value);ui.setAttribute('aria-valuetext',text);ui.setAttribute('aria-disabled',String(input.disabled));ui.tabIndex=input.disabled?-1:0;}
 const start=()=>{enhance();const home=document.querySelector('.sfx-home');if(home){const help=document.createElement('p');help.className='sfx-knob-help';help.textContent='Perillas: arrastra hacia arriba o abajo para ajustar; también puedes tocar el aro o usar las flechas del teclado. Mayús + arrastre permite un ajuste fino.';home.after(help);}new MutationObserver(enhance).observe(document.body,{childList:true,subtree:true,characterData:true});};
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start,{once:true});else start();
})();
