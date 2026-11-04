# Synth FX v0.5.0-rc2 · Perillas giratorias

Cambio solicitado: sustituir la presentación de los deslizadores por perillas, conservando los valores, rangos y funciones originales.

## Cambios

- Todos los parámetros numéricos y controles de sincronización se presentan como perillas con aro de nivel e indicador giratorio.
- Arrastre vertical u horizontal con ratón o toque; selección directa tocando el aro y ajuste fino con Mayús + arrastre.
- Teclado: flechas para un paso, Inicio/Fin para los límites y RePág/AvPág para diez pasos.
- Accesibilidad: nombre, mínimo, máximo, valor numérico y valor con unidades disponibles mediante el rol ARIA slider, que es la semántica accesible correspondiente a una perilla.
- Los controles de rango originales se conservan internamente y reciben los mismos eventos input/change. El motor sonoro, las escalas y las exportaciones no se modificaron.
- La posición del indicador sigue los presets, la restauración de valores y la regeneración de controles al cambiar de evento o capa.
- Se conserva íntegra la versión v0.5.0-rc1 en su carpeta y ZIP anteriores.

## Verificación de esta revisión

`pruebas/perillas.py` registra en `pruebas/resultados/perillas.json` las pruebas de los controles de las cuatro misiones en Chrome y WebKit: límites y pasos con teclado, actualización del estado accesible, arrastre con ratón, toque, cambio de presets/eventos/capas, generación efectiva de PCM y presentación a 390 px sin desbordamiento horizontal. El arrastre táctil se emula adicionalmente en Chrome. Las capturas están en la misma carpeta de resultados.

Las pruebas automatizadas de toque y tamaño de pantalla no equivalen a dispositivos físicos. La escucha humana, Safari instalado, Android/iPhone y Windows siguen pendientes como se documentó en rc1.

La auditoría general y sus resultados anteriores se conservan en `AUDITORIA_BASE_RC1.md` y `pruebas/resultados_base_rc1/`; esa evidencia corresponde a rc1. Esta revisión requiere distribuir también `knobs.js`. No se ha publicado el proyecto.

Resultado final: ocho casos misión/motor completos sin errores JavaScript; 38 controles de perilla comprobados por teclado en cada motor, con límites, pasos, presets, ratón, toque y señal sonora verificados. Pruebas ejecutadas el 3 de noviembre de 2026.
