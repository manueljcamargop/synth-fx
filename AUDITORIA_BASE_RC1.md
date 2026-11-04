# Auditoría Synth FX v0.5.0-rc1

**Laboratorio Interactivo de Diseño Sonoro**  
Fecha: 3 de noviembre de 2026. Destinatarios: estudiantes universitarios de Ingeniería Multimedia / Diseño Sonoro.

## Estado de la entrega

Se revisó la aplicación existente, conservando sus cuatro misiones, aspecto visual, navegación, escenas Canvas y actividades. Es una **candidata a publicación**, pendiente de escucha crítica humana y de pruebas en dispositivos físicos. No se publicó en GitHub ni se creó integración con DAW.

La entrada disponible fue la carpeta consolidada `SONOFX_LAB_Misiones_01_02_03_04_v0.4.0`, ya extraída; no estaba el ZIP citado en el encargo. Antes de editar, se creó una copia independiente `Synth_FX_v0.5.0-rc1`. La carpeta v0.4.0 permanece intacta y se entrega además `Respaldo_SONOFX_LAB_v0.4.0.zip`. Los 11 archivos del respaldo ZIP se compararon por SHA-256 con la carpeta original (`pruebas/resultados_base_rc1/respaldo.json`).

## Cambios y errores corregidos

1. **Identificación inconsistente:** las misiones mostraban v0.1.0, v0.3.0 y v0.4.0. Se unificaron nombre, títulos, versión, metadatos, encabezados, pies, fichas y nombres de descargas a Synth FX v0.5.0-rc1. Los nombres y rutas de los HTML se conservaron.
2. **Formas de onda incompletas:** M01 no ofrecía triangular y M02 no ofrecía cuadrada. Ahora ambas conservan el selector y añaden cuatro representaciones SVG seleccionables, nombre, estado accesible y escucha individual. M03/M04 conservan sus botones y sus escuchas de onda seleccionada; se corrigieron las siluetas para mostrar discontinuidades y segmentos exactos.
3. **Coherencia espectral:** se incorporaron coeficientes de onda triangular y sentido coherente de sierra en el generador aditivo de M01. Se eliminaron componentes tonales añadidas de aproximadamente media frecuencia en M02/M04: hacían que la fuente explicada como senoidal incluyera otra frecuencia y confundían la fundamental. El ruido y las modulaciones siguen siendo capas explícitas del efecto.
4. **Aliasing:** M01 mantiene su suma armónica limitada por Nyquist y a 16 parciales. M02–M04 utilizan corrección PolyBLEP en sierra/cuadrada. Es una reducción del aliasing; no se afirma una reconstrucción ideal sin error en todas las frecuencias. La triangular usa una función continua con esquinas.
5. **Diferencias de nivel entre escucha y WAV:** M01 aplicaba otra ganancia de 0,74 al reproducir, adicional a la normalización ya realizada; se eliminó. M04 atenuaba la escucha mono al convertirla a estéreo con panorámica central; ahora duplica la señal de capa sin esa atenuación. Se igualaron también sus duraciones de escucha y exportación: maquinaria 4 s, alarma 3 s, interfaz según el control.
6. **Frecuencia de muestreo de M01:** escucha y exportación generan ahora el mismo PCM de 44,1 kHz; Web Audio realiza la adaptación al dispositivo si es necesaria. M02 conserva sus 32 kHz estéreo válidos y M03/M04 sus 44,1 kHz.
7. **Riesgo de saturación en M03:** se retiró el recorte duro de muestras del evento y se aplicó reducción global si su pico excede 0,91. La banda completa también reduce su suma cuando es necesario. La reproducción de secuencia/escena usa esa misma mezcla normalizada que se exporta.
8. **Transitorios de final de evento:** se añadió una rampa corta de salida en M03 para reducir discontinuidades al terminar efectos breves.
9. **Desfase por cálculo y relojes:** se genera el PCM antes de fijar el origen temporal; M03 y M04 usan el reloj del contexto de audio para la imagen cuando hay sonido. La previsualización muda conserva su reloj visual. Las posiciones equivocadas iniciales siguen siendo ejercicios deliberados, no defectos corregidos automáticamente.
10. **Carrera reproducir/detener:** la primera prueba detectó fuentes activas después de detener de inmediato. Se añadieron identificadores de solicitud y comprobación tras ceder al bucle de microtareas para invalidar reproducciones pendientes. La repetición final terminó con cero fuentes activas.
11. **Ciclo de vida:** se detienen escenas y sonidos al abandonar/ocultar la página y cambiar de actividad; las fuentes terminadas se desconectan. M02 desconecta también sus fuentes al terminar naturalmente. La demostración de ondas se cancela ante otra acción de la aplicación.
12. **Recursos audiovisuales poco accesibles:** cada misión incluye ahora un reproductor MP4 `controls playsinline`, enlace de descarga y explicación de la relación entre video y Canvas. Se añadió regreso al inicio.
13. **Marca antigua en video:** M03/M04 contenían SONOFX LAB incrustado. Se sustituyó solo la placa de marca, reencodificando H.264 con inicio rápido. No se cambiaron acciones, duración, resolución, frecuencia de fotogramas ni ubicación de eventos. M01/M02 conservan sus MP4 originales byte por byte. Los archivos anteriores se conservan en el respaldo.
14. **Documentación:** se añadieron este informe, matriz de controles, CSV WAV, instrucciones de uso/publicación, scripts y resultados verificables. No hay bibliotecas externas en la aplicación; Playwright y FFmpeg se utilizaron únicamente como herramientas de auditoría.

