#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "docs/demos/artifacts"
OUT = ROOT / "docs/demos/screenshots/pptx-pdf-package.png"
PAGE = ART / "value-mechanism-evidence-hero.png"

W, H = 1600, 1000
canvas = Image.new("RGB", (W, H), "#cfd1d2")
d = ImageDraw.Draw(canvas)
font_dir = Path("/usr/share/fonts/truetype/dejavu")

def regular(size): return ImageFont.truetype(str(font_dir / "DejaVuSans.ttf"), size)
def bold(size): return ImageFont.truetype(str(font_dir / "DejaVuSans-Bold.ttf"), size)

# Native-looking PDF viewer toolbar; no promotional panels.
d.rectangle((0, 0, W, 64), fill="#323639")
for x, color in [(24,"#ff5f57"),(48,"#febc2e"),(72,"#28c840")]:
    d.ellipse((x-7,25-7,x+7,25+7), fill=color)
d.text((108, 20), "value-mechanism-evidence-deck.pdf", font=regular(14), fill="#f2f2f2")
# center page control
d.rounded_rectangle((726, 15, 874, 49), radius=7, fill="#242729", outline="#595d60")
d.text((756, 23), "2  /  4", font=bold(13), fill="#f2f2f2")
# right-side standard viewer controls only
d.text((1283, 20), "−", font=bold(18), fill="#f0f0f0")
d.text((1320, 21), "100%", font=regular(13), fill="#f0f0f0")
d.text((1385, 19), "+", font=bold(18), fill="#f0f0f0")
d.line((1433,16,1433,48), fill="#65696c", width=1)
d.text((1460, 18), "↓", font=bold(19), fill="#f0f0f0")
d.text((1510, 17), "⎙", font=regular(19), fill="#f0f0f0")

page = Image.open(PAGE).convert("RGB")
max_w, max_h = 1330, 820
scale = min(max_w/page.width, max_h/page.height)
page = page.resize((int(page.width*scale), int(page.height*scale)), Image.Resampling.LANCZOS)
px = (W-page.width)//2
py = 64 + (H-64-page.height)//2
# restrained document shadow
shadow = Image.new("RGBA", (W,H), (0,0,0,0))
sd = ImageDraw.Draw(shadow)
sd.rectangle((px+7,py+10,px+page.width+12,py+page.height+15), fill=(0,0,0,95))
shadow = shadow.filter(ImageFilter.GaussianBlur(14))
canvas = Image.alpha_composite(canvas.convert("RGBA"), shadow)
canvas.paste(page, (px,py))
# hairline page boundary
d = ImageDraw.Draw(canvas)
d.rectangle((px-1,py-1,px+page.width,py+page.height), outline="#9fa2a4", width=1)
canvas.convert("RGB").save(OUT, quality=95)
print(OUT)
