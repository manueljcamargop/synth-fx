# Flujo multidispositivo de Synth FX

## Cambios y publicación

1. Parte de `main` actualizado y crea una rama `codex/<tarea>` para cada cambio.
2. Guarda y sube los commits de la rama a GitHub para retomarlos desde otro equipo. Abre un pull request en borrador hacia `main`.
3. Revisa los archivos cambiados y las pruebas. En una copia de la rama, ejecuta `python3 -m http.server 8000` desde la raíz y abre [localhost:8000](http://localhost:8000). Para una prueba funcional, comprueba activación de audio, reproducción de escenas y exportación WAV. En un teléfono físico, abre esa copia desde un servidor de pruebas accesible al teléfono o desde el computador en la misma red.
4. Manuel decide cuándo fusionar después de revisar. Comprueba el despliegue en Actions y abre [Synth FX publicado](https://manueljcamargop.github.io/synth-fx/) tras una fusión autorizada.

## Copia recuperable

La rama `respaldo/v0.5.0-rc2` conserva el commit publicado `5d43669750cecc302965f29f76906eac20446c08`. Consérvala como referencia y usa una rama nueva si necesitas trabajar a partir de ella. Para recuperar producción, prepara un pull request que revierta los cambios problemáticos y revísalo antes de fusionar. Evita reescribir el historial de `main`.

## Acceso

- **Mac y otros computadores.** Usa una copia del repositorio con acceso de escritura a GitHub. Para retomar trabajo, descarga los cambios de la rama correspondiente antes de editar.
- **Codex Cloud.** En ChatGPT web o escritorio, elige Work in → Cloud → Create environment. Conecta GitHub si se solicita y selecciona `manueljcamargop/synth-fx`. El sitio es estático y no requiere compilación ni secretos. Revisa el entorno, publícalo y prueba primero con una tarea de lectura. Desde el celular, selecciona el entorno publicado en Codex.
- **Celular.** Abre Pages para probar la versión publicada y GitHub para leer el pull request, sus cambios y sus verificaciones. Pages sirve la versión desplegada desde `main`.
- **Reverberación.** Esta copia contiene las cuatro misiones de Synth FX. Si los archivos de Reverberación siguen en el Mac, su acceso en la nube requiere identificar su ubicación y decidir dónde guardarlos.

## Protección de main

En GitHub, configura una regla activa en Settings → Rules → Rulesets para `main`. Exige pull request, bloquea el borrado y las actualizaciones forzadas y deja vacía la lista de excepciones. Para un flujo individual, cero aprobaciones obligatorias permite que Manuel revise y fusione manualmente sus propios pull requests. Una aprobación obligatoria requiere otro revisor autorizado.
