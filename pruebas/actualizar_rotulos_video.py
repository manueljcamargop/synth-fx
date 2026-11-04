"""Reproduce el cambio de marca de M03/M04 desde la carpeta de respaldo.
Requiere imageio-ffmpeg solo para esta operación de mantenimiento.
No cambia eventos, duración, resolución ni fotogramas por segundo.
"""
from pathlib import Path
import subprocess,json
import imageio_ffmpeg
root=Path(__file__).resolve().parents[1];src=root.parent/'SONOFX_LAB_Misiones_01_02_03_04_v0.4.0'
ffmpeg=imageio_ffmpeg.get_ffmpeg_exe();records=[]
for m in [3,4]:
 name=f'Escena_Muda_Mision_{m:02d}.mp4';target=root/name
 vf=f"drawbox=x=12:y=12:w=180:h=20:color=0x081423:t=fill,drawtext=fontfile=/System/Library/Fonts/Supplemental/Arial.ttf:text='Synth FX  |  ESCENA {m:02d}':x=16:y=16:fontsize=12:fontcolor=0xb4ccd4"
 subprocess.run([ffmpeg,'-y','-hide_banner','-loglevel','error','-i',str(src/name),'-map','0:v:0','-an','-vf',vf,'-c:v','libx264','-preset','slow','-crf','18','-profile:v','baseline','-pix_fmt','yuv420p','-movflags','+faststart',str(target)],check=True)
 # Decodificar todos los fotogramas y leer el progreso final (no solo la cabecera).
 run=subprocess.run([ffmpeg,'-hide_banner','-loglevel','error','-i',str(target),'-progress','pipe:1','-f','null','-'],capture_output=True,text=True,check=True)
 records.append({'file':name,'decode':'ok','progress':run.stdout})
(root/'pruebas'/'resultados'/'videos_revisados.json').write_text(json.dumps(records,indent=2))
