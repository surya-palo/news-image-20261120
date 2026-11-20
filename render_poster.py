#!/usr/bin/env python3
"""Render the 20 November 2026 world-news poster (1024x1024 PNG).

Draws a newspaper-style front page with Pillow only: masthead, one lead
story (Cyclone Akvan) with a hand-drawn storm graphic, six story cards and
a sources footer. All text is rendered, never pasted as an image.
"""

import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 243, 230)
INK = (20, 20, 20)
GREY = (90, 86, 76)
RED = (166, 30, 30)
BLUE = (38, 84, 124)
LIGHT_BLUE = (214, 228, 238)
RULE = (60, 58, 50)
CARD_BG = (255, 252, 244)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(text, fnt, max_w, draw):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_para(draw, x, y, text, fnt, max_w, leading, color=INK):
    """Draw wrapped paragraph; returns y just below the last line."""
    for line in wrap(text, fnt, max_w, draw):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def rule(draw, x0, y, x1, width=2, color=RULE):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


def draw_storm(draw, x0, y0, x1, y1):
    """Hand-drawn cyclone: concentric spiral arms over a pale sky box."""
    draw.rectangle([x0, y0, x1, y1], fill=LIGHT_BLUE, outline=RULE, width=2)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2 - 2
    max_r = min(x1 - x0, y1 - y0) // 2 - 20
    # Spiral arms: three interleaved arcs winding into the eye.
    for arm in range(3):
        pts = []
        steps = 90
        for i in range(steps + 1):
            t = i / steps
            ang = arm * (2 * math.pi / 3) + t * 3.4 * math.pi
            r = max_r * (1.0 - t * 0.86)
            pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang) * 0.92))
        draw.line(pts, fill=BLUE, width=5)
    # Calm eye.
    draw.ellipse([cx - 13, cy - 13, cx + 13, cy + 13],
                 fill=PAPER, outline=BLUE, width=3)
    # Rain streaks along the bottom.
    for i in range(9):
        rx = x0 + 14 + i * 34
        draw.line([(rx, y1 - 26), (rx - 7, y1 - 8)], fill=BLUE, width=3)
    # Land strip and label.
    draw.rectangle([x0, y1 - 4, x1, y1], fill=(120, 110, 88))
    draw.text((x0 + 10, y0 + 8), "BAY OF BENGAL", font=font(SANS_B, 13),
              fill=BLUE)


def card(draw, x0, y0, w, h, kicker, headline, body):
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=CARD_BG,
                   outline=RULE, width=2)
    pad = 14
    y = y0 + pad
    draw.text((x0 + pad, y), kicker, font=font(SANS_B, 13), fill=RED)
    y += 22
    rule(draw, x0 + pad, y, x0 + w - pad, width=1, color=GREY)
    y += 10
    y = draw_para(draw, x0 + pad, y, headline, font(SERIF_B, 21),
                  w - 2 * pad, 26)
    y += 6
    draw_para(draw, x0 + pad, y, body, font(SANS, 14),
              w - 2 * pad, 19, color=(52, 50, 44))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36  # side margin

    # ---- Masthead ----
    y = 28
    d.text((W // 2, y), "THE WORLD IN ONE DAY", font=font(SERIF_B, 62),
           fill=INK, anchor="ma")
    y += 78
    rule(d, mx, y, W - mx, width=3)
    y += 8
    d.text((W // 2, y), "FRIDAY  20  NOVEMBER  2026", font=font(SANS_B, 24),
           fill=RED, anchor="ma")
    y += 36
    rule(d, mx, y, W - mx, width=3)
    rule(d, mx, y + 5, W - mx, width=1)

    # ---- Lead story ----
    y += 22
    lead_top = y
    d.text((mx, y), "LEAD  ·  INDIA — CYCLONE", font=font(SANS_B, 15),
           fill=RED)
    y += 26
    head = "Cyclone Akvan slams into Odisha"
    y = draw_para(d, mx, y, head, font(SERIF_B, 44), 600, 50)
    y += 6
    body = ("Cyclone Akvan crossed the Odisha coast near Gopalpur on Friday "
            "morning, its winds down to 70–80 km/h, gusting to 90. More than "
            "300,000 people were moved to safety, 423 rescue teams stood "
            "ready and 69 trains were cancelled. No major damage or loss of "
            "life had been reported by midday as heavy rain kept falling.")
    y = draw_para(d, mx, y, body, font(SANS, 17), 600, 23)
    lead_bottom = y + 8

    # Storm graphic, right of the lead text.
    gx0, gx1 = 668, W - mx
    draw_storm(d, gx0, lead_top + 2, gx1, lead_bottom - 4)
    d.text((gx0, lead_bottom + 2),
           "GOPALPUR · LANDFALL ~08:00 · 70–80 KM/H",
           font=font(SANS_B, 11), fill=GREY)

    y = lead_bottom + 26
    rule(d, mx, y, W - mx, width=2)
    y += 16

    # ---- Six story cards, 3 x 2 ----
    cards = [
        ("DIPLOMACY · SHENZHEN",
         "Three powers, one peace paper",
         "Trump, Xi and Putin issue a four-point “Declaration toward "
         "Peace” after their first trilateral meeting — UN reform, "
         "fuel, court immunity, nuclear-risk talks. No mention of "
         "Ukraine, Iran or North Korea."),
        ("JUSTICE · THE HAGUE",
         "World court: Myanmar committed genocide",
         "The ICJ rules 9–6 that Myanmar committed genocide against the "
         "Rohingya in 2017 — the first time the court has found a state "
         "guilty of the crime. Reparations and return are ordered."),
        ("ASIA · SEOUL",
         "Ex-PM’s 15-year term sent back",
         "South Korea’s Supreme Court overturns part of Han Duck-soo’s "
         "15-year sentence over the 2024 martial-law crisis and orders a "
         "retrial; other convictions stand and he stays in detention."),
        ("PACIFIC · SUVA",
         "Fiji declares a national disaster",
         "An El Niño drought forces a 30-day state of disaster; F$20 "
         "million is set aside for emergency water as below-normal rain "
         "is forecast until April."),
        ("INDIA · NEW DELHI",
         "Royals close India tour with Modi",
         "Prince William and Princess Kate meet PM Modi in New Delhi, "
         "capping a three-day visit built around the Earthshot Prize and "
         "India–UK ties."),
        ("TODAY · WORLD",
         "World Children’s Day",
         "UNICEF marks 20 November with the theme “My day. My rights. "
         "My future.” — 37 years since the Convention on the Rights of "
         "the Child was adopted."),
    ]
    gap = 14
    cw = (W - 2 * mx - 2 * gap) // 3
    ch = 230
    for i, (kick, head, body) in enumerate(cards):
        cx = mx + (i % 3) * (cw + gap)
        cy = y + (i // 3) * (ch + gap)
        card(d, cx, cy, cw, ch, kick, head, body)

    # ---- Footer ----
    fy = y + 2 * ch + gap + 14
    rule(d, mx, fy, W - mx, width=2)
    fy += 10
    foot = ("Sources: IMD / The Hindu BusinessLine · Reuters · ICJ · UNICEF — "
            "All events happened or were first reported on 20 November 2026.")
    d.text((W // 2, fy), foot, font=font(SANS, 13), fill=GREY, anchor="ma")
    fy += 20
    d.text((W // 2, fy), "make.fun · news-image-20261120",
           font=font(SANS_B, 13), fill=GREY, anchor="ma")

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
