"""Genera el fondo de escritorio abstracto de la portada (no se usa ningún fondo de Apple)."""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np, math, sys

W, H = 1920, 1200
out = sys.argv[1] if len(sys.argv) > 1 else 'wall.webp'

# base: degradado vertical azul noche → azul intenso
y = np.linspace(0, 1, H)[:, None]
top, bottom = np.array([10, 22, 64]), np.array([18, 92, 210])
base = (top * (1 - y) + bottom * y)[:, None, :].repeat(W, axis=1)
img = Image.fromarray(base.astype(np.uint8).reshape(H, W, 3), 'RGB')

# manchas de luz grandes y muy difuminadas
glow = Image.new('RGB', (W, H), (0, 0, 0))
d = ImageDraw.Draw(glow)
for cx, cy, r, col in [(1500, 260, 520, (60, 190, 255)), (380, 980, 620, (120, 70, 255)),
                       (1050, 760, 480, (0, 140, 255)), (200, 160, 380, (40, 90, 220))]:
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col)
glow = glow.filter(ImageFilter.GaussianBlur(220))
img = Image.blend(img, glow, 0.55)

# ondas tipo cristal, en capas
waves = Image.new('RGBA', (W, H), (0, 0, 0, 0))
dw = ImageDraw.Draw(waves)
for k, (amp, off, col) in enumerate([(120, 640, (140, 220, 255, 90)), (90, 760, (80, 160, 255, 110)),
                                     (150, 880, (40, 110, 240, 120)), (110, 1010, (20, 70, 200, 140))]):
    pts = [(x, off + amp * math.sin(x / W * 2.2 * math.pi + k * 0.9) + 40 * math.sin(x / W * 7 * math.pi + k))
           for x in range(0, W + 20, 20)]
    dw.polygon(pts + [(W, H), (0, H)], fill=col)
waves = waves.filter(ImageFilter.GaussianBlur(34))
img = img.convert('RGBA'); img.alpha_composite(waves)
img = img.convert('RGB').filter(ImageFilter.GaussianBlur(6))
img.save(out, quality=82, method=6)
