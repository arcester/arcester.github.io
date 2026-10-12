"""Genera las páginas de Connecter (inglés en /connecter/, español en /connecter/es/)
a partir de template.html e i18n.json.

Uso, desde la raíz del repositorio:  python3 tools/connecter/build.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent

template = (HERE / 'template.html').read_text(encoding='utf-8')
strings = json.loads((HERE / 'i18n.json').read_text(encoding='utf-8'))

for lang, s in strings.items():
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
