#!/usr/bin/env python3
"""Subset the angle-bracket glyphs the site's own faces do not carry.

    python3 _tools/make-ket-font.py

Writes assets/fonts/qf-ket-400.woff2 and qf-ket-700.woff2, each holding just
U+27E8 and U+27E9. The outputs are committed, because GitHub Pages runs Jekyll
and nothing else.

Why they exist: the group's name is written |QuantumFIT> with a real closing
angle bracket, and Lato has no U+27E9 -- nor does the Latin subset the site
loads. A literal one is otherwise substituted from whatever font the reader
happens to have, and those fallbacks have no matching bold, which leaves the
bracket thin beside heavy text. Supplying the glyph at 400 and 700 makes it
bold with everything around it.

assets/css/fonts.css scopes both faces with unicode-range: U+27E8-27E9, so
they are consulted for nothing else and are not fetched by a page with no
bracket on it.

Source is DejaVu Sans, the one family on a plain Debian box carrying the glyph
in two weights. The family is renamed on the way out: a modified font must not
claim to be the original. Licence goes to assets/fonts/LICENSE-qf-ket.txt.

Needs python3-fonttools and python3-brotli.
"""

import os
import sys

from fontTools.subset import Options, Subsetter
from fontTools.ttLib import TTFont

SOURCES = {
    400: "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    700: "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
}

CODEPOINTS = [0x27E8, 0x27E9]  # the pair, though only U+27E9 is in use

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build(weight, src):
    if not os.path.exists(src):
        sys.exit(f"missing source font: {src} (install fonts-dejavu-core)")

    font = TTFont(src)
    covered = set()
    for table in font["cmap"].tables:
        covered |= set(table.cmap.keys())
    absent = [hex(c) for c in CODEPOINTS if c not in covered]
    if absent:
        sys.exit(f"{src} does not carry {absent}")

    opts = Options()
    opts.flavor = "woff2"
    opts.desubroutinize = True
    opts.drop_tables += ["DSIG"]
    # Names are kept deliberately: the licence asks for its notice to travel
    # with the font, and the name table is where it lives.
    opts.name_IDs = ["*"]
    opts.name_legacy = True
    opts.notdef_outline = True

    subsetter = Subsetter(options=opts)
    subsetter.populate(unicodes=CODEPOINTS)
    subsetter.subset(font)

    for rec in font["name"].names:
        if rec.nameID not in (1, 3, 4, 6, 16, 21):
            continue
        try:
            value = rec.toUnicode()
        except Exception:
            continue
        rec.string = value.replace("DejaVu Sans", "QF Ket").replace("DejaVuSans", "QFKet")

    out = os.path.join(ROOT, "assets", "fonts", f"qf-ket-{weight}.woff2")
    font.flavor = "woff2"
    font.save(out)
    print(f"{os.path.relpath(out, ROOT)}  {os.path.getsize(out):,} bytes")


if __name__ == "__main__":
    for weight, src in sorted(SOURCES.items()):
        build(weight, src)
