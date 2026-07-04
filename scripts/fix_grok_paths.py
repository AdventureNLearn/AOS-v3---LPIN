#!/usr/bin/env python3
"""
Bulk Path Replacement Script for AOS v3.0
Replaces hard-coded .grok/skills/ paths with portable skills/ paths.

Run this script after cloning if any old .grok/ references remain in docs or other files.
"""
import os
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
EXTENSIONS = {".md", ".html", ".json"}

REPLACEMENTS = [
    (r"\.grok/skills/", "skills/"),
]

def fix_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        original = content
        for pattern, repl in REPLACEMENTS:
            content = re.sub(pattern, repl, content)
        if content != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Fixed: {filepath.relative_to(ROOT)}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

def main():
    print("Running bulk .grok path cleanup...")
    for f in ROOT.rglob("*"):
        if f.is_file() and f.suffix in EXTENSIONS:
            fix_file(f)
    print("Done.")

if __name__ == "__main__":
    main()