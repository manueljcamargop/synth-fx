# Controles verificados — Synth FX v0.5.0-rc1

Fecha: 2026-11-03. Cada fila corresponde a una interacción de la batería completa; las etapas se numeran de 1 a 5. Chrome y WebKit completaron estas interacciones. Los números miden casos ejecutados, no cobertura formal de todas las combinaciones posibles.

| Misión | Etapa | Control | Identificador | Evidencia sonora en Chrome |
|---|---:|---|---|---|
| 01 | 1 | ▶ Ver escena sin sonido | `#playScene0` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 1 | ■ Detener | `#stopScene0` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 2 | ▶ Escuchar A | `#listenA` | 1 fuente(s), pico 0.7400; render OfflineAudioContext con energía > 0 |
| 01 | 2 | ▶ Escuchar B | `#listenB` | 1 fuente(s), pico 0.7400; render OfflineAudioContext con energía > 0 |
| 01 | 2 | ⇄ Comparar A/B | `#listenAB` | 2 fuente(s), pico 0.7400; render OfflineAudioContext con energía > 0 |
| 01 | 2 | ■ Detener audio | `■ Detener audio` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 2 | Un sonido que conserva la misma frecuencia. | `[data-answer="a"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 2 | Un sonido que empieza agudo y baja rápidamente. | `[data-answer="b"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 2 | Un sonido que empieza grave y sube rápidamente. | `[data-answer="c"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 2 | ¿Necesitas una pista? | `#hintPitch` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 3 | ⚡ Láser breve | `[data-preset="classic"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 3 | ◈ Láser pesado | `[data-preset="heavy"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 3 | ⌁ Pulso suave | `[data-preset="soft"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 3 | Diente de sierra | `[data-sfx-wave="saw"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 3 | ▶ Escuchar | `▶ Escuchar` | 1 fuente(s), pico 0.2180; render OfflineAudioContext con energía > 0 |
| 01 | 3 | Triangular | `[data-sfx-wave="triangle"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 3 | ▶ Escuchar | `▶ Escuchar` | 1 fuente(s), pico 0.2200; render OfflineAudioContext con energía > 0 |
| 01 | 3 | Senoidal | `[data-sfx-wave="sine"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 3 | ▶ Escuchar | `▶ Escuchar` | 1 fuente(s), pico 0.2200; render OfflineAudioContext con energía > 0 |
| 01 | 3 | Cuadrada | `[data-sfx-wave="square"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 3 | ▶ Escuchar | `▶ Escuchar` | 1 fuente(s), pico 0.2200; render OfflineAudioContext con energía > 0 |
| 01 | 3 | ▶ Probar mi disparo | `#playCustom` | 1 fuente(s), pico 0.7400; render OfflineAudioContext con energía > 0 |
| 01 | 3 | ■ Detener | `■ Detener` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 3 | ↓ Exportar efecto WAV | `#downloadWav` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 4 | ▶ Reproducir escena + sonido | `#playSynced` | 1 fuente(s), pico 0.7400; render OfflineAudioContext con energía > 0 |
| 01 | 4 | ■ Detener | `#stopScene3` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 4 | ✓ Analizar sincronía | `#analyzeSync` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 4 | ◎ Ajustar al destello | `#alignSync` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | Mantener la frecuencia constante | `[data-quiz="0"][data-opt="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | Hacer un barrido rápido de agudo a grave | `[data-quiz="0"][data-opt="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | Subir el volumen sin cambiar la frecuencia | `[data-quiz="0"][data-opt="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | El contenido de armónicos y, por tanto, el timbre | `[data-quiz="1"][data-opt="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | La posición del clip en la escena | `[data-quiz="1"][data-opt="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | La duración del video | `[data-quiz="1"][data-opt="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | El brillo de la interfaz | `[data-quiz="2"][data-opt="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | La duración y el tiempo de ataque, según el efecto | `[data-quiz="2"][data-opt="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | La velocidad de reproducción del video | `[data-quiz="2"][data-opt="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | En cualquier lugar si el efecto es bonito | `[data-quiz="3"][data-opt="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | A los 6,20 s, y luego verificas escuchando | `[data-quiz="3"][data-opt="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | Siempre al comenzar el video (0 s) | `[data-quiz="3"][data-opt="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | ↓ Descargar mi disparo WAV | `#downloadWav2` | Clic ejecutado; sin fuente sonora prevista |
| 01 | 5 | Revisar respuestas | `#evaluateQuiz` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 1 | ▶ Ver escena muda | `#play0` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 1 | ■ Detener | `#stop0` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 2 | ▶ Escuchar A | `[data-hear="0"][data-ab="A"]` | 1 fuente(s), pico 0.2490; render OfflineAudioContext con energía > 0 |
| 02 | 2 | ▶ Escuchar B | `[data-hear="0"][data-ab="B"]` | 1 fuente(s), pico 0.3460; render OfflineAudioContext con energía > 0 |
| 02 | 2 | A aumenta claramente la altura | `[data-answer="0"][data-choice="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 2 | B aumenta claramente la altura | `[data-answer="0"][data-choice="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 2 | Ambos tienen idéntica altura | `[data-answer="0"][data-choice="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 2 | ▶ Escuchar A | `[data-hear="1"][data-ab="A"]` | 1 fuente(s), pico 0.2604; render OfflineAudioContext con energía > 0 |
| 02 | 2 | ▶ Escuchar B | `[data-hear="1"][data-ab="B"]` | 1 fuente(s), pico 0.2216; render OfflineAudioContext con energía > 0 |
| 02 | 2 | A conserva más componentes agudos | `[data-answer="1"][data-choice="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 2 | B conserva más componentes agudos | `[data-answer="1"][data-choice="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 2 | El filtro cambia la duración del video | `[data-answer="1"][data-choice="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 2 | ▶ Escuchar A | `[data-hear="2"][data-ab="A"]` | 1 fuente(s), pico 0.2451; render OfflineAudioContext con energía > 0 |
| 02 | 2 | ▶ Escuchar B | `[data-hear="2"][data-ab="B"]` | 1 fuente(s), pico 0.2445; render OfflineAudioContext con energía > 0 |
| 02 | 2 | A tiene vibrato más pronunciado | `[data-answer="2"][data-choice="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 2 | B tiene vibrato más pronunciado | `[data-answer="2"][data-choice="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 2 | El LFO solo sirve para crear melodías | `[data-answer="2"][data-choice="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 2 | ■ Detener audio | `#stopAB` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 3 | ✦ Nave exploradora | `[data-preset="exploradora"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 3 | ▣ Carguero pesado | `[data-preset="carguero"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 3 | ⚡ Interceptora | `[data-preset="interceptora"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 3 | Diente de sierra | `[data-sfx-wave="saw"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 3 | ▶ Escuchar | `▶ Escuchar` | 1 fuente(s), pico 0.2180; render OfflineAudioContext con energía > 0 |
| 02 | 3 | Cuadrada | `[data-sfx-wave="square"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 3 | ▶ Escuchar | `▶ Escuchar` | 1 fuente(s), pico 0.2200; render OfflineAudioContext con energía > 0 |
| 02 | 3 | Triangular | `[data-sfx-wave="tri"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 3 | ▶ Escuchar | `▶ Escuchar` | 1 fuente(s), pico 0.2200; render OfflineAudioContext con energía > 0 |
| 02 | 3 | Senoidal | `[data-sfx-wave="sine"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 3 | ▶ Escuchar | `▶ Escuchar` | 1 fuente(s), pico 0.2200; render OfflineAudioContext con energía > 0 |
| 02 | 3 | ▶ Escuchar mi motor | `#hearEngine` | 1 fuente(s), pico 0.4965; render OfflineAudioContext con energía > 0 |
| 02 | 3 | ■ Detener | `#stopEngine` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 3 | ↓ Descargar WAV | `#exportEngine` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 4 | ▶ Escuchar con imagen | `#play3` | 1 fuente(s), pico 0.4965; render OfflineAudioContext con energía > 0 |
| 02 | 4 | ■ Detener | `#stop3` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 4 | Comprobar sincronía | `#checkSync` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 4 | Pista: alinear con el destello | `#syncHelp` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | Aumentar el corte del filtro pasa-bajos | `[data-q="0"][data-c="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | Mover el clip en la línea de tiempo | `[data-q="0"][data-c="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | Cambiar la duración del video | `[data-q="0"][data-c="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | Incrementar el barrido de pitch | `[data-q="1"][data-c="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | Bajar el brillo de la pantalla | `[data-q="1"][data-c="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | Aumentar el volumen solamente | `[data-q="1"][data-c="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | Vibración periódica de la altura | `[data-q="2"][data-c="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | Cambia automáticamente la resolución del video | `[data-q="2"][data-c="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | Convierte el ruido en una melodía | `[data-q="2"][data-c="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | Su espectro armónico | `[data-q="3"][data-c="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | Su posición temporal respecto a la imagen | `[data-q="3"][data-c="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | La forma de onda del sintetizador | `[data-q="3"][data-c="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | El sonido viaja libremente por el vacío | `[data-q="4"][data-c="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | El sonido que diseñamos es una convención de ficción audiovisual | `[data-q="4"][data-c="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | Todas las naves reales tienen motor de diente de sierra | `[data-q="4"][data-c="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | Evaluar mis respuestas | `#grade` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | ↓ Exportar mi motor WAV | `#exportFinal` | Clic ejecutado; sin fuente sonora prevista |
| 02 | 5 | ↓ Guardar ficha técnica TXT | `#exportSettings` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 2 | ▶ Escuchar A | `[data-listen="0"][data-side="a"]` | 1 fuente(s), pico 0.3922; render OfflineAudioContext con energía > 0 |
| 03 | 2 | ▶ Escuchar B | `[data-listen="0"][data-side="b"]` | 1 fuente(s), pico 0.4673; render OfflineAudioContext con energía > 0 |
| 03 | 2 | ▶ Comparar A / B | `[data-listen="0"][data-side="ab"]` | 2 fuente(s), pico 0.4673; render OfflineAudioContext con energía > 0 |
| 03 | 2 | ■ Detener | `[data-listen="0"][data-side="stop"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 2 | A: zumbido estable | `[data-answer="0"][data-option="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 2 | B: zumbido oscilante | `[data-answer="0"][data-option="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 2 | ▶ Escuchar A | `[data-listen="1"][data-side="a"]` | 1 fuente(s), pico 0.5073; render OfflineAudioContext con energía > 0 |
| 03 | 2 | ▶ Escuchar B | `[data-listen="1"][data-side="b"]` | 1 fuente(s), pico 0.3868; render OfflineAudioContext con energía > 0 |
| 03 | 2 | ▶ Comparar A / B | `[data-listen="1"][data-side="ab"]` | 2 fuente(s), pico 0.5073; render OfflineAudioContext con energía > 0 |
| 03 | 2 | ■ Detener | `[data-listen="1"][data-side="stop"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 2 | A: barrido con más ruido | `[data-answer="1"][data-option="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 2 | B: barrido casi tonal | `[data-answer="1"][data-option="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 2 | ▶ Escuchar A | `[data-listen="2"][data-side="a"]` | 1 fuente(s), pico 0.8272; render OfflineAudioContext con energía > 0 |
| 03 | 2 | ▶ Escuchar B | `[data-listen="2"][data-side="b"]` | 1 fuente(s), pico 0.4934; render OfflineAudioContext con energía > 0 |
| 03 | 2 | ▶ Comparar A / B | `[data-listen="2"][data-side="ab"]` | 2 fuente(s), pico 0.8272; render OfflineAudioContext con energía > 0 |
| 03 | 2 | ■ Detener | `[data-listen="2"][data-side="stop"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 2 | A: choque más brillante al inicio | `[data-answer="2"][data-option="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 2 | B: choque menos brillante al inicio | `[data-answer="2"][data-option="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 3 | Restablecer este evento | `#restore` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 3 | Encendido | `[data-cue="encendido"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 3 | Zumbido | `[data-cue="zumbido"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 3 | Movimiento | `[data-cue="movimiento"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 3 | Choque | `[data-cue="choque"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 3 | Apagado | `[data-cue="apagado"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 3 | Senoidal | `[data-wave="sine"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 3 | Triangular | `[data-wave="triangle"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 3 | Cuadrada | `[data-wave="square"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 3 | Diente de sierra | `[data-wave="saw"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 3 | ▶ Escuchar solo la onda | `#waveListen` | 1 fuente(s), pico 0.3901; render OfflineAudioContext con energía > 0 |
| 03 | 3 | ▶ Núcleo | `#playTone` | 1 fuente(s), pico 0.3333; render OfflineAudioContext con energía > 0 |
| 03 | 3 | ▶ Textura | `#playNoise` | 1 fuente(s), pico 0.0235; render OfflineAudioContext con energía > 0 |
| 03 | 3 | ▶ Chispa | `#playSpark` | 1 fuente(s), pico 0.0070; render OfflineAudioContext con energía > 0 |
| 03 | 3 | ▶ Mezcla completa | `#playFull` | 1 fuente(s), pico 0.3448; render OfflineAudioContext con energía > 0 |
| 03 | 3 | ■ Detener | `#stopSound` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 3 | ▶ Escuchar diseño completo | `#playAll` | 1 fuente(s), pico 0.9100; render OfflineAudioContext con energía > 0 |
| 03 | 3 | ↓ Descargar WAV del evento elegido | `#exportPack` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 3 | Necesito una pista | `#hintLab` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 4 | ▶ Reproducir con sonido | `#scenePlay` | 1 fuente(s), pico 0.9100; render OfflineAudioContext con energía > 0 |
| 03 | 4 | ▶ Ver sin sonido | `#sceneMute` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 4 | ■ Detener | `#sceneStop` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 4 | Comprobar sincronía | `#checkSync` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 4 | Reiniciar posiciones | `#resetTiming` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 4 | Ver puntos de referencia | `#showGuide` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 4 | ↓ Descargar banda de efectos WAV (15 s) | `#exportScene` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Un impulso de pocos milisegundos | `[data-quiz="0"][data-choice="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Una señal sostenida con envolvente y modulación controladas | `[data-quiz="0"][data-choice="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Un silencio entre cada fotograma | `[data-quiz="0"][data-choice="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Aumentar la chispa transitoria inicial | `[data-quiz="1"][data-choice="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Eliminar la envolvente de amplitud | `[data-quiz="1"][data-choice="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Bajar el volumen de toda la escena a cero | `[data-quiz="1"][data-choice="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Una altura musical exacta | `[data-quiz="2"][data-choice="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Una textura aperiódica de aire o fricción | `[data-quiz="2"][data-choice="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Una progresión armónica | `[data-quiz="2"][data-choice="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | La forma de onda triangular | `[data-quiz="3"][data-choice="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | La sincronización temporal | `[data-quiz="3"][data-choice="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | La ausencia de una melodía | `[data-quiz="3"][data-choice="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Mayor riqueza armónica | `[data-quiz="4"][data-choice="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Que se eliminen todos los armónicos | `[data-quiz="4"][data-choice="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Que el sonido se convierta en una grabación real | `[data-quiz="4"][data-choice="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Evaluar comprensión | `#grade` | Clic ejecutado; sin fuente sonora prevista |
| 03 | 5 | Borrar respuestas | `#retry` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 1 | ▶ Ver escena muda | `#playVisualIntro` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 1 | ■ Detener | `#stopVisualIntro` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 2 | ▶ Escuchar A | `[data-ex="0"][data-side="a"]` | 1 fuente(s), pico 0.0964; render OfflineAudioContext con energía > 0 |
| 04 | 2 | ▶ Escuchar B | `[data-ex="0"][data-side="b"]` | 1 fuente(s), pico 0.1231; render OfflineAudioContext con energía > 0 |
| 04 | 2 | ▶ Comparar A/B | `[data-ex="0"][data-side="ab"]` | 1 fuente(s), pico 0.1231; render OfflineAudioContext con energía > 0 |
| 04 | 2 | ■ Detener | `[data-ex="0"][data-side="stop"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 2 | El sonido A | `[data-exanswer="0"][data-val="a"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 2 | El sonido B | `[data-exanswer="0"][data-val="b"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 2 | ▶ Escuchar A | `[data-ex="1"][data-side="a"]` | 1 fuente(s), pico 0.1190; render OfflineAudioContext con energía > 0 |
| 04 | 2 | ▶ Escuchar B | `[data-ex="1"][data-side="b"]` | 1 fuente(s), pico 0.0549; render OfflineAudioContext con energía > 0 |
| 04 | 2 | ▶ Comparar A/B | `[data-ex="1"][data-side="ab"]` | 1 fuente(s), pico 0.1190; render OfflineAudioContext con energía > 0 |
| 04 | 2 | ■ Detener | `[data-ex="1"][data-side="stop"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 2 | El sonido A | `[data-exanswer="1"][data-val="a"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 2 | El sonido B | `[data-exanswer="1"][data-val="b"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 2 | ▶ Escuchar A | `[data-ex="2"][data-side="a"]` | 1 fuente(s), pico 0.1568; render OfflineAudioContext con energía > 0 |
| 04 | 2 | ▶ Escuchar B | `[data-ex="2"][data-side="b"]` | 1 fuente(s), pico 0.1561; render OfflineAudioContext con energía > 0 |
| 04 | 2 | ▶ Comparar A/B | `[data-ex="2"][data-side="ab"]` | 1 fuente(s), pico 0.1568; render OfflineAudioContext con energía > 0 |
| 04 | 2 | ■ Detener | `[data-ex="2"][data-side="stop"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 2 | El sonido A | `[data-exanswer="2"][data-val="a"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 2 | El sonido B | `[data-exanswer="2"][data-val="b"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 3 | Atmósfera de maquinaria | `[data-layer="amb"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 3 | Confirmaciones de la interfaz | `[data-layer="ui"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 3 | Alarma tecnológica | `[data-layer="alarm"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 3 | Senoidal | `[data-wave="sine"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 3 | Triangular | `[data-wave="triangle"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 3 | Cuadrada | `[data-wave="square"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 3 | Diente de sierra | `[data-wave="saw"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 3 | ▶ Oír solo esta forma de onda | `#hearWave` | 1 fuente(s), pico 0.1255; render OfflineAudioContext con energía > 0 |
| 04 | 3 | ▶ Escuchar capa | `#playLayer` | 1 fuente(s), pico 0.2043; render OfflineAudioContext con energía > 0 |
| 04 | 3 | ▶ Escuchar combinación | `#playAll` | 1 fuente(s), pico 0.2593; render OfflineAudioContext con energía > 0 |
| 04 | 3 | ■ Detener | `#stopAudio` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 3 | ↓ Exportar esta capa WAV | `#exportLayer` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 3 | Restablecer capa | `#restoreLayer` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 4 | ▶ Reproducir con sonido | `#playScene` | 1 fuente(s), pico 0.3792; render OfflineAudioContext con energía > 0 |
| 04 | 4 | ▶ Solo imagen | `#playSceneMute` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 4 | ■ Detener | `#stopScene` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 4 | Alinear con la escena | `#autoSync` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 4 | ↓ Exportar mezcla WAV | `#exportMix` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | Establece una sensación de espacio y continuidad. | `[data-q="0"][data-a="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | Sustituye siempre todos los efectos puntuales. | `[data-q="0"][data-a="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | Produce automáticamente un diálogo. | `[data-q="0"][data-a="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | aumentan los agudos. | `[data-q="1"][data-a="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | se atenúan progresivamente componentes altas. | `[data-q="1"][data-a="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | se acelera la escena de video. | `[data-q="1"][data-a="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | La tasa de pulsos. | `[data-q="2"][data-a="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | El nombre del archivo WAV. | `[data-q="2"][data-a="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | La frecuencia de muestreo del proyecto. | `[data-q="2"][data-a="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | Colocarla al azar y subir volumen. | `[data-q="3"][data-a="0"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | Ajustar su inicio según el acontecimiento visual y la intención narrativa. | `[data-q="3"][data-a="1"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | Convertirla en una melodía obligatoriamente. | `[data-q="3"][data-a="2"]` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | Repetir evaluación | `#resetQuiz` | Clic ejecutado; sin fuente sonora prevista |
| 04 | 5 | ↓ Descargar ficha de práctica (TXT) | `#downloadSummary` | Clic ejecutado; sin fuente sonora prevista |

## Variantes de eventos, capas y presets

| Misión | Caso | Botón | Pico |
|---|---|---|---:|
| 01 | default | `playCustom` | 0.7400 |
| 02 | exploradora | `hearEngine` | 0.3412 |
| 02 | carguero | `hearEngine` | 0.2412 |
| 02 | interceptora | `hearEngine` | 0.4718 |
| 03 | encendido | `playTone` | 0.4122 |
| 03 | encendido | `playNoise` | 0.0379 |
| 03 | encendido | `playSpark` | 0.0238 |
| 03 | encendido | `playFull` | 0.4400 |
| 03 | encendido | `waveListen` | 0.3901 |
| 03 | zumbido | `playTone` | 0.4128 |
| 03 | zumbido | `playNoise` | 0.0205 |
| 03 | zumbido | `playSpark` | 0.0044 |
| 03 | zumbido | `playFull` | 0.4277 |
| 03 | zumbido | `waveListen` | 0.3925 |
| 03 | movimiento | `playTone` | 0.3739 |
| 03 | movimiento | `playNoise` | 0.0914 |
| 03 | movimiento | `playSpark` | 0.0089 |
| 03 | movimiento | `playFull` | 0.4214 |
| 03 | movimiento | `waveListen` | 0.3901 |
| 03 | choque | `playTone` | 0.3963 |
| 03 | choque | `playNoise` | 0.1595 |
| 03 | choque | `playSpark` | 0.3193 |
| 03 | choque | `playFull` | 0.7976 |
| 03 | choque | `waveListen` | 0.3956 |
| 03 | apagado | `playTone` | 0.3333 |
| 03 | apagado | `playNoise` | 0.0235 |
| 03 | apagado | `playSpark` | 0.0070 |
| 03 | apagado | `playFull` | 0.3448 |
| 03 | apagado | `waveListen` | 0.3901 |
| 04 | amb | `playLayer` | 0.1467 |
| 04 | amb | `hearWave` | 0.1255 |
| 04 | ui | `playLayer` | 0.1586 |
| 04 | ui | `hearWave` | 0.1285 |
| 04 | alarm | `playLayer` | 0.2210 |
| 04 | alarm | `hearWave` | 0.1286 |

Las 190 comprobaciones de extremos de deslizadores y las diferencias numéricas por parámetro figuran en `pruebas/resultados_base_rc1/chrome.json` y `pruebas/resultados_base_rc1/webkit/webkit.json`. La navegación por botones de paso, flechas, entradas y regresos figura en `compatibilidad.json`. La escucha crítica humana sigue pendiente.
