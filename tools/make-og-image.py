"""
Generates assets/og-image.png (1200x630) - the preview card LinkedIn shows
when the portfolio URL is shared.

Run from the project root:      python tools/make-og-image.py

If assets/profile.jpg exists it is composited in as a circular headshot;
otherwise a clean typographic card is produced. Re-run any time you change
the photo or the text constants below.

Requires: pip install pillow
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# ── Content ──────────────────────────────────────────────────────────────
EYEBROW = "DIGITAL TRANSFORMATION  ·  ENTERPRISE SYSTEMS"
NAME = "Manoj Rajan"
TITLE_1 = "Digital Transformation Manager"
TITLE_2 = "Enterprise Solutions Lead"
METRICS = ["20+ YEARS", "USD 2.5M+ DELIVERED", "70+ VESSELS"]
FOOTER = "PMP®  ·  CBAP®  ·  ITIL®        Dubai, United Arab Emirates"

# ── Look ─────────────────────────────────────────────────────────────────
W, H = 1200, 630
BG_TOP, BG_BOTTOM = (15, 23, 42), (30, 41, 59)     # slate-900 → slate-800
ACCENT = (217, 119, 6)                              # amber-600, bronze
ACCENT_SOFT = (251, 191, 36)                        # amber-400
WHITE = (255, 255, 255)
MUTED = (148, 163, 184)                             # slate-400

ROOT = Path(__file__).resolve().parent.parent
PHOTO = ROOT / "assets" / "profile.jpg"
OUT = ROOT / "assets" / "og-image.png"

FONT_DIR = Path("C:/Windows/Fonts")
FALLBACKS = {
    "bold": ["segoeuib.ttf", "arialbd.ttf", "DejaVuSans-Bold.ttf"],
    "semibold": ["seguisb.ttf", "segoeuib.ttf", "arialbd.ttf", "DejaVuSans-Bold.ttf"],
    "regular": ["segoeui.ttf", "arial.ttf", "DejaVuSans.ttf"],
}


def font(weight: str, size: int):
    for name in FALLBACKS[weight]:
        path = FONT_DIR / name
        if path.exists():
            return ImageFont.truetype(str(path), size)
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def tracked(draw, xy, text, fnt, fill, tracking=0):
    """Draw text with manual letter-spacing and return the width used."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking
    return x - xy[0]


def circular(img: Image.Image, size: int) -> Image.Image:
    """Centre-crop to a square, resize, and mask to a circle."""
    w, h = img.size
    side = min(w, h)
    img = img.crop(((w - side) // 2, (h - side) // 2,
                    (w - side) // 2 + side, (h - side) // 2 + side))
    img = img.resize((size, size), Image.LANCZOS).convert("RGB")

    mask = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size * 4, size * 4), fill=255)
    mask = mask.resize((size, size), Image.LANCZOS)

    out = Image.new("RGBA", (size, size))
    out.paste(img, (0, 0), mask)
    return out


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)

    # Vertical gradient background
    card = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(card)
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=tuple(
            int(BG_TOP[i] + (BG_BOTTOM[i] - BG_TOP[i]) * t) for i in range(3)))

    # Soft accent glow, bottom right
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((W - 600, H - 500, W + 200, H + 280),
                                 fill=ACCENT + (60,))
    glow = glow.filter(ImageFilter.GaussianBlur(110))
    card = Image.alpha_composite(card.convert("RGBA"), glow)
    d = ImageDraw.Draw(card)

    # Left accent rule
    d.rectangle((0, 0, 9, H), fill=ACCENT)

    has_photo = PHOTO.exists()
    text_right = 760 if has_photo else 1120
    x = 84

    tracked(d, (x, 92), EYEBROW, font("semibold", 21), ACCENT_SOFT, tracking=1.7)

    # Name - shrink to fit if it ever gets longer
    size = 82
    f_name = font("bold", size)
    while d.textlength(NAME, font=f_name) > (text_right - x) and size > 48:
        size -= 2
        f_name = font("bold", size)
    d.text((x, 138), NAME, font=f_name, fill=WHITE)

    d.text((x, 248), TITLE_1, font=font("semibold", 37), fill=(226, 232, 240))
    d.text((x, 296), TITLE_2, font=font("semibold", 37), fill=(226, 232, 240))

    d.rectangle((x, 372, x + 78, 376), fill=ACCENT)

    # Metric pills
    px, f_metric = x, font("semibold", 20)
    for m in METRICS:
        w = d.textlength(m, font=f_metric) + 34
        if px + w > text_right:
            break
        d.rounded_rectangle((px, 412, px + w, 462), radius=25,
                            outline=(71, 85, 105), width=2)
        d.text((px + 17, 425), m, font=f_metric, fill=(226, 232, 240))
        px += w + 12

    tracked(d, (x, 536), FOOTER, font("regular", 21), MUTED, tracking=0.6)

    if has_photo:
        size_px = 300
        cx, cy = 950, 300
        ring = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(ring).ellipse(
            (cx - size_px // 2 - 7, cy - size_px // 2 - 7,
             cx + size_px // 2 + 7, cy + size_px // 2 + 7), fill=ACCENT + (235,))
        card = Image.alpha_composite(card, ring)
        avatar = circular(Image.open(PHOTO), size_px)
        card.paste(avatar, (cx - size_px // 2, cy - size_px // 2), avatar)

    card.convert("RGB").save(OUT, "PNG", optimize=True)
    print(f"Wrote {OUT}  ({OUT.stat().st_size / 1024:.0f} KB)"
          f"{'  [with photo]' if has_photo else '  [no photo - add assets/profile.jpg and re-run]'}")


if __name__ == "__main__":
    main()
