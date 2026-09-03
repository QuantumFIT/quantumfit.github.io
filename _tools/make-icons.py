#!/usr/bin/env python3
"""Rasterise favicon.svg into the icon files the site links.

Run from anywhere:

    python3 _tools/make-icons.py

favicon.svg is the source and is edited by hand; this derives only the raster
formats browsers still ask for, so the two cannot drift apart. Re-run it after
editing the SVG and commit the results: GitHub Pages runs Jekyll and nothing
else, so nothing regenerates these on deploy.

Needs rsvg-convert (Debian: librsvg2-bin) and Pillow (python3-pil).

This directory starts with an underscore, so Jekyll leaves it out of the built
site without needing an `exclude:` entry.
"""

import os
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

# Sizes packed into /favicon.ico, which every browser requests unprompted even
# though the SVG supersedes it where supported.
ICO_SIZES = (16, 32, 48)

# Standalone PNGs, keyed by pixel size. 180 is the one apple-touch-icon size
# that covers every current iOS device.
PNG_TARGETS = {
    32: "favicon.png",
    180: os.path.join("images", "apple-touch-icon.png"),
}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG = os.path.join(ROOT, "favicon.svg")


def render(size, out):
    subprocess.run(
        ["rsvg-convert", "-w", str(size), "-h", str(size), SVG, "-o", out],
        check=True,
    )


def main():
    if shutil.which("rsvg-convert") is None:
        sys.exit("rsvg-convert not found; install librsvg2-bin")
    if not os.path.exists(SVG):
        sys.exit(f"missing source: {SVG}")

    for size, rel in sorted(PNG_TARGETS.items()):
        path = os.path.join(ROOT, rel)
        render(size, path)
        # librsvg writes at the zlib default; re-encoding at maximum takes
        # roughly a tenth off files that are committed and served on every
        # page load.
        Image.open(path).convert("RGBA").save(path, format="PNG", optimize=True)
        print(f"{rel}  {os.path.getsize(path):,} bytes")

    # Each ICO entry is rendered at its own size rather than letting Pillow
    # downscale one image: at 16px the difference between librsvg drawing the
    # ring and a resampled 48px ring is the difference between a legible Q and
    # a grey smudge.
    with tempfile.TemporaryDirectory() as tmp:
        frames = []
        for size in ICO_SIZES:
            path = os.path.join(tmp, f"{size}.png")
            render(size, path)
            frames.append(Image.open(path).convert("RGBA"))
        frames.sort(key=lambda im: im.width, reverse=True)

        ico = os.path.join(ROOT, "favicon.ico")
        frames[0].save(
            ico,
            format="ICO",
            append_images=frames[1:],
            sizes=[(im.width, im.height) for im in frames],
        )
    print(f"favicon.ico  {os.path.getsize(ico):,} bytes")


if __name__ == "__main__":
    main()
