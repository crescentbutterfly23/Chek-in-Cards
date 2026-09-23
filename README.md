# ASCEND Check-in Cards

A small web app that prints check-in cards for the ASCEND Agent Expo (Oct 6–8, 2026) on **Avery 5392** name badge inserts. Each card gets its own ticket number and QR code. There are two designs: **full color**, and **black & white** for when the printer runs low on ink.

**Open it:** https://crescentbutterfly23.github.io/Chek-in-Cards/ (after GitHub Pages is turned on; see below). You can also double-click `index.html` from a download of this repo. It works offline, because the fonts, logos and QR generator are all inside that one file.

Ticket lists never leave your computer. The page makes the QR codes in your browser and doesn't upload anything. It remembers your last list in that browser only.

## Making cards

1. Pick **Full color** or **Black & white**.
2. Add the tickets in one of three ways:
   - **Load CSV / TXT:** load an export from your ticketing or check-in system. Start from [`templates/ticket-template.csv`](templates/ticket-template.csv):
     ```
     Ticket,QR Link
     E1001,https://your-checkin-link/for-E1001
     ```
     **Ticket** is the number printed on the card, and **QR Link** is what the QR code holds. It can be a link, or a code or token your check-in scanner expects. Extra columns such as names or emails are ignored. The tool finds both columns, and you can change its choice in the dropdowns if it guesses wrong. Rows without a link are flagged. See [`templates/example-import.csv`](templates/example-import.csv) for a messy real-world export it handles.
   - **Paste:** paste one ticket per line (`E1004`, or `E1004, <QR content>`), or two columns straight from a spreadsheet.
   - **Fill a number range:** e.g. E1001 to E1060. The QR code then follows the **QR content** rule (`{id}` = the ticket number).
3. If your check-in system gives you ready-made QR pictures, click **Use QR images**. Name each file after its ticket (`E1004.png`).
4. Click **Download print-ready PDF**, then open the PDF in Acrobat, Preview or any PDF app and print it on Letter paper at **100% / Actual size**. Don't use "Fit", "Shrink oversized pages" or "Scale to fit".

   The page builds the PDF itself at 300 dpi, so it comes out the same whichever browser made it. That matters because Safari ignores a web page's print settings: it adds its own margins and headers and knocks the sheet off-center. **Print from browser** is still there for Chrome and Edge, with Margins: None, Scale: 100% and Background graphics on.

## The Avery 5392 sheet

The sheet is Letter, portrait:
- **Inserts:** 6 per sheet, 2 across × 3 down. Each is 4in wide × 3in tall, and they meet edge to edge at the perforations.
- **Margins:** 0.25in at the sides and 1in at the top and bottom.

The card is the full 3 × 4in design, turned 90° to fill the insert, so it reads upright in a vertical badge holder. **Top of the card faces** picks which way it turns.

**Page orientation** (toggle in the bottom-right corner):
- **Landscape (default):** turns the whole sheet so every card reads upright, in order E1001, E1002… left to right, top to bottom. The printer turns it back onto the portrait stock. The sheet is symmetrical, so it lands on the perforations whichever way it turns.
- **Portrait:** shows the sheet exactly as it feeds.

Edge options:
- **Bleed, 0.125in (full color):** on by default. The dark background runs past the sheet's outer edges; the inner edges meet at the perforations and need no bleed.
- **Card outline:** off by default, because a line slightly off a perforation shows.
- **Crop marks:** off by default. Only needed if you print on plain paper and cut by hand.

### Lining up with the perforations

Print the **Alignment test PDF** (or [`samples/alignment-test.pdf`](samples/alignment-test.pdf)) on one Avery sheet first, at 100%. Each insert gets an outline 1/8in inside its perforations, and two rulers should measure exactly **8in** and **9in**.

- **Rulers short, or the drift grows toward the back of the sheet:** the printer is scaling the page. In Acrobat choose **Actual size**. In Preview choose **Scale 100%**, not "Scale to fit". Turn off any "Fit to page" or "Shrink" option in the printer's own settings. If it persists, switch the corner toggle to Portrait and download again: some drivers scale when they turn a landscape page.
- **Rulers correct, but every gap shifted the same way:** use **Nudge right / Nudge down**. The directions are on the sheet held portrait.

## Working on it

`index.html` is **built**, so don't edit it directly. Edit [`src/template.html`](src/template.html), then rebuild:

```bash
python3 src/build.py
```

The build inlines everything in `src/assets/` into `index.html`:

| File | What it is |
|---|---|
| `expo-lockup.png` | Color-card logo lockup, separated from the design export at 4× with a transparent background |
| `ascend-badge.png` | B&W-card badge, cut from the design export |
| `inter-latin-*.woff2`, `bebas-neue-latin-400-normal.woff2` | Inter and Bebas Neue (SIL Open Font License) |
| `qrcode.js` | [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) by Kazuhiko Arase (MIT) |

The license texts are in [`src/assets/licenses/`](src/assets/licenses/). Card positions in the template are in 1/96in units (288 × 384 = 3 × 4in) and were measured against the original design exports.

`samples/` holds proof PDFs of both designs and the alignment test sheet.

## Turning on GitHub Pages (once)

On GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `(root)` → Save**. The site appears at the link at the top of this file within a minute or two.

## Keeping ticket data out of the repo

This repo is public. The `.gitignore` blocks every `.csv`, `.tsv`, `.xlsx` and `.pdf` except the templates and samples, so a real ticket list with live check-in links can't be committed by accident. Keep real lists outside this folder anyway.
