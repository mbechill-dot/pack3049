# Cub Scout Pack 3049 website

A plain static website for Cub Scout Pack 3049, Leo, Indiana. No frameworks, no build tools required, no JavaScript dependencies. It is designed to be hosted free on GitHub Pages with a custom domain.

**Launching?** `DEPLOY.md` walks through GitHub and the Spaceship DNS records step by step. `LAUNCH.md` says what works day one and what is still a placeholder. Start with those two.

`LAUNCH.md` It separates what works the moment DNS resolves from what is still a placeholder, and answers the question of whether the site depends on anything else being finished. It does not.

## What is in here

```
index.html      Home
join.html       How to join, costs, uniform
calendar.html   Meeting rhythm and the year's events
popcorn.html    The popcorn fundraiser
camp.html       Summer camp and outdoor program
gallery.html    Photo gallery
faq.html        Parent questions
contact.html    Leaders, social links, Scout Shop
register.html   Registration, links out to the application form
404.html        Not found page

assets/style.css   All the styling
assets/site.js     Mobile menu, footer year, past event dimming and removal
images/            Photos. Kick-Off flyer, plus products/ for popcorn photos.
CNAME              Your custom domain
DEPLOY.md          GitHub push and Spaceship DNS, step by step
LAUNCH.md          Launch checklist: what works day one, what is still blank
build.py           Optional page generator. The two application URLs live here
content.py         Page text, if you use the generator
```

## Two ways to edit

**Just edit the HTML.** Open any `.html` file and change the text. This is the simplest path and nothing will break. If you change the navigation or the footer you will need to change it in every page, since each page is self contained.

**Or use the generator.** `content.py` holds the text of every page and `build.py` stamps the shared header, navigation, and footer around it. Edit `content.py`, then run:

```
python3 build.py
```

That rewrites all the `.html` files. Change the nav or footer once in `build.py` and every page updates. Requires Python 3, nothing else.

Pick one and stick with it. If you hand edit the HTML and then run `build.py`, your hand edits are overwritten.

## Things to fill in before launch

Search the site for the red boxes labeled "Before this goes live". Each one names what to replace. The short list:

1. ~~Your domain.~~ Done. `CNAME` is set to `pack3049.com` and every page carries a canonical URL pointing there.
2. **Fees.** `join.html` needs the current council fee, the pack program fee, and the payment due date.
3. **Popcorn details.** `popcorn.html` needs this season's sales goal, buyout amount, and gift card percentage.
4. **Camp fees.** `camp.html` needs the per Scout and per adult camp fee and the payment deadline.
5. **Photos.** Drop files into `images/` and replace the placeholders in `gallery.html`.

Already wired up and correct: the Cedar Creek Church address, both BAND links and the Facebook group, the Cubmaster contact details, the full Fall 2026 schedule, and the whole camp page from the 2026 parent packet.

## Registration, and the one thing that is not finished

`register.html` is where every registration button on the site points: the home hero, both Kick-Off blocks, the join page steps, the contact page, and the 404. It explains the three steps and then sends families out to the official application.

**The two application URLs are not set yet.** The buttons should point at the deployed Apps Script intake engines you already built, not at the raw PDF on filestore.scouting.org. Those engines ask the questions in plain language, draw the answers onto the official 524-406 at exact coordinates, and email the finished PDF to the parent and to `cubpack3049@gmail.com`.

To get each URL: in the Apps Script editor choose **Deploy, New deployment, Web app**, set **Execute as: Me** and **Who has access: Anyone**, then copy the `https://script.google.com/macros/s/.../exec` URL.

Paste the youth one over `PASTE_YOUTH_APPS_SCRIPT_EXEC_URL_HERE` and the adult 524-501 one over `PASTE_ADULT_APPS_SCRIPT_EXEC_URL_HERE` in `content.py` under `PAGES["register.html"]`, then run `python3 build.py`.

Until you do, a script in `assets/site.js` redirects those two buttons to the contact page and prints a red warning under each one telling the family to contact a Cubmaster instead. **Nobody taps a dead link.** The warning removes itself automatically the moment a real URL is in place, so there is nothing to clean up afterward.

Two tokens the supplied block referenced, `--sand` and `--muted`, did not exist in this palette. They are mapped to the site's own paper and soft ink in `style.css` rather than falling back to the cream and warm grey in the original, which would have clashed with the sage and pine used everywhere else.

## The announcement banner

A gold strip sits under the navigation on every page. It is defined once, as `BANNER` near the top of `build.py`.

