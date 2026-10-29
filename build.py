#!/usr/bin/env python3
"""Build Plan Picker from src/app.html.

  index.html          the standalone web app (GitHub Pages), saves projects in the browser
  dist/artifact.html  the same app as a Claude artifact page (no document wrapper)

Run: python3 build.py
"""
import pathlib, re

root = pathlib.Path(__file__).parent
app = (root / "src" / "app.html").read_text()

head_extra = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Tag every piece on a furniture plan and choose a first pick and a backup from vendor PDFs.">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Plan Picker">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>
"""

# split the fragment: everything before the first <div id="app"> belongs in <head>
i = app.index('<div id="app">')
head, body = app[:i], app[i:]
index = f"<!doctype html>\n<html lang=\"en\">\n<head>\n{head_extra}{head}</head>\n<body>\n{body}</body>\n</html>\n"
(root / "index.html").write_text(index)

dist = root / "dist"
dist.mkdir(exist_ok=True)
(dist / "artifact.html").write_text(app)
print("built index.html and dist/artifact.html")
