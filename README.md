# Cub Scout Pack 3049 website

The public website for Cub Scout Pack 3049, Leo, Indiana. Live at **https://pack3049.com**.

Plain HTML, CSS, and JavaScript. No frameworks, no build tools required at runtime, no dependencies to keep updated. Hosted free on GitHub Pages.

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
register.html   Registration, links out to the application apps
404.html        Not found page

assets/style.css   All the styling
assets/site.js     Mobile menu, footer year, past event dimming, buyout calculator
images/            Photos. Kick-Off flyer, storefront QR, plus products/ for popcorn photos
CNAME              The custom domain
build.py           Page generator. The two application URLs live here
content.py         Page text
```

## Two ways to edit

**Just edit the HTML.** Open any `.html` file and change the text. Nothing will break. If you change the navigation or the footer you have to change it in every page, since each page is self contained.

**Or use the generator.** `content.py` holds the text of every page and `build.py` stamps the shared header, navigation, and footer around it. Edit `content.py`, then run:

```
python3 build.py
```

That rewrites all the `.html` files. Change the nav or footer once in `build.py` and every page updates. Requires Python 3, nothing else.

Pick one and stick with it. If you hand edit the HTML and then run `build.py`, your hand edits are overwritten.

## Where the important settings live

All near the top of `build.py`:

| Constant | What it is |
|---|---|
| `YOUTH_APPLICATION_URL` | The youth application web app. Blank shows a notice instead of a dead button |
| `ADULT_APPLICATION_URL` | The adult application web app. Same behavior |
| `BAND` | The pack-wide BAND group, used everywhere |
| `BAND_CAMP` | The summer camp chat, used only on `camp.html` |
| `FACEBOOK` | The pack Facebook group |
| `CUBMASTER_1`, `CUBMASTER_2` | Name, phone, and email for each Co-Cubmaster |
| `PACK_EMAIL` | The pack inbox |
| `BANNER` | The site wide announcement strip. Set to `""` to remove it |

## The announcement banner

A gold strip sits under the navigation on every page, defined once as `BANNER` in `build.py`.

Its label writes itself. The tag carries `data-event-date` and a script compares that to the reader's own clock, so it reads **This Monday**, then **Tomorrow night**, then **Tonight**. The `data-until` attribute is the last day it shows; after that the page script deletes the whole strip, so a stale banner never sits there advertising an event that already happened.

- **To change it:** edit the text in `BANNER` and re-run `python3 build.py`.
- **To remove it:** set `BANNER = ""` and rebuild.

The same expiry trick works on any element. The calendar dims rows whose `data-date` has passed.

## Adding photos

Drop image files into `images/`, resized to about 1200 pixels wide so pages stay fast, then reference them from `content.py` as:

```html
<img src="images/your-file.jpg" alt="short description" loading="lazy">
```

Use photos where kids are not individually identified by name, and honor any family's photo opt out immediately.

## Adding the popcorn product photos

Each of the twelve products shows a colored tile until a real photo exists. Save the photo into `images/products/` using the exact filename below and the tile picks it up on the next page load, fading the photo in. If a file is ever missing or renamed it falls back to the tile.

```
images/products/popping-corn.jpg        images/products/butter-microwave.jpg
images/products/caramel.jpg             images/products/kettle-corn.jpg
images/products/cheddar.jpg             images/products/caramel-sea-salt.jpg
images/products/jalapeno-cheese.jpg     images/products/sea-salt-splash.jpg
images/products/trail-mix.jpg           images/products/mountain-munch.jpg
images/products/freedom-pretzels.jpg    images/products/cheese-lovers.jpg
```

Square images, about 800 pixels wide. Pecatonica River Popcorn publishes product images to units at prpopcorn.com, and the same artwork appears in Scout Boss and council kickoff materials. Use the ones PRP provides to units rather than pulling them off a retail page.

## Storefront booking

The popcorn page has a **Book a storefront shift** block with a button and a scannable QR code, both pointing at the pack's Microsoft Bookings page. The QR image is `images/storefront-qr.png`. If the booking link ever changes, generate a fresh QR, replace that file, and update the two links in the block.

The QR prints larger than it displays, so the popcorn page can be printed and pinned to a table at the kick-off.

## The buyout calculator

A parent types their Scout's sales so far and sees what a buyout would cost right now, what the pack has been credited, their Scout's gift card, and how far they are from free camp and the Winner's Circle.

The formula is the one the pack already uses:

```
owed = max(0, BUYOUT - sales x RATE)
```

**To set this year's numbers,** open `assets/site.js` and edit the constants at the top of the calculator block:

```
var BUYOUT = 200;    // pack program cost per Scout, the full cash buyout
var RATE   = 0.38;   // pack commission credited on a Scout's sales
var BACK   = 0.04;   // paid to the Scout as an Amazon gift card
var CAMP   = 1600;   // free Cub Resident Camp at CCLT
var CIRCLE = 3000;   // Winner's Circle Club
```

Everything else recalculates from those, including the sell-this-much-more figure and the progress bar.

**Privacy:** the number a parent types never leaves their device. It is kept in their own browser's local storage so it is still there when they come back, and the Clear button wipes it. Nothing is sent to the pack, to GitHub, or anywhere else. The page says so plainly, because parents should not have to wonder.

## Allergen information

Each product tile lists allergens, transcribed from PRP's published nutrition page. This is on the site because families ask and because several Scouts in the pack have nut allergies.

Treat it as a courtesy, not a guarantee. The page tells readers to check the actual package and links to the full nutrition facts. If PRP changes a formulation, re-check this text at the start of each season.

## The two BAND groups

The pack runs two separate BAND groups and the site keeps them apart on purpose.

- **`BAND`** is the pack-wide group. It appears in the footer of every page and anywhere the site talks about schedule changes, weather cancellations, and popcorn updates.
- **`BAND_CAMP`** is the summer camp chat, and it appears **only on `camp.html`**. It is for families going to CCLT: packing questions, carpools, and the week itself.

Getting these backwards means a new family lands in a camp chat that goes quiet for eleven months of the year.

## Contact details on the site

Nicole Howard and Dan Noll are listed as the pack's main contacts, with phone numbers and email addresses, on every page and in the footer. Michael Bechill is credited as Committee Chair, by name only.

These are real phone numbers and inboxes on a public page that search engines index. That is a deliberate choice and it matches the recruiting flyer, but it does mean those addresses will collect some spam over time. To pull them back, they are defined in `CUBMASTER_1` and `CUBMASTER_2` in `build.py` and in the footer block in the same file.

## Hosting

GitHub Pages, from the `main` branch, `/ (root)` folder. The `CNAME` file holds the custom domain and `.nojekyll` tells GitHub not to run Jekyll on the files.

DNS lives at the registrar: four A records on the apex pointing at GitHub Pages (`185.199.108.153` through `185.199.111.153`), and a `www` CNAME pointing at `mbechill-dot.github.io`.

## Accessibility

The palette is checked against WCAG AA contrast and passes with zero failures at both desktop and phone widths. Two rules keep it that way, and both are easy to break by accident:

1. **Orange text on a light background uses `--fire-ink` (#b83c07), not `--fire-500`.** The bright orange is for fills, not for words. `--fire-500` behind dark `--pine-950` text is the button and pill pattern.
2. **Any component that paints its own light surface must also declare its own text color.** Inside `.section--pine` everything inherits pale text, so a white card without an explicit `color` renders white on white. `.table-scroll`, `.bigevent`, `.card--stem`, `.reg`, and `.contacts__card` all set their own ink for exactly this reason. Add yours to that list.

## A note on privacy

This site is public. It deliberately contains no Scout names, no family contact information, no roster data, and no dues or payment records. Keep it that way. Anything that identifies a specific child belongs in the private Facebook group or the BAND app, not here.

Photos should not be captioned with children's full names, and any family that asks to be left out should be left out, immediately and without discussion.

## Credits

Built for Pack 3049, Leo, Indiana. Chartered by Jack Brinker American Legion Post 409, Leo, Indiana. Anthony Wayne Area Council, Pokagon District, Scouting America. Meetings are held at Cedar Creek Church, which is the pack's meeting home, not its chartered organization. Those are two different things and the site keeps them distinct.

This is a volunteer maintained site and not an official publication of Scouting America.
