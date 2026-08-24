#!/usr/bin/env python3
"""Generate the Pack 3049 static site.

Every page is plain HTML with a shared header and footer stamped in from here,
so editing the nav or footer once updates all pages. Run:  python3 build.py
"""
import os, re

OUT = os.path.dirname(os.path.abspath(__file__))

SITE_TITLE = "Cub Scout Pack 3049"
SITE_URL = "https://pack3049.com"   # matches the CNAME file
TAGLINE = "Leo, Indiana"

NAV = [
    ("index.html", "Home"),
    ("join.html", "Join Us"),
    ("calendar.html", "Calendar"),
    ("popcorn.html", "Popcorn"),
    ("camp.html", "Camp"),
    ("gallery.html", "Gallery"),
    ("faq.html", "FAQ"),
    ("contact.html", "Contact"),
]

FACEBOOK = "https://www.facebook.com/groups/784285322261671"
BAND = "https://band.us/n/a8a0b4Jfwc2b5"        # the pack-wide BAND group
BAND_CAMP = "https://www.band.us/n/a3a3bacae6h2c"  # summer camp chat, camp page only
# Pack contacts, shown across the site.
CUBMASTER_1 = ("Nicole Howard", "(260) 557-2243", "+12605572243", "howardfamily411@gmail.com")
CUBMASTER_2 = ("Dan Noll", "(260) 602-5134", "+12606025134", "steelers6615@gmail.com")
PACK_EMAIL = "cubpack3049@gmail.com"   # the pack inbox; completed applications land here

# ---------------------------------------------------------------------------
# THE TWO APPLICATION LINKS. This is the only place they need to be set.
# Paste the deployed Apps Script web app URLs between the quotes and run
# `python3 build.py`. Each looks like:
#     https://script.google.com/macros/s/AKfycb....../exec
# Leave a line empty and the register page shows a visible "not set up yet"
# notice and sends families to the contact page instead of a dead button.
# ---------------------------------------------------------------------------
# Youth Application v2 deployment. The earlier deployment (AKfycbxk_0LTOtMraw...)
# returned 403 to anonymous visitors even with "Anyone" set, and editing it never
# cleared. A fresh deployment fixed it. Only ever use the URL from the deployment
# listed under Active in Deploy > Manage deployments.
YOUTH_APPLICATION_URL = "https://script.google.com/macros/s/AKfycbx3dPrzCkdgTn0nF3TDx7DEaU6nGh1d0GvCXQViu1nk3dzxvdq9Dl8fgxMXBwnQRlFtrw/exec"
ADULT_APPLICATION_URL = "https://script.google.com/macros/s/AKfycbzxb6_OXWkX8AkNUcO60AXlTwKL0xTdMidVSOae6pH9uY8aFmFhTroR7nAH_k4mSTXqxg/exec"