Its label writes itself. The tag carries `data-event-date="2026-08-24"` and a script in `site.js` compares that to the reader's own clock, so it reads **This Monday**, then **Tomorrow night**, then **Tonight**, then the whole banner removes itself. You never have to remember to change the wording on the day.

- **To change it:** edit the text in `BANNER` and re-run `python3 build.py`.
- **To remove it:** set `BANNER = ""` and rebuild.
- **It expires on its own.** The `data-until="2026-08-24"` attribute is the last day it shows. After that date the page script deletes it, so a stale banner will not sit there advertising an event that already happened. Set a new date when you write a new announcement.

The same expiry trick works on any element. The featured Kick-Off blocks on the home and join pages carry `data-until` too, and the calendar dims rows whose `data-date` has passed.

The Kick-Off blocks show the event flyer itself, at `images/scouting-kickoff-2026.jpg`. To promote a different event, drop the new flyer in `images/`, point the `<img>` and its link at it, and rewrite the `alt` text so the details are still readable to anyone using a screen reader or with images turned off.

## Adding the popcorn product photos

The popcorn page shows all twelve products as colored tiles with prices and allergen information. Each tile is ready to be replaced by a real product photo, and nothing else has to change when you add one.

**To add a photo:** save it into `images/products/` using the exact filename below. That is it. The tile picks it up on the next page load, fades the photo in over the colored tile, and falls back to the tile again if the file is ever missing or renamed.

```
images/products/popping-corn.jpg        images/products/butter-microwave.jpg
images/products/caramel.jpg             images/products/kettle-corn.jpg
images/products/cheddar.jpg             images/products/caramel-sea-salt.jpg
images/products/jalapeno-cheese.jpg     images/products/sea-salt-splash.jpg
images/products/trail-mix.jpg           images/products/mountain-munch.jpg
images/products/freedom-pretzels.jpg    images/products/cheese-lovers.jpg
```

Square images work best, since the tile is a square. Resize to about 800 pixels wide before uploading so the page stays fast on a phone.

**Where to get them:** Pecatonica River Popcorn publishes product images and printable sales resources at prpopcorn.com under its resources section, and the same artwork usually appears in Scout Boss and in the council's kickoff materials. Those are the pack's proper source. They are PRP's images, so use the ones they provide to units rather than pulling them off a retail page, and if you ever want to be certain, the council popcorn staff can confirm what units may post.

## Storefront booking

The popcorn page has a **Book a storefront shift** block with a button and a scannable QR code, both pointing at the pack's Microsoft Bookings page:

```
https://outlook.office365.com/book/CubScoutsPack3049Popcorn@indianatechedu.onmicrosoft.com/
```

The QR image is `images/storefront-qr.png`. It was cleaned up from the original graphic, the mirrored reflection trimmed off and a proper quiet zone added around the code, then re-scanned to confirm it still resolves to the same URL. If the booking link ever changes, generate a fresh QR and replace that file, and update the two links in the block.

The QR prints larger than it displays, so the popcorn page can be printed and pinned to a table at the kick-off.

## The buyout calculator

The popcorn page has a calculator where a parent types in their Scout's sales so far and sees what a buyout would cost them right now, what the pack has been credited, their Scout's gift card, and how far they are from free camp and the Winner's Circle.

**The formula** is the one the pack already uses:

```
owed = max(0, BUYOUT - sales x RATE)
```

It was checked against the 2024 "money owed to the pack" letter and reproduces all nine published amounts exactly, including the $0 for the Scout who had cleared it.

**To set this year's numbers,** open `assets/site.js`, scroll to the bottom, and edit the four constants at the top of the calculator block:

```
var BUYOUT = 200;    // pack program cost per Scout, the full cash buyout
var RATE   = 0.38;   // pack commission credited on a Scout's sales
var BACK   = 0.04;   // paid to the Scout as an Amazon gift card
var CAMP   = 1600;   // free Cub Resident Camp at CCLT
var CIRCLE = 3000;   // Winner's Circle Club
```

Everything else recalculates from those, including the sell-this-much-more figure and the progress bar, so there is nothing else to hunt down.

**Privacy:** the number a parent types never leaves their device. It is kept in their own browser's local storage so it is still there when they come back, and the Clear button wipes it. Nothing is sent to the pack, to GitHub, or anywhere else. The page says so plainly, because parents should not have to wonder.

## Allergen information