## Revisión acústica y pedagógica

Se conserva la progresión **observar → escuchar → experimentar → fabricar → sincronizar → reflexionar**, distribuida en las cinco etapas originales de cada misión. Las comparaciones cambian parámetros acústicos identificables y las respuestas explican el razonamiento. Se ejercitaron todas las alternativas de los controles de respuesta de la batería y se verificaron las respuestas correctas de los cuestionarios: 4 en M01, 5 en M02, 5 en M03 y 4 en M04.

Las explicaciones distinguen forma de onda, altura, brillo, envolvente y ubicación temporal. Los SVG representan ondas periódicas ideales; el efecto final incluye envolventes, filtrado y posibles capas de ruido. La DFT del generador compartido confirmó: senoidal sin armónicos adicionales; triangular con tercer armónico ≈ 1/9; cuadrada con tercero ≈ 1/3 y segundo despreciable; sierra con segundo ≈ 1/2 y tercero ≈ 1/3. Estos datos no son mediciones del altavoz.

Los filtros implementados son pasa-bajos digitales de un polo; no existe un parámetro de resonancia Q que se pueda auditar como tal. La resonancia descriptiva de un choque se refiere a su carácter tonal transitorio. Las envolventes son modelos de ataque, decaimiento, sostenimiento o salida según el efecto; **no todas implementan las cuatro fases ADSR independientes**. El LFO de M02 modula frecuencia; M03/M04 combinan modulación de frecuencia y/o amplitud según su modelo. El ruido es determinista y aperiódico a escala perceptual, filtrado cuando corresponde.

El motor de nave y las espadas se presentan como convenciones narrativas de ciencia ficción. Se conserva la aclaración de que el sonido requiere un medio material y no se propaga por el vacío. No se añadieron actividades musicales, tutoriales de DAW ni nuevas misiones.

## Pruebas ejecutadas

- **Google Chrome 156.0.8078.80 en macOS**, automatizado/headless: 209 interacciones de controles, 35 casos adicionales de escucha por preset/evento/capa y 190 comprobaciones de extremos de deslizadores. **Cero fallos registrados** en la última batería.
- **WebKit 26.4 de Playwright en macOS**, automatizado: la misma batería de 209 controles, 35 variantes y 190 extremos. **Cero fallos registrados**. No equivale al Safari instalado ni a un iPhone físico. Después de unificar la tasa de M01 se repitió su batería en WebKit: 42 controles y WAV, sin fallos (`webkit_m1.json`).
- Los botones sonoros se comprobaron capturando las fuentes reales creadas por sus manejadores, midiendo pico/RMS y volviendo a renderizar sus buffers con `OfflineAudioContext`. Todos los casos sonoros esperados registraron energía mayor que cero y muestras finitas por debajo de 1.
- Se midió además la señal en ramas de análisis conectadas al nodo que alimenta `AudioDestinationNode`, para confirmar actividad en el grafo de salida. Se conservaron el destino original y el nivel original; la rama de medición queda silenciada para evitar duplicación. La instrumentación se inyecta únicamente durante la prueba, no forma parte del producto.
- Se ejecutaron pruebas de clics rápidos, detención inmediata, respuestas correctas, navegación, selectores, presets, restauración, descarga y cambios de parámetro. Los registros completos contienen las diferencias numéricas y casos de cero intencional, por ejemplo nivel o ruido en cero.
- Se revisó el diseño con 1440 y 390 píxeles de ancho en las cinco etapas de las cuatro misiones: sin desbordamiento horizontal detectado. **390 px es simulación de tamaño, no Android/iPhone real**.
- Se abrieron las páginas finales por `file://`; Chrome también con emulación de red desconectada. WebKit funciona por `file://` sin esa emulación: `set_offline(True)` produjo un error interno del motor automatizado y no se usa como evidencia de fallo de la aplicación. No hay solicitudes externas necesarias para ejecutar la app.

