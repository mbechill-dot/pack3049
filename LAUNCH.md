# Launch checklist for pack3049.com

Short answer to "is the launch tied to everything else working": **no.** The website has no dependency on the registration apps, the popcorn engine, or anything else being finished. It is plain HTML, CSS, and JavaScript that runs entirely in the visitor's browser. The moment DNS resolves, everything below in the first list is live and correct.

The one visible gap is the two registration buttons, and they already fail gracefully on purpose.

---

## Works the instant the domain resolves

Nothing here depends on any other system.

- All ten pages, the navigation, the mobile menu, the fonts, and the full design
- **The buyout calculator.** Runs in the browser, saves to the visitor's own device, sends nothing anywhere
- **The calendar.** Past dates dim themselves against the reader's clock
- **The announcement banner.** Relabels itself to This Monday, Tomorrow night, Tonight, then deletes itself after August 24
- **The popcorn page**: twelve products with prices and allergens, the rewards ladder, the sales script, key dates
- **The camp page**: all seven sections from the 2026 parent packet
- **Every phone number and email**, tap-to-call and tap-to-email on a phone
- The 404 page, which GitHub Pages picks up automatically

## Works, but points at something you own

These are live links. They work on day one, but they depend on a service outside this repository staying up and unchanged.

| What | Where it points | If it changes |
|---|---|---|
| Storefront booking button and QR | Your Microsoft Bookings page | Regenerate the QR into `images/storefront-qr.png` and update the two links in the block |
| BAND, pack group | `band.us/n/a8a0b4Jfwc2b5` | One line in `build.py` |
| BAND, camp chat | `band.us/n/a3a3bacae6h2c` | One line in `build.py`, camp page only |
| Facebook group | The pack group | One line in `build.py` |
| Pack inbox | `cubpack3049@gmail.com` | One line in `build.py` |
| Scout Shop, council, CCLT, church, Legion, PRP | Their own sites | Nothing to do unless they move |

## Not finished yet

None of these stop the launch. They are visible gaps a visitor might notice.

**1. The two registration buttons.** Until you paste the deployed Apps Script URLs, both show a notice reading "This application link has not been set up yet. Contact a Cubmaster and they will register your Scout directly," and send the family to the contact page. Nobody hits a dead link. Set them in `build.py`:

```python
YOUTH_APPLICATION_URL = ""
ADULT_APPLICATION_URL = ""
```

Paste a URL between the quotes, run `python3 build.py`, and the notices vanish on their own.

**2. The photo gallery** is all placeholder tiles until you add images.

**3. Popcorn product photos** show colored tiles until files land in `images/products/`.

**4. Numbers still to confirm.** These appear on the site with values I derived rather than ones you gave me. Each is marked with a red box on the page.

- The council fee, the sibling and leader discount amounts, and the payment due date on the join page
- The popcorn sales goal and buyout amount, which the calculator uses. It currently assumes **$200 buyout at 38 percent**, taken from your 2024 owed letter, where that formula reproduced all nine published amounts exactly. If this year differs, two constants in `assets/site.js`
- The camp fees and payment deadline
- The 2023 season total. Your kickoff deck says $40,000, your final sales data says $36,242. The site shows $40,000
- The November 16 den meeting location, currently "info to come"

**5. Two things to confirm with people, not code.** That the leadership names on the contact page are current and that each of those volunteers is comfortable being named on a public page, and that "haunted corn maze" is the right name for the October event.

---

## Turning it on

1. Push this folder to a GitHub repository.
2. **Settings, Pages.** Source: Deploy from a branch, `main`, `/ (root)`.
3. At your registrar, point `pack3049.com` at GitHub with the four A records in the README, and `www` with a CNAME.
4. Back in **Settings, Pages**, enter `pack3049.com` under Custom domain.
5. Wait for the DNS check to pass, then tick **Enforce HTTPS**. The certificate is free and can take up to a day.

DNS can take a few hours to spread. If the site looks broken right after the switch, wait before changing anything.

## After it is live, check these on your phone

- The site loads at `https://pack3049.com` with a padlock
- The menu opens and every page is reachable
- Tapping a phone number starts a call
- The popcorn calculator updates as you type
- The storefront QR scans to the booking page
- Both registration buttons show the notice, not an error
