# Audio Pedagógico

**Laboratorio Interactivo de Diseño Sonoro · v0.5.0-rc2**

Aplicación educativa gratuita para estudiantes universitarios de Ingeniería Multimedia y Diseño Sonoro. Aprende a fabricar efectos audiovisuales mediante síntesis, escucha crítica y experimentación.

## Abrir la aplicación

**[Entrar a Audio Pedagógico](https://manueljcamargop.github.io/synth-fx/)**

No necesitas cuenta ni instalación. Pulsa un botón de escucha para activar el audio del navegador y comienza con volumen moderado.

## Síntesis de efectos sonoros

1. Disparos láser: formas de onda, barridos y envolventes.
2. Naves espaciales: filtros, ruido, modulación y movimiento estéreo.
3. Espadas de energía: eventos, capas y transitorios.
4. Ambientes tecnológicos: maquinaria, interfaz y alarma.

Observa → escucha → experimenta → fabrica → sincroniza → reflexiona.

Los parámetros se ajustan con perillas: arrastra hacia arriba/abajo, toca el aro o usa las flechas del teclado. Mayús + arrastre permite ajuste fino. Puedes escuchar las ondas, comparar diseños y exportar tus efectos en WAV para un DAW.

## Reverberación

- [Observa](Reverberacion_Interactiva_3_Paginas.html#observa) para comparar el sonido directo y las reflexiones de una sala.
- [Experimenta](Reverberacion_Interactiva_3_Paginas.html#experimenta) con el tiempo de reverberación, el retardo, la mezcla y la absorción.
- [Aplica](Reverberacion_Interactiva_3_Paginas.html#aplica) los ajustes a una situación y exporta el resultado en WAV.
- [Entrena tu oído](Entrenador_Reverberacion.html) en cuatro niveles: compara la duración de dos colas (con dificultad adaptativa), reconoce el tamaño y el pre-delay de un espacio, iguala una referencia sin ver sus valores y corrige una sugerencia automática (preset) según el encargo de un cliente. El progreso se guarda solo en el navegador y puede descargarse como registro en TXT.
- [Sala virtual](Sala_Virtual.html): diseña una sala (alto, ancho, profundidad y material), mira en planta cómo rebota la onda en las paredes o la sala en 3D, y escúchala. Usa el motor de MJ Reverb ([mjreverb-core.js](mjreverb-core.js)), el mismo del plugin VST3, con las mismas perillas y rangos: la señal coincide muestra a muestra con la versión en C++.

El procesamiento se realiza en el navegador. El módulo permite usar los sonidos incluidos o cargar un archivo de audio local.

## Audio 3D

Requiere audífonos.

- [Observa](Audio3D_Interactivo_3_Paginas.html#observa): compara el estéreo normal con el audio 3D y haz la prueba a ciegas para descubrir de dónde viene un sonido.
- [Experimenta](Audio3D_Interactivo_3_Paginas.html#experimenta): arrastra la fuente alrededor de la cabeza y observa la diferencia de tiempo (ITD), la de nivel (ILD) y la respuesta de cada oído. Compara HRTF medida, cabeza esférica sin orejas, estéreo normal y original.
- [Aplica](Audio3D_Interactivo_3_Paginas.html#aplica): diseña un recorrido (nave, mosca, pasos), compáralo con el estéreo y expórtalo como WAV binaural.

El motor binaural (`audio3d-motor.js`) es el mismo del plugin MJ Binaural 3D, portado a JavaScript, y corre en un AudioWorklet (con respaldo para navegadores antiguos). Las HRTF son del maniquí KEMAR del MIT (Gardner y Martin, 1994), de uso libre citando a los autores. El modelo esférico es el de Brown y Duda (1998). Al ser HRTF de un maniquí, es normal que a veces se confundan delante y detrás.

## Usar sin internet

Descarga **Code → Download ZIP**, extrae la carpeta completa y abre `index.html`. Conserva juntos el HTML de Reverberación, el HTML de Audio 3D con `audio3d-motor.js`, los cuatro HTML de misión, `synthfx.js`, `knobs.js`, `synthfx.css` y los cuatro MP4.

No hay dependencias externas, CDN, registro, backend ni envío de los diseños sonoros a servidores. La síntesis se ejecuta en el navegador. La visita a la web publicada no garantiza una copia offline: para ello descarga el ZIP.

## Estado de la versión

La versión de referencia de las cuatro misiones es `v0.5.0-rc2`. Sus pruebas automatizadas se realizaron en Chrome y WebKit en macOS. La simulación de tamaño/tacto móvil no equivale a pruebas en un teléfono físico. Sigue pendiente la escucha crítica humana y la comprobación en Android, iPhone, Windows y Safari instalado.

Consulta [la revisión de perillas](AUDITORIA_SYNTH_FX.md), [la auditoría de base](AUDITORIA_BASE_RC1.md) y [los controles verificados](CONTROLES_VERIFICADOS.md). Los informes históricos describen el estado anterior a esta publicación. Se incluyen scripts y resultados JSON; capturas y WAV de prueba se conservan en la entrega local, fuera del repositorio para estudiantes.

Estos sonidos son diseños creativos de ciencia ficción, no reproducciones físicas exactas de objetos reales. La aplicación se centra en efectos sonoros para imagen.
