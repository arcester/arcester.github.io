"""Genera las páginas de Paella (inglés en /paella/, español en /paella/es/)
a partir de template.html e i18n.json.

Uso, desde la raíz del repositorio:  python3 tools/paella/build.py
"""
import json
import re
from pathlib import Path

# Dirección pública de la landing: canonical, hreflang y og:* salen de aquí.
SITE = 'https://arcester.github.io/paella/'

# Repositorio en GitHub (botón de estrella) y clave del contador de visitas en Abacus
# (abacus.jasoncameron.dev, espacio arcester.github.io). Cambiar la clave pone el contador a cero.
GH_REPO = 'arcester/paella'
COUNTER_KEY = 'paella'

HERE = Path(__file__).parent
REPO = HERE.parent.parent

template = (HERE / 'template.html').read_text(encoding='utf-8')
strings = json.loads((HERE / 'i18n.json').read_text(encoding='utf-8'))

for lang, s in strings.items():
    s = {**s, 'site': SITE, 'url': SITE + s['path'], 'gh_repo': GH_REPO, 'counter_key': COUNTER_KEY,
         'js_strings': json.dumps(s['js_strings'], ensure_ascii=False)}

    def sub(m):
        key = m.group(1)
        if key not in s:
            raise KeyError(f'{lang}: falta la clave «{key}»')
        return s[key]
    html = re.sub(r'\{\{(\w+)\}\}', sub, template)
    out = REPO / s['out']
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding='utf-8')
    print(f'{lang}: {out.relative_to(REPO)}')

missing = set(strings['en']) ^ set(strings['es'])
if missing:
    raise SystemExit(f'Claves que solo están en un idioma: {sorted(missing)}')
