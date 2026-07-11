#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "docs/demos/artifacts"
OUT = ROOT / "docs/demos/screenshots/pptx-pdf-package.png"
SLIDE = ART / "hermes-built-research-deck-slide-01.png"
PPTX = ART / "hermes-built-research-deck.pptx"
PDF = ART / "hermes-built-research-deck.pdf"

W, H = 1600, 1000
bg = Image.new("RGB", (W, H), "#07101d")
d = ImageDraw.Draw(bg)

font_dir = Path("/usr/share/fonts/truetype/dejavu")
def font(name, size):
    return ImageFont.truetype(str(font_dir / name), size)

bold = lambda n: font("DejaVuSans-Bold.ttf", n)
regular = lambda n: font("DejaVuSans.ttf", n)

# Header
d.text((46, 34), "Research deck delivery", font=bold(31), fill="#eef5ff")
d.text((46, 77), "Native PowerPoint and rendered PDF, checked against the same opening slide", font=regular(16), fill="#9fb3d1")
d.rounded_rectangle((1310, 36, 1548, 82), radius=22, fill="#123354", outline="#3f72a3", width=2)
d.text((1354, 49), "24 SLIDES · QA COMPLETE", font=bold(12), fill="#bfe1ff")

# Slide preview panel
panel = (42, 120, 1166, 930)
d.rounded_rectangle(panel, radius=18, fill="#101d32", outline="#2e496c", width=2)
d.text((66, 143), "Opening checkpoint slide", font=bold(15), fill="#dce8fa")
slide = Image.open(SLIDE).convert("RGB")
max_w, max_h = 1068, 704
ratio = min(max_w / slide.width, max_h / slide.height)
slide = slide.resize((int(slide.width * ratio), int(slide.height * ratio)), Image.Resampling.LANCZOS)
x = panel[0] + (panel[2] - panel[0] - slide.width) // 2
y = 190 + (690 - slide.height) // 2
bg.paste(slide, (x, y))
d = ImageDraw.Draw(bg)
d.rounded_rectangle((x-2, y-2, x+slide.width+2, y+slide.height+2), radius=8, outline="#6e86a4", width=2)
d.text((66, 889), "Rendered from the delivered PDF; the PowerPoint remains editable.", font=regular(13), fill="#9fb3d1")

# Delivery cards
def size_mb(path):
    return f"{path.stat().st_size / (1024*1024):.1f} MB"

def card(y0, ext, title, subtitle, size, accent, lines):
    x0, x1, y1 = 1200, 1558, y0 + 246
    d.rounded_rectangle((x0, y0, x1, y1), radius=17, fill="#101d32", outline=accent, width=2)
    d.rounded_rectangle((x0+22, y0+22, x0+90, y0+90), radius=12, fill=accent)
    tw = d.textbbox((0,0), ext, font=bold(13))[2]
    d.text((x0+56-tw/2, y0+48), ext, font=bold(13), fill="#ffffff", anchor="mm")
    d.text((x0+110, y0+25), title, font=bold(17), fill="#eef5ff")
    d.text((x0+110, y0+52), subtitle, font=regular(12), fill="#9fb3d1")
    d.rounded_rectangle((x0+110, y0+76, x0+190, y0+104), radius=14, fill="#0b1424", outline="#2e496c")
    d.text((x0+126, y0+84), size, font=bold(11), fill="#cbd9ec")
    yy = y0 + 126
    for text in lines:
        d.ellipse((x0+24, yy+4, x0+32, yy+12), fill="#82e6c5")
        d.text((x0+43, yy), text, font=regular(12), fill="#cbd9ec")
        yy += 30

card(147, "PPTX", "Editable PowerPoint", "Native presentation file", size_mb(PPTX), "#2f6fa6", ["Editable text and tables", "Slide geometry retained", "Ready for further revision"])
card(422, "PDF", "Rendered PDF", "Presentation-ready export", size_mb(PDF), "#b24d57", ["Same 24-slide sequence", "Font and layout check", "Portable review copy"])

# QA block
d.rounded_rectangle((1200, 697, 1558, 930), radius=17, fill="#0d1728", outline="#2a4268", width=2)
d.text((1224, 719), "Delivery checks", font=bold(16), fill="#eef5ff")
checks = ["PPTX opened successfully", "PDF rendered from PowerPoint", "Opening slide matches", "Contact-sheet review complete"]
yy = 759
for text in checks:
    d.rounded_rectangle((1224, yy, 1244, yy+20), radius=10, fill="#173d31")
    d.text((1229, yy+1), "✓", font=bold(13), fill="#82e6c5")
    d.text((1256, yy+1), text, font=regular(12), fill="#cbd9ec")
    yy += 38

OUT.parent.mkdir(parents=True, exist_ok=True)
bg.save(OUT, quality=95)
print(OUT)
