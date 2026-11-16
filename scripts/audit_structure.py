#!/usr/bin/env python
"""Advisory static UI risk scanner (not a browser audit or SAST). No dependencies."""
from __future__ import annotations
import argparse
from pathlib import Path
import re

RULES = (
    ("Clickable div", re.compile(r"<div\b[^>]*\bonClick\s*=", re.I), "Prefer semantic button/link"),
    ("Auto-focus", re.compile(r"\bautoFocus\s*(?:=|\b)", re.I), "Check intentional focus behavior"),
    ("dangerouslySetInnerHTML", re.compile(r"\bdangerouslySetInnerHTML\b"), "Audit untrusted HTML and sanitization"),
    ("Infinite animation", re.compile(r"animation\s*:[^;]*infinite", re.I), "Verify reduced motion and pause control"),
    ("Icon-only button", re.compile(r"<button\b(?:(?!>).)*>\s*<(?:svg|Icon|[A-Z]\w*Icon)\b", re.S), "Check accessible name manually"),
)
SKIP = {"node_modules", ".git", "dist", "build", ".next", "coverage", "vendor"}
EXT = {".tsx", ".jsx", ".ts", ".js", ".css", ".html", ".vue", ".svelte"}

def scan(root: Path):
    count = 0
    for path in root.rglob("*"):
        if path.suffix not in EXT or any(part in SKIP for part in path.parts) or not path.is_file(): continue
        if path.stat().st_size > 1_000_000: continue
        try: text = path.read_text(encoding="utf-8")
        except UnicodeError: continue
        for label, pattern, recommendation in RULES:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                print(f"{path.relative_to(root)}:{line}: {label} — {recommendation}")
                count += 1
    return count

def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument("path", nargs="?", default=".")
    args = p.parse_args(); root = Path(args.path).resolve()
    if not root.is_dir(): p.error("Not a directory")
    count = scan(root)
    print(f"Advisory findings: {count}; manual review required. This scan does not establish WCAG compliance.")

if __name__ == "__main__": main()
