# Handoff de Sesión

- **Fecha/Hora**: 2026-11-12T12:12:00+01:00
- **Workspace**: /Users/guzman/Desarrollo/arcester.github.io
- **Objetivo en curso**: Lanzamiento de Connecter: web oficial actualizada, badge de Product Hunt colocado y lanzamiento programado en Product Hunt.
- **Estado actual**: Todo completado. La web está actualizada y subida a GitHub (`main` en commit `364d4e0`). El lanzamiento en Product Hunt está programado (ID: `1313965`) para el 18 de noviembre de 2026.

## Ficheros modificados / creados
- `/Users/guzman/Desarrollo/arcester.github.io/connecter/index.html`: Enlace Mac App Store y badge de Product Hunt recolocado al final del bloque CTA.
- `/Users/guzman/Desarrollo/arcester.github.io/connecter/es/index.html`: Versión en español con el badge recolocado al bloque CTA final.
- `/Users/guzman/Desarrollo/arcester.github.io/tools/connecter/template.html`: Plantilla actualizada con la posición final del badge en el bloque CTA.
- `/Users/guzman/Desarrollo/arcester.github.io/tools/connecter/build.py`: Constante `APP_STORE` añadida para inyección automática.
- `/Users/guzman/Desarrollo/arcester.github.io/tools/connecter/i18n.json`: Textos de "próximamente" reemplazados por "ya disponible".
- `~/.gemini/config/mcp_config.json`: Servidor MCP de Product Hunt configurado y operativo.

## Decisiones clave
- El badge de Product Hunt se movió al bloque CTA final (debajo del botón de descarga blanco) para mantener la cabecera limpia y acorde a la paleta de colores.
- El enlace de la App Store se dejó internacional (`/app/id6829888591`).
- En Product Hunt se programó para el miércoles 18 de noviembre de 2026 a las 00:01 PST, con precio gratuito, 3 capturas añadidas y rol de Maker asignado a `@guzman_arce`.
- La animación de la hoja «Nuevo recurso» (volumen «fotos») está desplegada en las páginas HTML generadas, pero sigue pendiente de consolidarse en `template.html`.

## Próximos 2 pasos
1. Pasar la animación de la hoja «Nuevo recurso» (volumen «fotos») de `connecter/index.html` y `connecter/es/index.html` a `tools/connecter/template.html` para que futuros `python3 tools/connecter/build.py` no la sobrescriban.
2. (Opcional) Publicar el hilo en el foro de Product Hunt o preparar el primer comentario del Maker antes del 18 de noviembre.
