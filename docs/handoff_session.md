# Handoff de Sesión

- **Fecha/Hora**: 2026-11-12T11:52:00+01:00
- **Workspace**: /Users/guzman/Desarrollo/arcester.github.io
- **Objetivo en curso**: Lanzamiento de Connecter: web oficial actualizada y lanzamiento programado en Product Hunt.
- **Estado actual**: Todo completado. La web está actualizada y subida a GitHub (`main` en commit `97be80f`). El lanzamiento en Product Hunt está programado (ID: `1313965`) para el 18 de noviembre de 2026.

## Ficheros modificados / creados
- `/Users/guzman/Desarrollo/arcester.github.io/connecter/index.html`: Enlaces de descarga actualizados a `https://apps.apple.com/app/id6829888591`.
- `/Users/guzman/Desarrollo/arcester.github.io/connecter/es/index.html`: Enlaces en español actualizados a la App Store.
- `/Users/guzman/Desarrollo/arcester.github.io/tools/connecter/build.py`: Constante `APP_STORE` añadida para inyección automática.
- `/Users/guzman/Desarrollo/arcester.github.io/tools/connecter/i18n.json`: Textos de "próximamente" reemplazados por "ya disponible".
- `/Users/guzman/Desarrollo/arcester.github.io/tools/connecter/template.html`: Botones primarios convertidos en enlaces `<a>`.
- `~/.gemini/config/mcp_config.json`: Servidor MCP de Product Hunt configurado y operativo.

## Decisiones clave
- El enlace de la App Store se dejó neutral/internacional (`/app/id6829888591`) para redirigir a la tienda local de cada usuario.
- En Product Hunt se programó para el miércoles 18 de noviembre de 2026 a las 00:01 PST, con precio gratuito, 3 capturas añadidas y rol de Maker asignado a `@guzman_arce`.
- La animación de la hoja «Nuevo recurso» (volumen «fotos») está desplegada en las páginas HTML generadas, pero sigue pendiente de consolidarse en `template.html`.

## Próximos 2 pasos
1. Pasar la animación de la hoja «Nuevo recurso» (volumen «fotos») de `connecter/index.html` y `connecter/es/index.html` a `tools/connecter/template.html` para que futuros `python3 tools/connecter/build.py` no la sobrescriban.
2. (Opcional) Redactar el comentario de bienvenida del Maker en Product Hunt para dejarlo programado antes del 18 de noviembre.
