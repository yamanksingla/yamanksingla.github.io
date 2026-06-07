#!/usr/bin/env python3
"""Post-render: append PhD thesis URL to the generated sitemap.xml."""
import re, pathlib

sitemap = pathlib.Path("_book/sitemap.xml")
if not sitemap.exists():
    raise SystemExit("sitemap.xml not found in _book/")

content = sitemap.read_text()

thesis_entry = """  <url>
    <loc>https://yamanksingla.github.io/PhD-thesis/</loc>
  </url>"""

if "PhD-thesis" not in content:
    content = content.replace("</urlset>", thesis_entry + "\n</urlset>")
    sitemap.write_text(content)
    print("Added PhD thesis to sitemap.xml")
else:
    print("PhD thesis already in sitemap.xml")
