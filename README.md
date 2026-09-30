# ASCEND Check-in Cards

A small web app that prints check-in cards and badges for the ASCEND Agent Expo (Oct 6–8, 2026) on Avery name badge stock. Each card gets its own ticket number and QR code. Every sheet type comes in two designs: **full color**, and **black & white** for when the printer runs low on ink.

| Sheet type | What it prints |
|---|---|
| **Avery 5392** | 6 check-in cards per sheet: a 3 × 4in card, in 4 × 3in inserts |
| **Avery 8522** | 2 badges per sheet: 4.25 × 6in, each with two 4.25 × 1.5in tickets that are left blank |

**Open it:** https://crescentbutterfly23.github.io/Chek-in-Cards/. You can also double-click `index.html` from a download of this repo. It works offline, because the fonts, logos and QR generator are all inside that one file.

Ticket lists never leave your computer. The page makes the QR codes in your browser and doesn't upload anything. It remembers your last list and settings in that browser only.

## Making cards

1. Pick the **Sheet type** (Avery 5392 or Avery 8522), then **Full color** or **Black & white**.
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
4. Click **Download print-ready PDF**, open it in Acrobat, Preview or any PDF app, and print on Letter paper at **100% / Actual size**. Don't use "Fit", "Shrink oversized pages" or "Scale to fit".

   The page builds the PDF itself at 300 dpi, so it comes out the same whichever browser made it. That matters because Safari ignores a web page's print settings: it adds its own margins and headers and knocks the sheet off-center. **Print from browser** is still there for Chrome and Edge, with Margins: None, Scale: 100% and Background graphics on.

## Avery 5392

- **Sheet:** Letter portrait. 6 inserts, 2 across × 3 down. Each insert is 4in wide × 3in tall, and they meet edge to edge at the perforations.
- **Margins:** 0.25in at the sides and 1in at the top and bottom.
- **Card:** the 3 × 4in card, turned 90° to fill the insert, so it reads upright in a vertical badge holder. **Top of the card faces** picks which way the card turns.
- **Page orientation** (toggle in the bottom-right corner):
  - **Landscape (default):** turns the whole sheet so every card reads upright, in order E1001, E1002… left to right, top to bottom. The printer turns it back onto the portrait stock. The sheet is symmetrical, so it lands on the perforations whichever way it turns.
  - **Portrait:** shows the sheet exactly as it feeds.
- **Bleed, 0.125in (full color):** the dark background runs past the sheet's outer edges. Inner edges meet at the perforations and need none.

## Avery 8522

- **Sheet:** Letter portrait. 2 badges side by side, each 4.25in wide × 6in tall. They fill the full 8.5in width, so the sheet has no side margin.
- **Tickets:** under each badge are two 4.25 × 1.5in tickets. They're left blank, but their space is reserved.
- **Position:** each column runs badge 1.62–7.62in from the top, then tickets 7.62–9.12in and 9.12–10.62in. Avery's sheet diagram suggested 1.5in; a test print on real stock came out 0.12in (0.3cm) high, so the layout sits 0.12in lower. **The two tickets sit** switches the tickets above the badge if your stock is laid out that way.
- **Full-color edges:** the dark background runs to the centre perforation (the two badges meet there) and down to the ticket perforation, so the tickets stay blank. Above the badge it gets a 0.125in bleed.
- **White margin on the outer side (full color):** 0.2in (about 0.5cm) by default. The badges fill the sheet's full width, and many printers can't print that close to the paper's left and right edges. The design shrinks about 5% and is centred in the dark area, which stops 0.2in from the paper edge. Each badge then needs just one cut, its outer side; turn on **Crop marks** to mark it. Set 0 for edge-to-edge color on a borderless printer. The white-background design keeps its content more than 0.3in from every edge and stays full size.

## Both sheet types

- **Card outline:** off by default, because a line slightly off a perforation shows.
- **Crop marks:** off by default. Only needed if you print on plain paper and cut by hand.

### Lining up with the perforations

Before the full run, download the **Alignment test PDF** for your sheet type, or use [`samples/alignment-test-5392.pdf`](samples/alignment-test-5392.pdf) or [`samples/alignment-test-8522.pdf`](samples/alignment-test-8522.pdf). Print it on one real Avery sheet at 100%. Every insert, badge and ticket gets an outline 1/8in inside its perforations, and two rulers should measure exactly **8in** and **9in**.

- **Rulers short, or the drift grows toward the back of the sheet:** the printer is scaling the page. In Acrobat choose **Actual size**. In Preview choose **Scale 100%**, not "Scale to fit". Turn off any "Fit to page" or "Shrink" option in the printer's own settings. On 5392, if it persists, switch the corner toggle to Portrait and download again: some drivers scale when they turn a landscape page.
- **Rulers correct, but every gap shifted the same way:** use **Nudge right / Nudge down**. The directions are on the sheet held portrait.

Avery doesn't publish these sheets' margins. The 5392 margins follow from the sheet math, and the 8522 position comes from Avery's sheet diagram, corrected by a test print on real stock. That's why the test sheet matters.

## Working on it

`index.html` is **built**, so don't edit it directly. Edit [`src/template.html`](src/template.html), then rebuild:

```bash
python3 src/build.py
```

The build inlines everything in `src/assets/` into `index.html`:

| File | What it is |
|---|---|
| `expo-lockup-5392.png`, `expo-lockup-8522.png` | Full-color logo lockup for each design, separated from the design exports at 4× with a transparent background |
| `ascend-badge-5392.png`, `ascend-badge-8522.png` | Black-and-white design's badge logo, cut from each design export |
| `inter-latin-*.woff2`, `bebas-neue-latin-400-normal.woff2` | Inter and Bebas Neue (SIL Open Font License) |
| `qrcode.js` | [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) by Kazuhiko Arase (MIT) |

The license texts are in [`src/assets/licenses/`](src/assets/licenses/). Card positions are in 1/96in units (5392: 288 × 384 = 3 × 4in; 8522: 408 × 576 = 4.25 × 6in), measured against each design's own export.

`samples/` holds a proof PDF of each design on each sheet type, plus both alignment test sheets.

## Turning on GitHub Pages (once)

On GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `(root)` → Save**. The site appears at the link at the top of this file within a minute or two.

## Keeping ticket data out of the repo

This repo is public. The `.gitignore` blocks every `.csv`, `.tsv`, `.xlsx` and `.pdf` except the templates and samples, so a real ticket list with live check-in links can't be committed by accident. Keep real lists outside this folder anyway.
