"""把 template.html 的圖片佔位符換成 base64，產出單一 HTML。"""
import base64, io, json, glob, os
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
DL = os.path.join(ROOT, "assets_dl")
GEN = os.path.join(ROOT, "slides", "generated")


def jpeg_uri(path, width):
    img = Image.open(path).convert("RGB")
    w, h = img.size
    if w > width:
        img = img.resize((width, int(h * width / w)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=80, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def svg_uri(path):
    with open(path, "rb") as f:
        return "data:image/svg+xml;base64," + base64.b64encode(f.read()).decode()


flags = {c: svg_uri(os.path.join(DL, f"{c}.svg"))
         for c in ["tw", "jp", "in", "gb", "fr", "us", "br", "eg", "au"]}
cover = sorted(glob.glob(os.path.join(GEN, "cover_*.png")))[-1]
ending = sorted(glob.glob(os.path.join(GEN, "ending_*.png")))[-1]

with open(os.path.join(ROOT, "template.html"), encoding="utf-8") as f:
    html = f.read()
html = (html.replace("__FLAGS__", json.dumps(flags))
            .replace("__MAP__", jpeg_uri(os.path.join(DL, "worldmap.jpg"), 1280))
            .replace("__COVER__", jpeg_uri(cover, 1400))
            .replace("__ENDING__", jpeg_uri(ending, 1400)))
out = os.path.join(ROOT, "index.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print(out, round(os.path.getsize(out) / 1024), "KB")
