# Publicación futura de Synth FX

Esta entrega no crea repositorios ni publica archivos. Los pasos siguientes se ejecutarán cuando se autorice la publicación.

1. Crear o elegir un repositorio, por ejemplo `synth-fx`.
2. Copiar **el contenido** de esta carpeta a la raíz del repositorio: `index.html`, las cuatro misiones HTML, `synthfx.js`, `knobs.js`, `synthfx.css` y los cuatro MP4 deben conservar sus nombres y rutas relativas. No subir el respaldo v0.4.0. La carpeta `pruebas` contiene evidencia técnica y puede conservarse fuera del sitio público.
3. Conservar la documentación y el número de versión. Revisar permisos de distribución del material antes de hacerlo público.
4. En **Settings → Pages**, elegir **Deploy from a branch**, rama `main`, carpeta `/ (root)` y guardar. El archivo `.nojekyll` incluido permite servir directamente este sitio estático.
5. Cuando GitHub muestre la dirección, abrirla y recorrer las cuatro misiones, los cuatro MP4 y todas las exportaciones. En un sitio de proyecto, la URL será de la forma `https://USUARIO.github.io/synth-fx/`.
6. Comprobar en un Android y un iPhone físicos: activación del sonido mediante toque, reproducción repetida, descarga WAV, reproducción/seek de video y regreso desde segundo plano. Registrar navegador, sistema, modelo y resultado.
7. Etiquetar una versión estable únicamente después de esas pruebas; mantener `v0.5.0-rc2` hasta entonces.

No hay compilación, servidor de audio, npm, CDN, fuentes remotas ni claves de API. Para uso sin internet, descargar la carpeta completa y abrir `index.html`; haber visitado la versión publicada no garantiza que quede disponible offline. No se ha incorporado un service worker.

Para probar por HTTP en el equipo, desde esta carpeta ejecutar `python3 -m http.server 8000` y abrir `http://localhost:8000`. Si el servidor básico no permite buscar posiciones del video de forma correcta, usar un servidor con soporte de solicitudes HTTP Range; los MP4 también pueden abrirse directamente desde la carpeta local.

Referencia oficial consultada: [Crear un sitio de GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).