Each product tile lists allergens, transcribed from PRP's published nutrition page. This is on the site because families ask and because several Scouts in the pack have nut allergies.

Treat it as a courtesy, not a guarantee. The page tells readers to check the actual package, and links to `pecatonicariverpopcorn.com/nutrition-information/` for full nutrition facts. If PRP changes a formulation, that text needs updating here too, so re-check it at the start of each season.

## The two BAND groups

The pack runs two separate BAND groups and the site keeps them apart on purpose.

- **`BAND`** in `build.py` and `content.py` is the pack-wide group, "Cub Scouts Pack 3049". It appears in the footer of every page and anywhere the site talks about schedule changes, weather cancellations, and popcorn updates.
- **`BAND_CAMP`** is the summer camp chat, and it appears **only on `camp.html`**. It is for families going to CCLT: packing questions, carpools, and the week itself.

If you ever swap one, change it in the constant at the top of the file rather than hunting through pages. Getting these backwards means a new family lands in a camp chat that goes quiet for eleven months of the year.

## Contact details on the site

Nicole Howard and Dan Noll are listed as the pack's main contacts, with phone numbers and email addresses, on every page and in the footer. Michael Bechill is credited as Committee Chair.

These are real phone numbers and inboxes on a public page that search engines will index. That is a deliberate choice and it matches the recruiting flyer, but it does mean those addresses will collect some spam over time. If you ever want to pull them back, they are defined in two places: `CONTACTS` near the top of `content.py`, and the footer block in `build.py`.

## Publishing on GitHub Pages

1. Create a new repository on GitHub. A public repo named something like `pack3049` works well.
2. Upload everything in this folder to the repository root, or push it with git:

   ```
   git init
   git add .
   git commit -m "Pack 3049 website"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/pack3049.git
   git push -u origin main
   ```

3. In the repository, go to **Settings, Pages**. Under **Source**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`. Save.
4. Wait a minute or two. The site appears at `https://YOUR-USERNAME.github.io/pack3049/`.

The `.nojekyll` file tells GitHub not to run Jekyll on the files, which avoids surprises with folder names.

## Custom domain: pack3049.com

The `CNAME` file already says `pack3049.com`, and `SITE_URL` in `build.py` matches it. What is left is DNS at your registrar.

1. At your domain registrar, create these DNS records:

   **Apex domain** (`pack3049.com`), four A records pointing at GitHub Pages:

   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```

   And optionally the matching AAAA records for IPv6:

   ```
   2606:50c0:8000::153
   2606:50c0:8001::153
   2606:50c0:8002::153
   2606:50c0:8003::153
   ```

   **The www subdomain** (`www.pack3049.com`), one CNAME record pointing to:

   ```
   YOUR-USERNAME.github.io
   ```

2. Back in **Settings, Pages**, enter `pack3049.com` under **Custom domain** and save. Once GitHub reports the DNS check has passed, tick **Enforce HTTPS**. The certificate is free and automatic, and can take up to a day to issue.

DNS changes can take a few hours to spread. If the site looks broken right after the switch, wait before changing anything else.

## Accessibility

The palette is checked against WCAG AA contrast, and the site currently passes with zero failures at both desktop and phone widths. Two rules keep it that way, and both are easy to break by accident:

1. **Orange text on a light background uses `--fire-ink` (#b83c07), not `--fire-500`.** The bright orange is for fills, not for words. `--fire-500` behind dark `--pine-950` text is the button and pill pattern.
2. **Any component that paints its own light surface must also declare its own text color.** Inside `.section--pine` everything inherits pale text, so a white card without an explicit `color` renders white on white. `.table-scroll`, `.editme`, `.bigevent`, `.card--stem`, and `.contacts__card` all set their own ink for exactly this reason. Add yours to that list.

## A note on privacy

This site is public. It deliberately contains no Scout names, no family contact information, no roster data, and no dues or payment records. Keep it that way. Anything that identifies a specific child belongs in the private Facebook group or the BAND app, not here.

Photos on the gallery page should not be captioned with children's full names, and any family that asks to be left out should be left out, immediately and without discussion.

## Credits

Built for Pack 3049, Leo, Indiana. Chartered by Jack Brinker American Legion Post 409, Leo, Indiana. Anthony Wayne Area Council, Pokagon District, Scouting America. Meetings are held at Cedar Creek Church, which is the pack's meeting home, not its chartered organization. Those are two different things and the site keeps them distinct.

This is a volunteer maintained site and not an official publication of Scouting America.
