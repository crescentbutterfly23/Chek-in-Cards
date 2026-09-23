#!/usr/bin/env python3
"""Inline fonts, logos and the QR library into one self-contained HTML file.

Run after editing src/template.html:  python3 src/build.py
Output: ../index.html, the page GitHub Pages serves (it also works offline; just double-click it).
"""
import base64
import re
from pathlib import Path

SRC = Path(__file__).resolve().parent
ASSETS = SRC / "assets"
OUT = SRC.parent / "index.html"

TEXT_INLINE = {"qrcode.js"}  # pasted as-is; everything else is base64


def fill(match):
    name = match.group(1)
    data = (ASSETS / name).read_bytes()
    if name in TEXT_INLINE:
        return data.decode("utf-8").replace("</script", "<\\/script")
    return base64.b64encode(data).decode("ascii")


html = re.sub(r"\{\{([\w.\-]+)\}\}", fill, (SRC / "template.html").read_text("utf-8"))
OUT.write_text(html, "utf-8")
print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")
