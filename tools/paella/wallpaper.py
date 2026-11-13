"""Genera el fondo abstracto de la portada de Paella: azafrán, naranja y un toque de pimentón.

Uso, desde la raíz del repositorio:  python3 tools/paella/wallpaper.py paella/img/wall.webp
"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np, math, sys

W, H = 1920, 1200
out = sys.argv[1] if len(sys.argv) > 1 else 'wall.webp'

# base: degradado vertical de tierra tostada (socarrat) a naranja intenso
y = np.linspace(0, 1, H)[:, None]
top, bottom = np.array([74, 26, 6]), np.array([214, 104, 12])
base = (top * (1 - y) + bottom * y)[:, None, :].repeat(W, axis=1)
img = Image.fromarray(base.astype(np.uint8).reshape(H, W, 3), 'RGB')

# manchas de luz grandes y muy difuminadas: azafrán, ámbar y pimentón
glow = Image.new('RGB', (W, H), (0, 0, 0))
d = ImageDraw.Draw(glow)
for cx, cy, r, col in [(1500, 260, 520, (255, 196, 40)), (380, 980, 620, (220, 50, 30)),
                       (1050, 760, 480, (255, 150, 0)), (200, 160, 380, (180, 70, 10))]:
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col)
glow = glow.filter(ImageFilter.GaussianBlur(220))
img = Image.blend(img, glow, 0.55)

# ondas en capas, como el calor que sube
waves = Image.new('RGBA', (W, H), (0, 0, 0, 0))
dw = ImageDraw.Draw(waves)
for k, (amp, off, col) in enumerate([(120, 640, (255, 222, 120, 90)), (90, 760, (255, 176, 40, 110)),
                                     (150, 880, (240, 120, 20, 120)), (110, 1010, (190, 60, 15, 140))]):
    pts = [(x, off + amp * math.sin(x / W * 2.2 * math.pi + k * 0.9) + 40 * math.sin(x / W * 7 * math.pi + k))
           for x in range(0, W + 20, 20)]
    dw.polygon(pts + [(W, H), (0, H)], fill=col)
waves = waves.filter(ImageFilter.GaussianBlur(34))
img = img.convert('RGBA'); img.alpha_composite(waves)
img = img.convert('RGB').filter(ImageFilter.GaussianBlur(6))
img.save(out, quality=82, method=6)