# Site wide announcement bar. Set BANNER = "" to remove it.
# data-until is the last day it shows; after that the script deletes it.
BANNER = """<div class="eventbar" data-until="2026-08-24">
  <div class="wrap">
    <span class="eventbar__tag" data-event-date="2026-08-24">Monday night</span>
    <p class="eventbar__text">Scouting Kick-Off, Monday August 24, 6:30 to 8:00 PM
      <span>Riverside Gardens Park, Grabill. Bring the whole family.</span></p>
    <a class="eventbar__cta" href="join.html#kickoff">Event details</a>
  </div>
</div>"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#123021">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito+Sans:wght@400;600;700;800&family=Space+Mono:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><circle cx='16' cy='16' r='16' fill='%23123021'/><path d='M16 5l5 8h-3l4 7h-3l4 6H9l4-6h-3l4-7H11z' fill='%23ffc93c'/><rect x='14.6' y='25' width='2.8' height='4' fill='%23ff6b35'/></svg>">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Cub Scout Pack 3049">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">
      <span class="brand__mark" aria-hidden="true">
        <svg viewBox="0 0 32 32" fill="none"><path d="M16 3l5.5 9h-3.2l4.4 7.5h-3.2L24 27H8l4.5-7.5H9.3L13.7 12h-3.2z" fill="#123021"/><rect x="14.5" y="25.5" width="3" height="5" rx="1" fill="#ff6b35"/></svg>
      </span>
      <span class="brand__text">
        <span class="brand__name">Cub Scout Pack 3049</span>
        <span class="brand__sub">Leo &middot; Indiana</span>
      </span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav">Menu</button>
    <nav class="nav" id="primary-nav" aria-label="Primary">
{nav}
    </nav>
  </div>
</header>

<!-- Site wide announcement. It removes itself the day after data-until.
     To change or retire it early, edit BANNER near the top of build.py. -->
{banner}

<main id="main">
{body}
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="grid grid--3">
      <div>
        <h4>Cub Scout Pack 3049</h4>
        <p>Serving kindergarten through 5th grade families in Leo, Grabill, Cedarville, and the surrounding communities for more than 90 years.</p>
        <p><strong>We meet at:</strong> Mondays, 6:30 PM<br>
        <a href="https://cedarcreekchurch.com">Cedar Creek Church</a><br>
        12606 Leo Road, Fort Wayne, IN 46845</p>
        <p><strong>Chartered by:</strong><br>
        Jack Brinker American Legion Post 409<br>
        14133 Leo Road, Leo, IN 46765</p>
      </div>
      <div>
        <h4>Quick links</h4>
        <ul>
          <li><a href="register.html">Register a Scout</a></li>
          <li><a href="join.html">How to join</a></li>
          <li><a href="calendar.html">Pack calendar</a></li>
          <li><a href="popcorn.html">Popcorn fundraiser</a></li>
          <li><a href="camp.html">Camp and outdoors</a></li>
          <li><a href="faq.html">Parent questions</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact us</h4>
        <ul>
          <li><strong>Nicole Howard</strong>, Co-Cubmaster<br>
            <a href="tel:+12605572243">(260) 557-2243</a><br>
            <a href="mailto:howardfamily411@gmail.com">howardfamily411@gmail.com</a></li>
          <li style="margin-top:.6rem"><strong>Dan Noll</strong>, Co-Cubmaster<br>
            <a href="tel:+12606025134">(260) 602-5134</a><br>
            <a href="mailto:steelers6615@gmail.com">steelers6615@gmail.com</a></li>
          <li style="margin-top:.6rem"><strong>The pack inbox</strong><br>
            <a href="mailto:cubpack3049@gmail.com">cubpack3049@gmail.com</a></li>
        </ul>
        <h4 style="margin-top:1.25rem">Stay connected</h4>
        <div class="fsocial">
          <a class="fbtn" href="{facebook}">
            <span class="fbtn__icon fbtn__icon--fb" aria-hidden="true">
              <svg viewBox="0 0 24 24"><path fill="currentColor" d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.68.24 2.68.24v2.96h-1.51c-1.49 0-1.96.93-1.96 1.89v2.26h3.33l-.53 3.49h-2.8V24C19.61 23.1 24 18.1 24 12.07z"/></svg>
            </span>
            <span class="fbtn__text"><b>Facebook group</b><small>Photos and day to day news</small></span>
          </a>
          <a class="fbtn" href="{band}">
            <span class="fbtn__icon fbtn__icon--band" aria-hidden="true">
              <svg viewBox="0 0 24 24"><path fill="currentColor" d="M12 2C6.2 2 1.5 5.9 1.5 10.7c0 2.8 1.6 5.3 4.1 6.9l-.9 3.5c-.1.5.4.9.8.6l4-2.4c.8.1 1.6.2 2.5.2 5.8 0 10.5-3.9 10.5-8.8S17.8 2 12 2zm-4.6 10.4a1.6 1.6 0 1 1 0-3.2 1.6 1.6 0 0 1 0 3.2zm4.6 0a1.6 1.6 0 1 1 0-3.2 1.6 1.6 0 0 1 0 3.2zm4.6 0a1.6 1.6 0 1 1 0-3.2 1.6 1.6 0 0 1 0 3.2z"/></svg>
            </span>
            <span class="fbtn__text"><b>BAND app</b><small>Schedule changes and reminders</small></span>
          </a>
        </div>
        <ul class="fsocial__more">
          <li><a href="https://www.awac.org/">Anthony Wayne Area Council</a></li>
          <li><a href="https://www.scouting.org/">Scouting America</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span data-year>2026</span> Cub Scout Pack 3049, Leo, Indiana. Chartered by <a href="https://maps.google.com/?q=14133+Leo+Rd,+Leo,+IN+46765">Jack Brinker American Legion Post 409</a>, Leo, Indiana. Anthony Wayne Area Council, Pokagon District, Scouting America. Site maintained by Michael Bechill, Committee Chair. This is not an official publication of Scouting America.</p>
    </div>
  </div>
</footer>

<script src="assets/site.js"></script>
</body>
</html>
"""


def render(filename, title, desc, body):
    nav = "\n".join(
        '      <a href="{href}"{cur}>{label}</a>'.format(
            href=href,
            label=label,
            cur=' aria-current="page"' if href == filename else "",
        )
        for href, label in NAV
    )
    canonical = SITE_URL + "/" + ("" if filename == "index.html" else filename)
    # An unset application URL falls back to the guarded placeholder, which the
    # page script turns into a visible notice.
    body = body.replace("__YOUTH_APPLICATION_URL__",
                        YOUTH_APPLICATION_URL or "PASTE_YOUTH_APPS_SCRIPT_EXEC_URL_HERE")
    body = body.replace("__ADULT_APPLICATION_URL__",
                        ADULT_APPLICATION_URL or "PASTE_ADULT_APPS_SCRIPT_EXEC_URL_HERE")
    # The red "one thing left" setup box is for you, not for visitors. Once both
    # application URLs are set it has nothing left to say, so drop it.
    if YOUTH_APPLICATION_URL and ADULT_APPLICATION_URL:
        body = re.sub(r"<!--SETUP-NOTE-->.*?<!--/SETUP-NOTE-->", "", body, flags=re.S)
    html = TEMPLATE.format(
        title=title, desc=desc, nav=nav, body=body, banner=BANNER,
        facebook=FACEBOOK, band=BAND, canonical=canonical,
    )
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    return filename


if __name__ == "__main__":
    from content import PAGES, ORDER
    for name in ORDER:
        title, desc, body = PAGES[name]
        render(name, title, desc, body)
        print("wrote", name)