| Misión | Controles de la batería | Controles que generaron fuentes | Casos adicionales de escucha |
|---|---:|---:|---:|
| 01 | 42 | 9 | 1 |
| 02 | 54 | 12 | 3 |
| 03 | 61 | 16 | 25 |
| 04 | 52 | 13 | 6 |

La tabla individual está en [CONTROLES_VERIFICADOS.md](CONTROLES_VERIFICADOS.md). La navegación adicional por botones y flechas figura en `compatibilidad.json`: 170 acciones entre ambos motores, más reproducción/seek/final de los cuatro MP4 en cada motor.

### Medición de salida del grafo

Se midió un sonido de fabricación por misión en su configuración de inicio. Las cifras dependen de ese instante y no representan sonoridad percibida ni calibración de auriculares.

| Misión | RMS | Pico |
|---|---:|---:|
| 01 | 0.371502 | 0.593279 |
| 02 | 0.101232 | 0.183974 |
| 03 | 0.135784 | 0.268828 |
| 04 | 0.038901 | 0.077542 |

### Exportaciones WAV

Se capturaron **12 archivos distintos por motor**, con cabeceras RIFF/WAVE PCM de 16 bits y carga útil legible mediante el módulo `wave` de Python. Se midieron duración, canales, tasa, pico y RMS; ningún archivo medido presentó muestras a escala completa ni silencio inesperado. La diferencia de una muestra en algunas duraciones procede del redondeo a muestras enteras.

| Archivo | Duración (s) | Hz | Canales | Pico | RMS |
|---|---:|---:|---:|---:|---:|
| SynthFX_Laser_Mision01.wav | 0.36000 | 44100 | 1 | 0.73999 | 0.28895 |
| SynthFX_M03_Banda_Efectos_15s.wav | 15.00000 | 44100 | 1 | 0.91000 | 0.16615 |
| SynthFX_M03_apagado.wav | 0.92000 | 44100 | 1 | 0.34476 | 0.10133 |
| SynthFX_M03_choque.wav | 1.10002 | 44100 | 1 | 0.79758 | 0.16824 |
| SynthFX_M03_encendido.wav | 1.05000 | 44100 | 1 | 0.43997 | 0.16019 |
| SynthFX_M03_movimiento.wav | 0.75000 | 44100 | 1 | 0.42136 | 0.12117 |
| SynthFX_M03_zumbido.wav | 2.60000 | 44100 | 1 | 0.42773 | 0.21545 |
| SynthFX_M04_Ambiente_Sala_Control_14s.wav | 14.00000 | 44100 | 2 | 0.37616 | 0.07667 |
| SynthFX_M04_alarm.wav | 3.00000 | 44100 | 1 | 0.22095 | 0.13926 |
| SynthFX_M04_amb.wav | 4.00000 | 44100 | 1 | 0.14664 | 0.07158 |
| SynthFX_M04_ui.wav | 0.19000 | 44100 | 1 | 0.15863 | 0.05283 |
| SynthFX_Mision02_MotorNave.wav | 4.20000 | 32000 | 2 | 0.47177 | 0.12342 |

`RESULTADOS_WAV.csv` ofrece los mismos datos. En una prueba independiente, el WAV descargado y el buffer de la escucha del mismo diseño se compararon muestra a muestra para las cuatro misiones. Todos coincidieron dentro de **2/32768**, tolerancia conservadora de cuantización PCM de 16 bits:

| Misión | Máximo error absoluto |
|---|---:|
| 01 | 0.00003487 |
| 02 | 0.00002483 |
| 03 | 0.00002739 |
| 04 | 0.00003482 |

No se ha realizado todavía una importación real en REAPER o MorningDAW. El formato PCM WAV se verificó; su reconocimiento en esos programas sigue siendo una prueba manual pendiente.

### Escenas y sincronización

