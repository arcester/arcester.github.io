# arcester.github.io

Webs de mis proyectos, publicadas con GitHub Pages.

- `/` → redirige a [arcesaez.com](https://arcesaez.com)
- [`/connecter/`](https://arcester.github.io/connecter/) → Connecter, gestor de carpetas compartidas SMB para macOS (inglés)
- [`/connecter/es/`](https://arcester.github.io/connecter/es/) → Connecter en español
- `/connecter/en/` → redirige a `/connecter/` (estuvo publicada como versión inglesa)

## Cómo editar la web de Connecter

Las dos páginas (`connecter/index.html` y `connecter/es/index.html`) se generan; no se editan a mano.

- `tools/connecter/template.html`: estructura, estilos y animaciones.
- `tools/connecter/i18n.json`: todos los textos, en inglés y en español.
- `tools/connecter/wallpaper.py`: genera `connecter/img/wall.webp`, el fondo abstracto de la portada.

Tras cualquier cambio: `python3 tools/connecter/build.py`
