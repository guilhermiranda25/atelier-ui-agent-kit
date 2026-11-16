#!/usr/bin/env python
"""Offline WCAG relative-luminance contrast for opaque sRGB hex colors.

Usage: python check_contrast.py '#152624' '#ffffff'
Rejects alpha because it would require compositing against a known background.
"""
from __future__ import annotations
import argparse
import re

def luminance(color: str) -> float:
    if not re.fullmatch(r"#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})", color):
        raise ValueError("Expected #RGB or #RRGGBB without alpha")
    h = color[1:]
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    channels = [int(h[n : n + 2], 16) / 255 for n in (0, 2, 4)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in channels]
    return sum(c * w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))

def contrast(a: str, b: str) -> float:
    light, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (light + 0.05) / (dark + 0.05)

def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("foreground"); p.add_argument("background")
    args = p.parse_args()
    try: ratio = contrast(args.foreground, args.background)
    except ValueError as e: p.error(str(e))
    print(f"Contrast: {ratio:.2f}:1")
    print("AA normal text:", "PASS" if ratio >= 4.5 else "FAIL")
    print("AA large text / essential graphics:", "PASS" if ratio >= 3 else "FAIL")
    print("AAA normal text:", "PASS" if ratio >= 7 else "FAIL")

if __name__ == "__main__": main()