Los cuatro MP4 se decodificaron completamente con FFmpeg: M01 **288 fotogramas / 12 s**, M02 **180 / 12 s**, M03 **300 / 15 s**, M04 **224 / 14 s**. No contienen pistas sonoras. Se verifican también reproducción, búsqueda a posiciones concretas y llegada a `ended` en Chrome y WebKit por archivo local en `compatibilidad.json`.

La primera prueba HTTP con el servidor básico de Python devolvió posición cero en algunas búsquedas; ese servidor no implementa HTTP Range. Esas lecturas están conservadas en los JSON y **no se cuentan como seek correcto**. La comprobación final usa `file://` y verifica posiciones reales de 1 s, 3 s y cerca del final. GitHub Pages debe verificarse nuevamente al publicar.

Los referentes Canvas se conservan: M01 6,20 s; M02 2,40 s; M03 1,30 / 2,10 / 5,60 / 8,40 / 11,70 s; M04 interfaz 2,20 s y alarma 8,70 s. Se comprobó el origen temporal programado con el reloj de audio y el avance del reloj visual. No se midió la latencia física pantalla–altavoz ni la latencia Bluetooth.

## Límites y pruebas manuales pendientes

1. **Escucha crítica humana:** verificar que los pares A/B resulten claros para estudiantes, que el nivel sea cómodo y que no se perciban clics o silencios anómalos. La energía numérica no sustituye esa escucha.
2. **Equipos físicos:** Android, iPhone, Windows y Safari instalado no se probaron. Comprobar toque inicial, descargas, selección de destino, retorno desde segundo plano, cambio de orientación y escenas completas en cada equipo.
3. **Sincronía percibida:** revisar eventos visuales con auriculares cableados y altavoz. La tolerancia didáctica de M03 (0,25 s) es una aproximación del ejercicio, no un estándar de sincronía profesional.
4. **WAV en DAW:** importar al menos un evento y una banda completa en REAPER/MorningDAW y comprobar duración, canalización y nivel. No se modificaron los DAW.
5. **Carga extrema:** las pruebas cubren los casos registrados y extremos individuales; no demuestran todas las combinaciones simultáneas de parámetros, todos los dispositivos ni escucha prolongada de una clase completa.
6. **Accesibilidad:** hay nombres de controles, foco y estado de selección; falta una revisión con lector de pantalla y usuarios. La escena visual no posee una audiodescripción completa.
7. **Disponibilidad offline:** distribuir la carpeta completa o el ZIP. Las misiones ya comparten `synthfx.js` y `synthfx.css`; no distribuir un HTML aislado. Visitar una página web publicada no instala una copia offline.

La etiqueta **rc1** se mantiene hasta cerrar esas comprobaciones. No se afirma compatibilidad universal ni estabilidad certificada.

## Reproducción de las pruebas

Desde esta carpeta, con Python y Google Chrome instalado en la ruta estándar de macOS:

```sh
python3 -m venv /tmp/synthfx-qa
/tmp/synthfx-qa/bin/pip install playwright imageio-ffmpeg
/tmp/synthfx-qa/bin/python -m playwright install webkit
/tmp/synthfx-qa/bin/python pruebas/verificar.py
/tmp/synthfx-qa/bin/python pruebas/verificar.py --webkit
/tmp/synthfx-qa/bin/python pruebas/compatibilidad.py
/tmp/synthfx-qa/bin/python pruebas/mediciones.py
```

Las dependencias anteriores pertenecen exclusivamente a QA. Para usar Synth FX, abrir `index.html` sin instalación. Los scripts que exponen `__qa` lo hacen sobre una copia HTML servida en memoria; los archivos finales no incluyen ese acceso. `actualizar_rotulos_video.py` documenta la operación de rotulación y requiere conservar el respaldo original.

## Publicación futura y referencias

Seguir [PUBLICACION_GITHUB_PAGES.md](PUBLICACION_GITHUB_PAGES.md) cuando exista autorización. Se incluye `.nojekyll`; no hay compilación ni servicios externos.

Referencias técnicas consultadas: [Web Audio del W3C, borrador 1.1](https://www.w3.org/TR/webaudio/), [OfflineAudioContext](https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioContext), [programación de AudioBufferSourceNode](https://developer.mozilla.org/en-US/docs/Web/API/AudioBufferSourceNode/start), [formas de onda](https://developer.mozilla.org/en-US/docs/Web/API/OscillatorNode/type) y [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site). Los resultados de esta auditoría proceden de los archivos y pruebas entregados.
