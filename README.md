# Plan Picker

Pick furniture piece by piece from a floorplan.

1. **Plan** — upload the furniture plan (PDF or image). Turn on *Tag pieces* and tap each piece drawn on the plan; name it with one tap from the tray. Pinch or scroll to zoom, drag to pan, drag a tag to move it. New tags go into the room shown in the dock.
2. **Library** — upload vendor PDFs or presentation boards, open a page, and drag a box around each product to cut it into the library. *Find pieces on this page* asks Claude to mark the products for you.
3. **Choose** — tap a tag to set its **first pick** and **backup** from the library.
4. **Schedule** — every tag by room with both picks and totals. Export a CSV or **make a selection report** (PDF) at any stage; open pieces are flagged and the report is marked as a working draft until every piece has a first pick.

## Where projects are saved

The web app saves projects in the browser on each device (IndexedDB), works offline once loaded, and can be added to the home screen. To move a project to another device, use **⋯ → Save a backup file**, then **Open a backup file** on the other device.

The same app also runs as a Claude artifact, where projects sync wherever the page is opened.

## Finding pieces with Claude (optional)

In the web app the scan uses your own Anthropic API key (**⋯ → Find pieces with Claude**). The key stays in that browser and is sent only to Anthropic. API usage is billed separately from a Claude subscription. Everything else works without a key.

## Development

The whole app is one file: `src/app.html`. Run `python3 build.py` to produce:

- `index.html` — the web app served by GitHub Pages
- `dist/artifact.html` — the same page for publishing as a Claude artifact

No build tools or dependencies beyond Python 3. PDF.js and jsPDF load from cdnjs.
