# arcester.github.io

Webs de mis proyectos, publicadas con GitHub Pages.

- `/` → redirige a [arcesaez.com](https://arcesaez.com)
- [`/connecter/`](https://arcester.github.io/connecter/) → Connecter, gestor de carpetas compartidas SMB para macOS (inglés)
- [`/connecter/es/`](https://arcester.github.io/connecter/es/) → Connecter en español
- `/connecter/en/` → redirige a `/connecter/` (estuvo publicada como versión inglesa)
- [`/paella/`](https://arcester.github.io/paella/) → Paella, termostato de barra de menús para MacBook Air sin ventilador (inglés)
- [`/paella/es/`](https://arcester.github.io/paella/es/) → Paella en español

## Cómo editar la web de Connecter

Las dos páginas (`connecter/index.html` y `connecter/es/index.html`) se generan; no se editan a mano.

- `tools/connecter/template.html`: estructura, estilos y animaciones.
- `tools/connecter/i18n.json`: todos los textos, en inglés y en español.
- `tools/connecter/wallpaper.py`: genera `connecter/img/wall.webp`, el fondo abstracto de la portada.

Tras cualquier cambio: `python3 tools/connecter/build.py`

## Cómo editar la web de Paella

Igual que Connecter: `paella/index.html` y `paella/es/index.html` se generan.

- `tools/paella/template.html`: estructura, estilos y animaciones (menú simulado y curva de temperatura).
- `tools/paella/i18n.json`: todos los textos, en inglés y en español.
- `tools/paella/wallpaper.py`: genera `paella/img/wall.webp`, el fondo en tonos azafrán.

Tras cualquier cambio: `python3 tools/paella/build.py`

## Visitas y estrellas

Las dos webs muestran en el pie un contador de visitas (una por sesión del navegador, sin cookies)
y en Soporte un botón para dar una estrella al repositorio con el número actual.

- Contador: [Abacus](https://abacus.jasoncameron.dev), espacio `arcester.github.io`, claves `connecter` y `paella`
  (inglés y español suman juntos). Consultar sin sumar: `https://abacus.jasoncameron.dev/get/arcester.github.io/connecter`
- Estrellas: API pública de GitHub.
- Repositorio y clave están en `GH_REPO` y `COUNTER_KEY` de cada `build.py`. Si un servicio falla, su dato no aparece.
