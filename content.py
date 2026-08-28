# -*- coding: utf-8 -*-
"""Page content for the Pack 3049 site.

Each entry is: filename -> (browser title, meta description, body HTML).
Edit the HTML here and re-run build.py, or edit the generated .html files
directly if you prefer. Both work.
"""

FACEBOOK = "https://www.facebook.com/groups/784285322261671"
BAND = "https://band.us/n/a8a0b4Jfwc2b5"        # the pack-wide BAND group
BAND_CAMP = "https://www.band.us/n/a3a3bacae6h2c"  # summer camp chat, camp page only

ORDER = [
    "index.html", "join.html", "calendar.html", "popcorn.html",
    "camp.html", "gallery.html", "faq.html", "contact.html",
    "register.html", "404.html",
]

CONTACTS = """<div class="contacts">
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Nicole Howard</div>
        <a href="tel:+12605572243">(260) 557-2243</a>
        <a href="mailto:howardfamily411@gmail.com">howardfamily411@gmail.com</a>
      </div>
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Dan Noll</div>
        <a href="tel:+12606025134">(260) 602-5134</a>
        <a href="mailto:steelers6615@gmail.com">steelers6615@gmail.com</a>
      </div>
    </div>"""

PAGES = {}

# Simple white glyphs that sit inside the rank patches.
PAW = ('<svg viewBox="0 0 48 48" fill="#fff" aria-hidden="true">'
       '<circle cx="13" cy="17" r="5"/><circle cx="23" cy="12" r="5.4"/>'
       '<circle cx="33" cy="16" r="4.8"/><circle cx="40" cy="26" r="4"/>'
       '<path d="M23 22c-6.5 0-12 5.4-12 11 0 4 3 6.4 6.4 6.4 2.2 0 3.4-1.1 5.6-1.1s3.4 1.1 5.6 1.1c3.4 0 6.4-2.4 6.4-6.4 0-5.6-5.5-11-12-11z"/>'
       '</svg>')
TENT = ('<svg viewBox="0 0 48 48" aria-hidden="true">'
        '<path d="M24 8 4 39h40z" fill="#fff"/>'
        '<path d="M24 21 15.5 39h17z" fill="#0b1c14" opacity=".38"/>'
        '</svg>')
ARROW = ('<svg viewBox="0 0 48 48" fill="#fff" aria-hidden="true">'
         '<path d="M6 21h22v-8l14 11-14 11v-8H6z"/>'
         '<circle cx="12" cy="9" r="2.6"/><circle cx="21" cy="6" r="2.1"/>'
         '<circle cx="12" cy="39" r="2.6"/><circle cx="21" cy="42" r="2.1"/>'
         '</svg>')


def icons(s):
    return (s.replace("{paw}", PAW)
             .replace("{tent}", TENT)
             .replace("{arrow}", ARROW))


# ---------------------------------------------------------------- HOME
PAGES["index.html"] = (
    "Cub Scout Pack 3049 | Leo, Indiana",
    "Cub Scout Pack 3049 in Leo, Indiana. Kindergarten through 5th grade boys and girls. Den meetings Mondays at 6:30 PM at Cedar Creek Church.",
    """
<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Leo, Indiana &middot; Pokagon District</span>
    <h1 class="hero__title">
      <span class="hero__pack">Cub Scout Pack 3049</span>
      <span class="hero__tag">Muddy boots. Big ideas. <em>Every Monday.</em></span>
    </h1>
    <p class="lede">Campfires, water rockets, pinewood cars that go way too fast, and 78 kids figuring out what they are capable of. Pack 3049 has been doing this in Leo for more than 90 years. Kindergarten through 5th grade, boys and girls, everybody welcome.</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="register.html">Join the pack</a>
      <a class="btn btn--ghost" href="calendar.html">See what's coming up</a>
    </div>
  </div>
  <svg class="hero__patch" viewBox="0 0 200 200" aria-hidden="true" focusable="false">
    <defs>
      <path id="patch-ring" d="M100,100 m-70,0 a70,70 0 1,1 140,0 a70,70 0 1,1 -140,0"></path>
    </defs>
    <circle cx="100" cy="100" r="96" fill="#ffc93c"></circle>
    <circle cx="100" cy="100" r="90" fill="#123021"></circle>
    <circle cx="100" cy="100" r="86" fill="none" stroke="#ffc93c" stroke-width="2" stroke-dasharray="6 6"></circle>
    <circle cx="100" cy="100" r="63" fill="#1a4530"></circle>
    <circle cx="100" cy="100" r="63" fill="none" stroke="#ff6b35" stroke-width="3"></circle>
    <text fill="#ffc93c" font-family="Space Mono, monospace" font-weight="700" font-size="13" letter-spacing="2">
      <textPath href="#patch-ring" startOffset="0" textLength="440" lengthAdjust="spacingAndGlyphs">CUB SCOUT PACK 3049 &#183; LEO, INDIANA &#183;</textPath>
    </text>
    <path d="M100 56l10.5 17h-6l8.5 14.5h-6L116 104H84l9-16.5h-6L95.5 73h-6z" fill="#ffc93c"></path>
    <rect x="97.5" y="102" width="5" height="9" rx="1.5" fill="#ff6b35"></rect>
    <text x="100" y="131" text-anchor="middle" fill="#7fc49a" font-family="Space Mono, monospace" font-weight="700" font-size="9.5" letter-spacing="1.8">DO YOUR BEST</text>
  </svg>
</section>

<section class="section" data-until="2026-08-31">
  <div class="wrap">
    <div class="bigevent" id="blastoff" data-until="2026-08-31">
      <div class="flyer">
        <figure class="flyer__pin">
          <a href="images/popcorn-blastoff-2026.jpg">
            <img src="images/popcorn-blastoff-2026.jpg" width="1103" height="1426" alt="Pack 3049 Popcorn Blast-Off flyer. A two-liter bottle rocket with red fins and a red nose cone launches through a cloud of popcorn, trailing fire. Cub Scouts Pack 3049, Popcorn Blast-Off. Monday August 31 at 6:30 PM, Cedar Creek Church. Parents talk popcorn. Kids blast off bottle rockets. Class B street clothes. Water rockets and popcorn. Bring an empty two-liter bottle, and an extra for a friend if you have one. Scouts will bring home popcorn Monday to sell.">
          </a>
          <figcaption class="flyer__cap">Tap the flyer to open it full size</figcaption>
        </figure>
        <div>
          <span class="eyebrow" data-event-date="2026-08-31">This Monday</span>
          <h2>Popcorn Blast-Off</h2>
          <p>Popcorn season starts with a bang. While the grown-ups get the rundown on this year's
             sale, the Scouts head outside to build water rockets out of two-liter bottles and launch
             them. Build it, blast it, do it again.</p>
          <div class="bigevent__meta">
            <div><span class="k">When</span><span class="v">Monday, August 31<small>6:30 PM</small></span></div>
            <div><span class="k">Where</span><span class="v">Cedar Creek Church<small>12606 Leo Road, Fort Wayne, IN 46845</small></span></div>
            <div><span class="k">Wear</span><span class="v">Class B<small>Scout T-shirt or regular street clothes</small></span></div>
          </div>
          <h3>Bring an empty two-liter bottle</h3>
          <ul class="checklist checklist--yes">
            <li>One empty two-liter bottle per Scout, that is their rocket</li>
            <li>An extra for a friend if you have one</li>
            <li>Rinse it out, labels can stay on</li>
          </ul>
          <p><strong>Scouts take their popcorn home that night</strong> and can start selling right away.</p>
          <div class="btn-row">
            <a class="btn btn--primary" href="https://maps.google.com/?q=12606+Leo+Rd,+Fort+Wayne,+IN+46845">Get directions</a>
            <a class="btn btn--solid" href="popcorn.html">How the sale works</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="facts">
      <div class="fact"><div class="fact__num">78</div><div class="fact__label">Scouts in the pack</div></div>
      <div class="fact"><div class="fact__num">6</div><div class="fact__label">Dens, kindergarten to 5th grade</div></div>
      <div class="fact"><div class="fact__num">90+</div><div class="fact__label">Years serving Leo families</div></div>
      <div class="fact"><div class="fact__num">#1</div><div class="fact__label">Largest pack in northern Indiana</div></div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="grid grid--2">
      <div>
        <h2>What Cub Scouts actually looks like</h2>
        <p>Most weeks your Scout meets with their den, a small group of kids in the same grade. They build something, play a purposeful game, learn a skill, and work on an adventure toward their rank. It takes about an hour.</p>
        <p>Once a month the whole pack gets together with families for a pack meeting: skits, awards, a theme, and a lot of noise. Between those, we hike, camp, race cars, tour the fire station, launch water rockets, and hand out more than a few pies to the face.</p>
        <p>Scouting is a family program. Parents are not dropping kids off and leaving. You will be right there, and that is most of the point.</p>
        <p><a class="btn btn--solid" href="join.html">How to get started</a></p>
      </div>
      <div>
        <div class="card card--accent">
          <h3>Where and when we meet</h3>
          <p><strong>Den meetings:</strong> Mondays, 6:30 to 7:30 PM<br>
          <strong>Pack meetings:</strong> one Monday a month, 6:30 to 8:00 PM<br>
          <strong>Committee meetings:</strong> Thursdays at 7:00 PM, all adults welcome</p>
          <p><strong><a href="https://cedarcreekchurch.com">Cedar Creek Church</a></strong><br>
          12606 Leo Road, Fort Wayne, IN 46845</p>
          <p class="muted">Dens usually meet two to three times a month. The pack takes off for school breaks and most holidays.</p>
          <p><a href="https://maps.google.com/?q=12606+Leo+Rd,+Fort+Wayne,+IN+46845">Open in maps</a></p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <span class="eyebrow">Six ranks, six years</span>
    <h2>Find your den</h2>
    <p class="muted">Every Scout joins the den that matches the grade they are entering. Each rank has its own handbook, its own adventures, and its own patch to sew on.</p>
    <div class="patch-row">
      <figure class="patch">
        <div class="patch__disc" style="--rank:#f2a516">{paw}</div>
        <span class="patch__grade">Kindergarten</span>
        <div class="patch__name">Lions</div>
        <p class="patch__note">Short meetings, a grown up at every one, and a whole lot of firsts.</p>
      </figure>
      <figure class="patch">
        <div class="patch__disc" style="--rank:#ef6c1a">{paw}</div>
        <span class="patch__grade">1st grade</span>
        <div class="patch__name">Tigers</div>
        <p class="patch__note">Exploring the neighborhood and meeting the people who run it.</p>
      </figure>
      <figure class="patch">
        <div class="patch__disc" style="--rank:#cf3a2c">{paw}</div>
        <span class="patch__grade">2nd grade</span>
        <div class="patch__name">Wolves</div>
        <p class="patch__note">Outdoor skills, and the first real taste of doing it themselves.</p>
      </figure>
      <figure class="patch">
        <div class="patch__disc" style="--rank:#2e7fb8">{paw}</div>
        <span class="patch__grade">3rd grade</span>
        <div class="patch__name">Bears</div>
        <p class="patch__note">Tools, camp cooking, critters. Bears run the pumpkin contest.</p>
      </figure>
      <figure class="patch">
        <div class="patch__disc" style="--rank:#3f8f5f">{tent}</div>
        <span class="patch__grade">4th grade</span>
        <div class="patch__name">Webelos</div>
        <p class="patch__note">Camping gets serious and Scouts start running things themselves.</p>
      </figure>
      <figure class="patch">
        <div class="patch__disc" style="--rank:#1a4530">{arrow}</div>
        <span class="patch__grade">5th grade</span>
        <div class="patch__name">Arrow of Light</div>
        <p class="patch__note">The highest Cub Scout rank, and the bridge into a Scouts BSA troop.</p>
      </figure>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <span class="eyebrow">Science by way of getting filthy</span>
    <h2>The STEM is the fun part</h2>
    <p class="muted" style="max-width:62ch">Nobody in this pack calls it STEM. They call it launching a bottle rocket over the parking lot, or figuring out why the fast car is fast. Same thing.</p>
    <div class="grid grid--3">
      <div class="card card--stem">
        <h3>Water rockets and launch day</h3>
        <p>Air pressure, fins, water volume, and a lot of arguing about whose design goes higher. Then they change one variable and try again. That is an experiment, and they never notice.</p>
      </div>
      <div class="card card--stem">
        <h3>Pinewood Derby physics</h3>
        <p>A block of pine, four wheels, and a hard cap on weight. Scouts learn about friction, mass, and center of gravity by losing a heat and figuring out why.</p>
      </div>
      <div class="card card--stem">
        <h3>Nature, up close</h3>
        <p>Tracks in the mud at Metea Park, water bugs in a creek, constellations from the campsite. Field science, done in the field.</p>
      </div>
      <div class="card card--stem">
        <h3>Build it and use it</h3>
        <p>Knots that hold, fires that light, a pocket knife used correctly, a meal cooked over coals. Practical engineering with immediate consequences.</p>
      </div>
      <div class="card card--stem">
        <h3>Nova awards</h3>
        <p>Scouting America's own STEM program. Scouts who want to go deeper earn Nova awards in science, technology, engineering, and math.</p>
      </div>
      <div class="card card--stem">
        <h3>Fix the thing that broke</h3>
        <p>Tents in the wind, a wheel that wobbles, a plan that fell apart at 9 PM. Troubleshooting under real pressure is the most underrated skill Scouting teaches.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--pine">
  <div class="wrap">
    <span class="eyebrow">The long game</span>
    <h2>What they actually walk away with</h2>
    <div class="grid grid--4" style="margin-top:1.75rem">
      <div class="card"><h3>Nerve</h3><p>Knocking on a stranger's door to sell popcorn is terrifying at seven. It is not at nine.</p></div>
      <div class="card"><h3>Leadership</h3><p>By Webelos they are running den meetings, teaching younger Scouts, and leading a flag ceremony in front of a hundred people.</p></div>
      <div class="card"><h3>Grit</h3><p>Rain on the campout. Losing the derby. Do Your Best is not a participation trophy, it is a standard you hold yourself to.</p></div>
      <div class="card"><h3>Service</h3><p>Food drives, park cleanups, flags on veterans' graves. Kids learn that a community is something you maintain.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <span class="eyebrow">The calendar</span>
    <h2>A year in Pack 3049</h2>
    <div class="grid grid--4">
      <div class="card"><h3>Fall</h3><p>Recruitment night, the popcorn sale, a pack hike at Metea Park, the corn maze, and the fall carnival with the Bears' pumpkin contest.</p></div>
      <div class="card"><h3>Winter</h3><p>Pack camp-in at the church, the pie in the face pack meeting, crossover, and the Pinewood Derby.</p></div>
      <div class="card"><h3>Spring</h3><p>Blue and Gold banquet, rank advancement, service projects, and getting back outside the second the weather allows.</p></div>
      <div class="card"><h3>Summer</h3><p>Resident camp at Camp Chief Little Turtle, day camp, the Grabill Days parade, and pack picnics.</p></div>
    </div>
    <p class="center" style="margin-top:2rem"><a class="btn btn--solid" href="calendar.html">See the full calendar</a></p>
  </div>
</section>

<section class="section section--pine">
  <div class="narrow">
    <span class="eyebrow">What we say out loud</span>
    <h2>The Scout Oath</h2>
    <p class="oath">On my honor I will do my best<br>
    To do my duty to God and my country and to obey the Scout Law;<br>
    To help other people at all times;<br>
    To keep myself physically strong, mentally awake, and morally straight.</p>
    <h2 style="margin-top:2.5rem">The Scout Law</h2>
    <p>A Scout is trustworthy, loyal, helpful, friendly, courteous, kind, obedient, cheerful, thrifty, brave, clean, and reverent.</p>
    <h2 style="margin-top:2.5rem">The Cub Scout motto</h2>
    <p class="motto">Do Your Best.</p>
    <p class="muted">You will hear those three words constantly around here. It is the whole standard. Not win, not be the best. Just do your best.</p>
  </div>
</section>

<section class="section section--tint">
  <div class="narrow center">
    <h2>Come see for yourself</h2>
    <p>New families are welcome any time of year, not just in the fall. Show up on a Monday, say hello, and let your kid try a den meeting before you decide anything. Call or text either Cubmaster with any question at all.</p>
    <div class="contacts">
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Nicole Howard</div>
        <a href="tel:+12605572243">(260) 557-2243</a>
        <a href="mailto:howardfamily411@gmail.com">howardfamily411@gmail.com</a>
      </div>
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Dan Noll</div>
        <a href="tel:+12606025134">(260) 602-5134</a>
        <a href="mailto:steelers6615@gmail.com">steelers6615@gmail.com</a>
      </div>
    </div>
    <div class="btn-row">
      <a class="btn btn--primary" href="register.html">Register your Scout</a>
      <a class="btn btn--solid" href="calendar.html">See the calendar</a>
    </div>
  </div>
</section>
""".replace("{paw}", PAW).replace("{tent}", TENT).replace("{arrow}", ARROW),
)

# ---------------------------------------------------------------- JOIN
PAGES["join.html"] = (
    "Join Pack 3049 | Cub Scouts in Leo, Indiana",
    "How to join Cub Scout Pack 3049 in Leo, Indiana: who can join, when we meet, what it costs, and what to expect at your first meeting.",
    """
<section class="hero hero--page">
  <div class="wrap">
    <span class="eyebrow">Join us</span>
    <h1>So you're thinking about it</h1>
    <p class="lede">No experience required, from you or your Scout. Show up on a Monday and we will take it from there.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid--2">
      <div class="card card--accent">
        <h3>Who can join</h3>
        <p>Any child in kindergarten through 5th grade. Boys and girls both, in the same pack. Dens are organized by grade, and Cub Scouting is a family program, so siblings and parents are part of nearly everything we do.</p>
      </div>
      <div class="card card--accent">
        <h3>When we meet</h3>
        <p><strong>Mondays at 6:30 PM</strong> during the school year at <a href="https://cedarcreekchurch.com">Cedar Creek Church</a>, 12606 Leo Road, Fort Wayne, IN 46845. Dens meet two to three times a month, and the whole pack meets together once a month. We take school breaks and holidays off.</p>
      </div>
      <div class="card card--accent">
        <h3>What to wear the first time</h3>
        <p>Nothing special. Come in regular clothes. Once you have joined we will help you sort out the uniform, and the pack often has gently used shirts available before you buy anything new.</p>
      </div>
      <div class="card card--accent">
        <h3>Can we join mid year?</h3>
        <p>Yes. Most families join in August or September, but Scouts join in January, in March, and everywhere in between. Your Scout will catch up on adventures with their den.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <span class="eyebrow">Three steps, that's it</span>
    <h2>How to join</h2>
    <div class="trail" style="margin-top:2.5rem">
      <div class="card"><h3>Come to a meeting</h3><p>Email us or just show up on a Monday at 6:30 PM. Meet the leaders, meet the other families, and let your Scout try a den meeting before committing to anything.</p></div>
      <div class="card"><h3>Register online</h3><p>The whole thing is one form on your phone, about five minutes, and nothing is due that day. <a href="register.html">Start the application here.</a></p></div>
      <div class="card"><h3>Get set up</h3><p>We will point you to the right handbook, the right den, the uniform, and our BAND app and Facebook group so you never miss an announcement.</p></div>
    </div>
    <div class="bigevent" id="kickoff" data-until="2026-08-24">
      <div class="flyer">
        <figure class="flyer__pin">
          <a href="images/scouting-kickoff-2026.jpg">
            <img src="images/scouting-kickoff-2026.jpg" width="1102" height="1427" alt="Pack 3049 Scouting Kick-Off flyer. A large Cub Scouts paw print holds four messages: Make an Impact, Grow Together, Create Memories, and Explore More. You are invited to the Scouting Kick-Off. Adventure, friendship, character, fun. Monday August 24, 6:30 to 8:00 PM at Riverside Gardens Park, 14701 Schwartz Rd, Grabill, IN 46741. Games and activities, Scout Shop, food and treats, meet leaders and families, and much more. Bring the whole family. Pack 3049, Leo, Indiana, with the Lion, Tiger, Wolf, Bear, Webelos, and Arrow of Light rank badges along the bottom.">
          </a>
          <figcaption class="flyer__cap">Tap the flyer to open it full size</figcaption>
        </figure>
        <div>
          <span class="eyebrow">You're invited</span>
          <h2>Scouting Kick-Off</h2>
          <p>Kick off a great year of Scouting with Pack 3049. Every Scout and every family is invited, and so is anyone who is simply curious. Come see what a year with us looks like, meet the leaders and the other families, and sign up on the spot if it feels right.</p>
          <div class="bigevent__meta">
            <div><span class="k">When</span><span class="v">Monday, August 24<small>6:30 to 8:00 PM</small></span></div>
            <div><span class="k">Where</span><span class="v">Riverside Gardens Park<small>14701 Schwartz Rd, Grabill, IN 46741</small></span></div>
          </div>
          <h3>What's there</h3>
          <ul class="checklist checklist--yes">
            <li>Games and activities</li>
            <li>Scout Shop on site</li>
            <li>Food and treats</li>
            <li>Meet leaders and families</li>
            <li>Sign up for the year</li>
            <li>And much more</li>
          </ul>
          <p><strong>Bring the whole family.</strong> Free to attend, and you can register that night.</p>
          <div class="btn-row">
            <a class="btn btn--primary" href="https://maps.google.com/?q=14701+Schwartz+Rd,+Grabill,+IN+46741">Get directions</a>
            <a class="btn btn--solid" href="register.html">Register your Scout</a>
          </div>
        </div>
      </div>
      <h3 style="margin-top:2rem">Questions? Contact us</h3>
      <div class="contacts">
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Nicole Howard</div>
        <a href="tel:+12605572243">(260) 557-2243</a>
        <a href="mailto:howardfamily411@gmail.com">howardfamily411@gmail.com</a>
      </div>
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Dan Noll</div>
        <a href="tel:+12606025134">(260) 602-5134</a>
        <a href="mailto:steelers6615@gmail.com">steelers6615@gmail.com</a>
      </div>
    </div>
    </div>
    <div class="callout callout--info" style="margin-top:1.75rem">
      <p><strong>Missed it? That is completely fine.</strong> The kick-off is our one big recruiting night of the year, but families join Pack 3049 in October, in January, and everywhere in between. Just <a href="contact.html">reach out</a> or come to a Monday meeting.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <span class="eyebrow">The honest version</span>
    <h2>What it costs</h2>

    <div class="bigevent" style="margin-bottom:2.25rem">
      <div class="grid grid--2" style="align-items:center">
        <div>
          <div class="fact__num" style="font-size:clamp(3rem,2rem+4vw,4.6rem)">$100</div>
          <p style="font-size:1.15rem;margin-top:.4rem"><strong>Per Scout, per year.</strong> That is registration in Pack 3049 for a full year of Scouting.</p>
          <ul class="checklist checklist--yes">
            <li><strong>Sibling discounts</strong> for families with more than one Scout</li>
            <li><strong>Leader discounts</strong> for registered adult volunteers</li>
            <li>Financial assistance whenever a family needs it</li>
          </ul>
        </div>
        <div>
          <div class="card">
            <h3>What $100 a year actually buys</h3>
            <p>Roughly <strong>30 meetings and events</strong> between August and May, plus everything the pack hands out along the way. That works out to <strong>under $3 a week</strong> during the school year.</p>
            <p class="muted">A season of most youth sports costs more than that, runs three months instead of ten, and does not include a campout.</p>
          </div>
        </div>
      </div>
    </div>

    <h3>Where the money goes</h3>
    <p>We would rather show you than ask you to trust us. Here is every piece of it.</p>
    <div class="table-scroll">
      <table>
        <caption class="visually-hidden">Where Cub Scout money goes</caption>
        <thead><tr><th scope="col">Where it goes</th><th scope="col">Amount</th><th scope="col">What it pays for</th></tr></thead>
        <tbody>
          <tr><td>Scouting America national registration</td><td>$85 per year</td><td>National membership, liability insurance, and program support. This is not ours and we cannot discount it.</td></tr>
          <tr><td>Anthony Wayne Area Council fee</td><td>Set each year by council</td><td>Local camps, leader training, district events, and the Scout Shop</td></tr>
          <tr><td><em>Scout Life</em> magazine</td><td>$15 per year, optional</td><td>The Scout magazine, mailed to your house</td></tr>
          <tr><td><strong>Everything the pack does</strong></td><td><strong>Covered by popcorn</strong></td><td>Rank badges and adventure loops, the neckerchief slide every Scout gets at Blue and Gold, the haunted corn maze, pinewood derby cars, craft and activity supplies, campfire wood, pack camping gear, awards, and the Blue and Gold banquet itself</td></tr>
          <tr><td>Uniform</td><td>One time, then it lasts</td><td>Shirt, neckerchief, slide, and handbook from the Scout Shop. Ask us first, the pack usually has used shirts to hand down.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="alert">
      <h3>The part nobody tells you</h3>
      <p><strong>The pack loses money on every registration.</strong> Look at that table again: the $85 national fee plus the council fee already adds up to more than the $100 you pay us, and that is before a single rank badge, derby car, or bag of marshmallows.</p>
      <p>Every award your Scout earns, every activity we run, and every slide handed out at Blue and Gold is paid for by <a href="popcorn.html">the popcorn sale</a>, not by your registration check. That is the whole reason we sell.</p>
    </div>

    <div class="callout">
      <p><strong>And most families do not pay the program cost out of pocket either.</strong> A Scout who reaches the pack sales goal has covered their year, and one who sells $1,600 earns free summer camp at CCLT on top of it. Families who would rather not sell can take the buyout or the calendar fundraiser instead.</p>
    </div>
    <div class="callout callout--info">
      <p><strong>Cost should never be the reason a kid misses out.</strong> Financial assistance is available, the conversation stays between you and a pack leader, and nobody else finds out. Just ask.</p>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <h2>The uniform</h2>
    <div class="grid grid--2">
      <div>
        <p>Cub Scouts wear two kinds of uniform. The <strong>Class A</strong> is the official blue Cub Scout shirt with the neckerchief and slide, worn for pack meetings, ceremonies, camp dinners, and anywhere we represent the pack in public. Lions through Bears wear the blue shirt. Webelos and Arrow of Light Scouts may move to the tan shirt.</p>
        <p>The <strong>Class B</strong> is simply a pack T shirt or any plain T shirt, worn for hikes, work days, camp activities, and most of what we do outdoors.</p>
        <p>Buy Class A pieces at the Anthony Wayne Scout Shop. Take your Scout with you so the shirt gets fitted, and ask us first, because the pack often has used shirts and neckerchiefs to pass along.</p>
      </div>
      <div class="card card--accent">
        <h3>Anthony Wayne Scout Shop</h3>
        <p>8315 W. Jefferson Boulevard<br>Fort Wayne, IN 46804</p>
        <p><a href="tel:+12604329593">(260) 432-9593</a></p>
        <p><strong>Hours:</strong><br>
        Monday to Friday, 8:30 AM to 5:00 PM<br>
        Saturday, 9:00 AM to 1:00 PM</p>
        <p class="muted">Same building as the council service center. Call ahead if you need a specific size or a rank specific item.</p>
        <p><a href="https://www.awac.org/">awac.org</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="narrow center">
    <h2>Still have questions?</h2>
    <p>The <a href="faq.html">parent FAQ</a> covers the ones we hear most. Anything else, call, text, or email either Co-Cubmaster.</p>
    <div class="contacts">
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Nicole Howard</div>
        <a href="tel:+12605572243">(260) 557-2243</a>
        <a href="mailto:howardfamily411@gmail.com">howardfamily411@gmail.com</a>
      </div>
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Dan Noll</div>
        <a href="tel:+12606025134">(260) 602-5134</a>
        <a href="mailto:steelers6615@gmail.com">steelers6615@gmail.com</a>
      </div>
    </div>
  </div>
</section>
""".replace("{facebook}", FACEBOOK),
)

# ---------------------------------------------------------------- CALENDAR
PAGES["calendar.html"] = (
    "Calendar | Cub Scout Pack 3049",
    "The full Fall 2026 schedule for Cub Scout Pack 3049: den meetings, pack meetings, committee meetings, the Scouting Kick-Off, popcorn, parade, hike, and crossover, with dates, times, and locations.",
    """
<section class="hero hero--page">
  <div class="wrap">
    <span class="eyebrow">Calendar</span>
    <h1>Fall 2026, start to finish</h1>
    <p class="lede">Every den meeting, pack meeting, committee meeting, and event from August through the first meeting of the new year. Print it, screenshot it, put it on the fridge.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>The weekly rhythm</h2>
    <div class="grid grid--3">
      <div class="card card--accent">
        <h3>Den meetings</h3>
        <p><strong>Mondays, 6:30 to 7:30 PM</strong><br>Cedar Creek Church</p>
        <p class="muted">Your Scout's grade level group. Roughly one hour, two or three Mondays a month.</p>
      </div>
      <div class="card card--accent">
        <h3>Pack meetings</h3>
        <p><strong>One Monday a month, 6:30 to 7:30 or 8:00 PM</strong><br>Usually Cedar Creek Church</p>
        <p class="muted">Families come too. Awards, a theme, and a lot of noise. Some are offsite, so check the location.</p>
      </div>
      <div class="card card--accent">
        <h3>Committee meetings</h3>
        <p><strong>Thursdays, 7:00 PM</strong><br>Cedar Creek Church</p>
        <p class="muted">All adults welcome, always. This is where the year actually gets planned.</p>
      </div>
    </div>
    <div class="callout callout--info">
      <p>Schedules move and weather happens. Changes go out through the <a href="{band}">BAND app</a> and the <a href="{facebook}">Facebook group</a> before they reach this page.</p>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <span class="eyebrow">August 2026</span>
    <h2>August</h2>
    <div class="table-scroll">
      <table>
        <caption class="visually-hidden">August 2026 schedule</caption>
        <thead><tr><th scope="col">Date</th><th scope="col">Time</th><th scope="col">Event</th><th scope="col">Where</th></tr></thead>
        <tbody>
          <tr data-date="2026-08-06"><td>Thu, Aug 6</td><td>4:15 PM</td><td>Cedarville kindergarten recruitment</td><td>Cedarville Elementary School</td></tr>
          <tr data-date="2026-08-10"><td>Mon, Aug 10</td><td>4:15 PM</td><td>Cedarville 1st to 3rd grade recruitment</td><td>Cedarville Elementary School</td></tr>
          <tr data-date="2026-08-20"><td>Thu, Aug 20</td><td>7:00 PM</td><td>August committee meeting</td><td>Cedar Creek Church</td></tr>
          <tr data-date="2026-08-24"><td><strong>Mon, Aug 24</strong></td><td><strong>6:30 to 8:00 PM</strong></td><td><strong>Scouting Kick-Off</strong><br>Registration, games, food, and the Scout Shop on site. Bring the whole family.</td><td>Riverside Gardens Park<br>14701 Schwartz Rd, Grabill</td></tr>
          <tr data-date="2026-08-31"><td>Mon, Aug 31</td><td>6:30 PM</td><td><strong>August pack meeting:</strong> Popcorn Kick-Off and water rockets<br><span class="evt-flag">Setup and cleanup: Arrow of Light</span></td><td>Cedar Creek Church<br>12606 Leo Rd, Fort Wayne</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <span class="eyebrow">September 2026</span>
    <h2>September</h2>
    <div class="table-scroll">
      <table>
        <caption class="visually-hidden">September 2026 schedule</caption>
        <thead><tr><th scope="col">Date</th><th scope="col">Time</th><th scope="col">Event</th><th scope="col">Where</th></tr></thead>
        <tbody>
          <tr data-date="2026-09-07"><td>Mon, Sep 7</td><td></td><td class="muted">No Cub Scouts, Labor Day</td><td></td></tr>
          <tr data-date="2026-09-10"><td>Thu, Sep 10</td><td>7:00 PM</td><td>September committee meeting</td><td>Cedar Creek Church</td></tr>
          <tr data-date="2026-09-12"><td>Sat, Sep 12</td><td>9:30 AM</td><td>Grabill County Fair Parade</td><td>Downtown Grabill, lineup details on BAND</td></tr>
          <tr data-date="2026-09-14"><td>Mon, Sep 14</td><td></td><td class="muted">No Cub Scouts, EACS in-service day</td><td></td></tr>
          <tr data-date="2026-09-21"><td>Mon, Sep 21</td><td>6:30 PM</td><td><strong>1st den meeting:</strong> Bobcat adventure</td><td>Cedar Creek Church</td></tr>
          <tr data-date="2026-09-28"><td>Mon, Sep 28</td><td>6:30 PM</td><td><strong>September pack meeting:</strong> Safety Day and bike rodeo</td><td>Safety Village<br>1270 S Phoenix Parkway, Fort Wayne</td></tr>
        </tbody>
      </table>
    </div>
    <p class="muted">Bring a bike and a helmet to the September pack meeting.</p>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <span class="eyebrow">October 2026</span>
    <h2>October</h2>
    <div class="table-scroll">
      <table>
        <caption class="visually-hidden">October 2026 schedule</caption>
        <thead><tr><th scope="col">Date</th><th scope="col">Time</th><th scope="col">Event</th><th scope="col">Where</th></tr></thead>
        <tbody>
          <tr data-date="2026-10-05"><td>Mon, Oct 5</td><td>6:30 PM</td><td><strong>2nd den meeting:</strong> fall hike, The Great Outdoors</td><td>Metea County Park<br>8401 Union Chapel Rd, Fort Wayne</td></tr>
          <tr data-date="2026-10-08"><td>Thu, Oct 8</td><td>7:00 PM</td><td>October committee meeting</td><td>Cedar Creek Church</td></tr>
          <tr data-date="2026-10-12"><td>Mon, Oct 12</td><td></td><td class="muted">No Cub Scouts, fall break</td><td></td></tr>
          <tr data-date="2026-10-19"><td>Mon, Oct 19</td><td>6:30 PM</td><td><strong>3rd den meeting:</strong> Fitness Fun</td><td>Cedar Creek Church</td></tr>
          <tr data-date="2026-10-26"><td>Mon, Oct 26</td><td>6:30 PM</td><td><strong>October pack meeting:</strong> Fall Family Fun</td><td>Cedar Creek Produce<br>11709 Clay St, Leo-Cedarville, IN 46765</td></tr>
        </tbody>
      </table>
    </div>
    <div class="callout">
      <p><strong>Popcorn return day is Friday, October 23.</strong> Unsold product goes back to council by noon, so get anything you are not going to sell to the popcorn kernel before then.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <span class="eyebrow">November 2026</span>
    <h2>November</h2>
    <div class="table-scroll">
      <table>
        <caption class="visually-hidden">November 2026 schedule</caption>
        <thead><tr><th scope="col">Date</th><th scope="col">Time</th><th scope="col">Event</th><th scope="col">Where</th></tr></thead>
        <tbody>
          <tr data-date="2026-11-02"><td>Mon, Nov 2</td><td></td><td class="muted">No Cub Scouts, EACS in-service day</td><td></td></tr>
          <tr data-date="2026-11-05"><td>Thu, Nov 5</td><td>7:00 PM</td><td>November committee meeting</td><td>Cedar Creek Church</td></tr>
          <tr data-date="2026-11-09"><td>Mon, Nov 9</td><td>6:30 PM</td><td><strong>4th den meeting:</strong> Cubservation</td><td>Cedar Creek Church</td></tr>
          <tr data-date="2026-11-16"><td>Mon, Nov 16</td><td>6:30 PM</td><td><strong>5th den meeting:</strong> Call for Citizenship</td><td>Watch BAND for the location</td></tr>
          <tr data-date="2026-11-23"><td>Mon, Nov 23</td><td>6:30 PM</td><td><strong>November pack meeting:</strong> STEM Day and intro to the Pinewood Derby<br><span class="evt-flag">Setup and cleanup: Wolves. Flag ceremony: Bears.</span></td><td>Cedar Creek Church</td></tr>
          <tr data-date="2026-11-30"><td>Mon, Nov 30</td><td></td><td class="muted">No Cub Scouts, extended Thanksgiving break</td><td></td></tr>
        </tbody>
      </table>
    </div>
    <div class="callout">
      <p><strong>The popcorn sale ends Wednesday, November 25.</strong> All money and order forms are due. See the <a href="popcorn.html">popcorn page</a>.</p>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <span class="eyebrow">December 2026 and January 2027</span>
    <h2>December, then the break</h2>
    <div class="table-scroll">
      <table>
        <caption class="visually-hidden">December 2026 and January 2027 schedule</caption>
        <thead><tr><th scope="col">Date</th><th scope="col">Time</th><th scope="col">Event</th><th scope="col">Where</th></tr></thead>
        <tbody>
          <tr data-date="2026-12-03"><td>Thu, Dec 3</td><td>7:00 PM</td><td>December committee meeting</td><td>Cedar Creek Church</td></tr>
          <tr data-date="2026-12-07"><td>Mon, Dec 7</td><td>6:30 PM</td><td><strong>6th den meeting:</strong> Camping Essentials</td><td>Cedar Creek Church</td></tr>
          <tr data-date="2026-12-14"><td>Mon, Dec 14</td><td>6:30 PM</td><td><strong>December pack meeting:</strong> awards and Arrow of Light crossover<br><span class="evt-flag">Setup and cleanup: Lions. Flag ceremony: Arrow of Light.</span></td><td>Cedar Creek Church</td></tr>
          <tr data-date="2026-12-21"><td>Mon, Dec 21</td><td></td><td class="muted">No Cub Scouts, winter break</td><td></td></tr>
          <tr data-date="2026-12-28"><td>Mon, Dec 28</td><td></td><td class="muted">No Cub Scouts, winter break</td><td></td></tr>
          <tr data-date="2027-01-04"><td>Mon, Jan 4</td><td></td><td class="muted">No Cub Scouts, winter break</td><td></td></tr>
          <tr data-date="2027-01-11"><td>Mon, Jan 11</td><td>6:30 PM</td><td><strong>First den meeting of the new year</strong></td><td>Cedar Creek Church</td></tr>
        </tbody>
      </table>
    </div>
    <p class="muted">The spring calendar, including the Pinewood Derby and the Blue and Gold banquet, is published after the winter break.</p>
  </div>
</section>

<section class="section section--pine">
  <div class="wrap">
    <span class="eyebrow">Know before you go</span>
    <h2>Where everything happens</h2>
    <div class="grid grid--3">
      <div class="card">
        <h3>Cedar Creek Church</h3>
        <p>12606 Leo Road<br>Fort Wayne, IN 46845</p>
        <p class="muted">Our home church. Most den meetings, most pack meetings, and every committee meeting.</p>
        <p><a href="https://maps.google.com/?q=12606+Leo+Rd,+Fort+Wayne,+IN+46845">Directions</a></p>
      </div>
      <div class="card">
        <h3>Riverside Gardens Park</h3>
        <p>14701 Schwartz Road<br>Grabill, IN 46741</p>
        <p class="muted">The Scouting Kick-Off on August 24.</p>
        <p><a href="https://maps.google.com/?q=14701+Schwartz+Rd,+Grabill,+IN+46741">Directions</a></p>
      </div>
      <div class="card">
        <h3>Safety Village</h3>
        <p>1270 S Phoenix Parkway<br>Fort Wayne, IN</p>
        <p class="muted">September pack meeting, Safety Day and bike rodeo. Bring a bike and a helmet.</p>
        <p><a href="https://maps.google.com/?q=1270+S+Phoenix+Parkway,+Fort+Wayne,+IN">Directions</a></p>
      </div>
      <div class="card">
        <h3>Metea County Park</h3>
        <p>8401 Union Chapel Road<br>Fort Wayne, IN 46845</p>
        <p class="muted">The October 5 fall hike. Dress for the weather and the mud.</p>
        <p><a href="https://maps.google.com/?q=8401+Union+Chapel+Rd,+Fort+Wayne,+IN+46845">Directions</a></p>
      </div>
      <div class="card">
        <h3>Cedar Creek Produce</h3>
        <p>11709 Clay Street<br>Leo-Cedarville, IN 46765</p>
        <p class="muted">October pack meeting, Fall Family Fun.</p>
        <p><a href="https://maps.google.com/?q=11709+Clay+St,+Leo-Cedarville,+IN+46765">Directions</a></p>
      </div>
      <div class="card">
        <h3>Cedarville Elementary</h3>
        <p>12225 Hardisty Road<br>Fort Wayne, IN 46845</p>
        <p class="muted">Where our August recruitment visits happen. Not a regular meeting location.</p>
        <p><a href="https://maps.google.com/?q=12225+Hardisty+Rd,+Fort+Wayne,+IN+46845">Directions</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid--2">
      <div>
        <span class="eyebrow">Den duties this fall</span>
        <h2>Who is on deck</h2>
        <p>Every pack meeting needs a den to set up and tear down, and one to run the flag ceremony. It is a ten minute job and it teaches the Scouts more than you would expect.</p>
        <div class="rows">
          <div><span class="k">Aug 31</span><span class="v">Setup and cleanup: <strong>Arrow of Light</strong></span></div>
          <div><span class="k">Sep 28</span><span class="v">No assignment, offsite at Safety Village</span></div>
          <div><span class="k">Oct 26</span><span class="v">No assignment, offsite at Cedar Creek Produce</span></div>
          <div><span class="k">Nov 23</span><span class="v">Setup and cleanup: <strong>Wolves</strong><br>Flag ceremony: <strong>Bears</strong></span></div>
          <div><span class="k">Dec 14</span><span class="v">Setup and cleanup: <strong>Lions</strong><br>Flag ceremony: <strong>Arrow of Light</strong></span></div>
        </div>
      </div>
      <div>
        <span class="eyebrow">Mark these off</span>
        <h2>Mondays with no Cub Scouts</h2>
        <ul class="checklist">
          <li>September 7, Labor Day</li>
          <li>September 14, EACS in-service day</li>
          <li>October 12, fall break</li>
          <li>November 2, EACS in-service day</li>
          <li>November 30, extended Thanksgiving break</li>
          <li>December 21, winter break</li>
          <li>December 28, winter break</li>
          <li>January 4, winter break</li>
        </ul>
        <div class="callout callout--info">
          <p>Scouting picks back up <strong>Monday, January 11</strong> at 6:30 PM.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="narrow center">
    <h2>Never miss a change</h2>
    <p>Den leaders post reminders and last minute changes in the BAND app first. That is where a weather cancellation shows up.</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="{band}">Join us on BAND</a>
      <a class="btn btn--solid" href="{facebook}">Facebook group</a>
    </div>
    <div class="contacts">
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Nicole Howard</div>
        <a href="tel:+12605572243">(260) 557-2243</a>
        <a href="mailto:howardfamily411@gmail.com">howardfamily411@gmail.com</a>
      </div>
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Dan Noll</div>
        <a href="tel:+12606025134">(260) 602-5134</a>
        <a href="mailto:steelers6615@gmail.com">steelers6615@gmail.com</a>
      </div>
    </div>
  </div>
</section>
""".replace("{band}", BAND).replace("{facebook}", FACEBOOK),
)

# ---------------------------------------------------------------- POPCORN
PAGES["popcorn.html"] = (
    "Popcorn Fundraiser | Cub Scout Pack 3049",
    "How the Pack 3049 popcorn sale works: this season's dates, the full product list and prices, the four ways to sell, storefront shifts, Square card payments, free camp at $1,600, the Winner's Circle Club at $3,000, and a script for your Scout.",
    """
<section class="hero hero--page">
  <div class="wrap">
    <span class="eyebrow">Our one fundraiser</span>
    <h1>Popcorn pays for all of it</h1>
    <p class="lede">One sale, one season, and it funds nearly everything the pack does. Five straight years first in council. Here is exactly how it works.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid--2">
      <div>
        <span class="eyebrow">Start here</span>
        <h2>Everything costs money</h2>
        <p>Badges, belt loops, pinewood derby cars, campfire wood, pack camping gear, the Blue and Gold banquet, awards, craft supplies, and the pack's share of camp. It adds up to a real annual budget, and it works out to roughly <strong>$200 of programming per Scout, per year</strong>.</p>
        <p>Pack 3049 runs one fundraiser to cover all of it. That is deliberate. No wrapping paper in October, no cookie dough in February, no candy bars in the spring. Sell popcorn once, then spend the rest of the year actually doing Scouting.</p>
        <p><strong>A Scout who hits the pack sales goal has paid for their year.</strong> Sell past it and you build camp credit.</p>
      </div>
      <div>
        <div class="card card--accent">
          <h3>The math, plainly</h3>
          <div class="rows">
            <div><span class="k">Per Scout</span><span class="v">About $200 of program</span></div>
            <div><span class="k">Sales goal</span><span class="v">$525 per Scout<small>Covers their year</small></span></div>
            <div><span class="k">Free camp at</span><span class="v">$1,600<small>One session at CCLT, fully paid</small></span></div>
            <div><span class="k">Winner's Circle at</span><span class="v">$3,000<small>Pick a laptop, a TV, a 3D printer, and more</small></span></div>
            <div><span class="k">Scout keeps</span><span class="v">4 percent<small>Amazon gift card on their own sales</small></span></div>
            <div><span class="k">Pack keeps</span><span class="v">Up to 38 cents of every dollar</span></div>
            <div><span class="k">Online</span><span class="v">35 percent, and no product to haul</span></div>
          </div>
          <p class="muted" style="margin-top:1rem">Commission climbs with training, growth over last year, and total volume. Every one of those is something the pack earns together.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--pine">
  <div class="wrap">
    <span class="eyebrow">Proven success</span>
    <h2>Five years, first in council</h2>
    <div class="table-scroll">
      <table>
        <caption class="visually-hidden">Pack 3049 popcorn sales by year</caption>
        <thead><tr><th scope="col">Year</th><th scope="col">Total sales</th><th scope="col">Result</th></tr></thead>
        <tbody>
          <tr><td>2021</td><td>$24,524</td><td>1st in council</td></tr>
          <tr><td>2022</td><td>$49,982</td><td>1st in council</td></tr>
          <tr><td>2023</td><td>$40,000</td><td>1st in council</td></tr>
          <tr><td>2024</td><td>$45,724</td><td>1st in council</td></tr>
          <tr><td><strong>2025</strong></td><td><strong>$64,939</strong></td><td>1st in council, best year on record</td></tr>
        </tbody>
      </table>
    </div>
    <p class="muted">Every dollar of that came from Scouts who were nervous the first time they knocked on a door, and were not by the tenth.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <span class="eyebrow">This season</span>
    <h2>Key dates</h2>
    <div class="grid grid--2">
      <div>
        <ul class="sched">
          <li data-date="2026-08-26"><span class="when">Week of Aug 24</span><span class="what">Popcorn arrives<span class="where">The pack's full season order is delivered. Distribution details go out in BAND.</span></span></li>
          <li data-date="2026-08-31"><span class="when">Mon Aug 31</span><span class="what">Popcorn Kick-Off at the pack meeting<span class="where">Cedar Creek Church, 6:30 PM. Order forms, Square setup, <a href="#storefronts">storefront sign ups</a>, and water rockets.</span></span></li>
          <li data-date="2026-10-23"><span class="when">Fri Oct 23</span><span class="what">Return day<span class="where">Unsold product goes back to council by noon. This is the only return window all season.</span></span></li>
          <li data-date="2026-11-25"><span class="when">Wed Nov 25</span><span class="what">Final sale day<span class="where">All money and order forms due to the popcorn kernel.</span></span></li>
        </ul>
      </div>
      <div>
        <ul class="sched">
          <li data-date="2026-12-04"><span class="when">Fri Dec 4</span><span class="what">Invoice payment due to council</span></li>
          <li data-date="2026-12-07"><span class="when">Mon Dec 7</span><span class="what">Camp credit and Winner's Circle forms due</span></li>
          <li data-date="2026-12-13"><span class="when">Sun Dec 13</span><span class="what">Payouts, and Amazon gift cards to Scouts</span></li>
        </ul>
        <div class="callout">
          <p><strong>Sell early.</strong> The first few weeks are consistently the strongest weeks of the season, every single year. Scouts who start on day one almost always finish first, and they finish sooner.</p>
        </div>
        <div class="callout callout--info">
          <p><strong>Three numbers to remember:</strong> <strong>$525</strong> pays for your Scout's year, <strong>$1,600</strong> earns them free summer camp at CCLT, and <strong>$3,000</strong> gets them into the Winner's Circle Club. Everything they sell also earns 4 percent back as an Amazon gift card.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <span class="eyebrow">Pick your lane</span>
    <h2>Four ways to sell</h2>
    <div class="grid grid--4">
      <div class="card card--accent">
        <h3>Show and sell</h3>
        <p>Set up in a high traffic spot with product in hand. The pack buys inventory up front, so your Scout hands a bag over the moment someone buys.</p>
      </div>
      <div class="card card--accent">
        <h3>Show and deliver</h3>
        <p>Take popcorn door to door and sell it on the spot. No waiting, no second trip, no order forms to chase down later.</p>
      </div>
      <div class="card card--accent">
        <h3>Take order</h3>
        <p>The traditional way. Go door to door with the order form, then deliver after the sale closes. Good for Scouts who would rather not haul a wagon.</p>
      </div>
      <div class="card card--accent">
        <h3>Online</h3>
        <p>Your Scout gets a personal link to send to family anywhere in the country. Ships direct from PRP, free shipping, and it still counts toward their total.</p>
      </div>
    </div>

    <div class="grid grid--2" style="margin-top:2rem">
      <div class="card">
        <h3>Storefront shifts</h3>
        <p>The pack books shifts at local stores through the council, and you sign up for the ones that fit your family.</p>
        <ul class="checklist checklist--yes">
          <li>Book up to 14 days in advance</li>
          <li>Two hour shifts</li>
          <li>Pick your location</li>
          <li>Reserve your time</li>
        </ul>
        <p class="muted">Two Scouts and two registered adults per shift, Class A uniform. Shifts fill fast, so grab them the day they open. <a href="#storefronts">Book one below.</a></p>
      </div>
      <div class="card">
        <h3>Taking cards with Square</h3>
        <p>The pack runs card sales through <strong>Square</strong>, same as last year, so nobody has to turn down a customer who is not carrying cash. In practice that is most customers.</p>
        <p>Your den leader gets you set up at the kick-off. If Square gives you trouble mid-season, tell the popcorn kernel right away rather than working around it, because every sale needs to land in the system to count toward your Scout's total.</p>
      </div>
    </div>

    <div class="booking" id="storefronts" style="margin-top:2.25rem">
      <div>
        <span class="eyebrow">Sign up</span>
        <h3>Book a storefront shift</h3>
        <p>Storefront shifts are booked through the pack's own scheduler. Pick the store, pick the time, and it is yours.</p>
        <ul class="checklist checklist--yes">
          <li>Opens 14 days ahead, so check back weekly</li>
          <li>Two hour shifts</li>
          <li>Two Scouts and two registered adults per shift</li>
          <li>Class A uniform</li>
        </ul>
        <div class="btn-row" style="margin-top:1.2rem">
          <a class="btn btn--primary" href="{book}">Reserve a shift</a>
        </div>
      </div>
      <figure class="booking__qr">
        <img src="images/storefront-qr.png" width="600" height="600" alt="QR code linking to the Pack 3049 storefront shift booking page" loading="lazy">
        <figcaption>Scan to book</figcaption>
      </figure>
    </div>

    <div class="callout callout--info">
      <p><strong>Shop online at <a href="https://prpopcornstore.com">prpopcornstore.com</a>.</strong> Every purchase is credited to your Scout and the pack by name, shipping is free, there is nothing to deliver, and online orders count toward your Scout's total, camp credit, and Winner's Circle just like everything else. This is the one to send to grandparents three states away.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <span class="eyebrow">The product mix</span>
    <h2>What we sell</h2>
    <p class="muted" style="max-width:66ch">Pecatonica River Popcorn, sold through the Anthony Wayne Area Council. Family owned and making popcorn since 1983. These twelve are what Pack 3049 stocks in person this season.</p>

    <ul class="products">
      <li class="product">
        <div class="product__img" style="--tin:#f4dd9a">
          <div class="product__tin"><svg viewBox="0 0 48 48" fill="#0b1c14" aria-hidden="true"><path d="M24 6c4 0 6.5 3 6 6.5 3.3-1.2 6.5 1 6.5 5 0 3-2 5.2-4.3 6.2 2.2 2 3.3 4.4 3.3 7.3 0 6.4-5.6 12-11.5 12S12.5 37 12.5 30.6c0-2.9 1.1-5.3 3.3-7.3C13.5 22.3 11.5 20.1 11.5 17c0-4 3.2-6.2 6.5-5-.5-3.5 2-6 6-6z" opacity=".85"/></svg><span>2 lb Yellow Popping Corn</span></div>
          <img src="images/products/popping-corn.jpg" alt="2 lb Yellow Popping Corn" loading="lazy" onload="this.classList.add(&#39;is-loaded&#39;)" onerror="this.remove()">
        </div>
        <div class="product__body">
          
          <h3 class="product__name">2 lb Yellow Popping Corn</h3>
          <p class="product__price">$15</p>
          <p class="product__allergen"><strong>Allergens:</strong> No allergens listed.</p>
        </div>
      </li>
      <li class="product">
        <div class="product__img" style="--tin:#d9973f">
          <div class="product__tin"><svg viewBox="0 0 48 48" fill="#0b1c14" aria-hidden="true"><path d="M24 6c4 0 6.5 3 6 6.5 3.3-1.2 6.5 1 6.5 5 0 3-2 5.2-4.3 6.2 2.2 2 3.3 4.4 3.3 7.3 0 6.4-5.6 12-11.5 12S12.5 37 12.5 30.6c0-2.9 1.1-5.3 3.3-7.3C13.5 22.3 11.5 20.1 11.5 17c0-4 3.2-6.2 6.5-5-.5-3.5 2-6 6-6z" opacity=".85"/></svg><span>Caramel Corn, TV bucket</span></div>
          <img src="images/products/caramel.jpg" alt="Caramel Corn, TV bucket" loading="lazy" onload="this.classList.add(&#39;is-loaded&#39;)" onerror="this.remove()">
        </div>
        <div class="product__body">
          
          <h3 class="product__name">Caramel Corn, TV bucket</h3>
          <p class="product__price">$15</p>
          <p class="product__allergen"><strong>Allergens:</strong> Contains milk and soy. Processed with peanuts and tree nuts.</p>
        </div>
      </li>
      <li class="product">
        <div class="product__img" style="--tin:#f0a63a">
          <div class="product__tin"><svg viewBox="0 0 48 48" fill="#0b1c14" aria-hidden="true"><path d="M24 6c4 0 6.5 3 6 6.5 3.3-1.2 6.5 1 6.5 5 0 3-2 5.2-4.3 6.2 2.2 2 3.3 4.4 3.3 7.3 0 6.4-5.6 12-11.5 12S12.5 37 12.5 30.6c0-2.9 1.1-5.3 3.3-7.3C13.5 22.3 11.5 20.1 11.5 17c0-4 3.2-6.2 6.5-5-.5-3.5 2-6 6-6z" opacity=".85"/></svg><span>Cheddar Cheese</span></div>
          <img src="images/products/cheddar.jpg" alt="Cheddar Cheese" loading="lazy" onload="this.classList.add(&#39;is-loaded&#39;)" onerror="this.remove()">
        </div>
        <div class="product__body">
          
          <h3 class="product__name">Cheddar Cheese</h3>
          <p class="product__price">$20</p>
          <p class="product__allergen"><strong>Allergens:</strong> Contains milk. Processed with soy, peanuts, and tree nuts.</p>
        </div>
      </li>
      <li class="product">
        <div class="product__img" style="--tin:#9cbf4a">
          <div class="product__tin"><svg viewBox="0 0 48 48" fill="#0b1c14" aria-hidden="true"><path d="M24 6c4 0 6.5 3 6 6.5 3.3-1.2 6.5 1 6.5 5 0 3-2 5.2-4.3 6.2 2.2 2 3.3 4.4 3.3 7.3 0 6.4-5.6 12-11.5 12S12.5 37 12.5 30.6c0-2.9 1.1-5.3 3.3-7.3C13.5 22.3 11.5 20.1 11.5 17c0-4 3.2-6.2 6.5-5-.5-3.5 2-6 6-6z" opacity=".85"/></svg><span>Jalapeno Cheese</span></div>
          <img src="images/products/jalapeno-cheese.jpg" alt="Jalapeno Cheese" loading="lazy" onload="this.classList.add(&#39;is-loaded&#39;)" onerror="this.remove()">
        </div>
        <div class="product__body">
          <span class="product__new">New this year</span>
          <h3 class="product__name">Jalapeno Cheese</h3>
          <p class="product__price">$20</p>
          <p class="product__allergen"><strong>Allergens:</strong> Contains milk. Processed with soy, peanuts, and tree nuts.</p>
        </div>
      </li>
      <li class="product">
        <div class="product__img" style="--tin:#b98a5e">
          <div class="product__tin"><svg viewBox="0 0 48 48" fill="#0b1c14" aria-hidden="true"><path d="M24 6c4 0 6.5 3 6 6.5 3.3-1.2 6.5 1 6.5 5 0 3-2 5.2-4.3 6.2 2.2 2 3.3 4.4 3.3 7.3 0 6.4-5.6 12-11.5 12S12.5 37 12.5 30.6c0-2.9 1.1-5.3 3.3-7.3C13.5 22.3 11.5 20.1 11.5 17c0-4 3.2-6.2 6.5-5-.5-3.5 2-6 6-6z" opacity=".85"/></svg><span>Trail Mix</span></div>
          <img src="images/products/trail-mix.jpg" alt="Trail Mix" loading="lazy" onload="this.classList.add(&#39;is-loaded&#39;)" onerror="this.remove()">
        </div>
        <div class="product__body">
          
          <h3 class="product__name">Trail Mix</h3>
          <p class="product__price">$20</p>
          <p class="product__allergen"><strong>Allergens:</strong> Contains peanuts, almonds, cashews, soy, and milk.</p>
        </div>
      </li>
      <li class="product">
        <div class="product__img" style="--tin:#f7cf6b">
          <div class="product__tin"><svg viewBox="0 0 48 48" fill="#0b1c14" aria-hidden="true"><path d="M24 6c4 0 6.5 3 6 6.5 3.3-1.2 6.5 1 6.5 5 0 3-2 5.2-4.3 6.2 2.2 2 3.3 4.4 3.3 7.3 0 6.4-5.6 12-11.5 12S12.5 37 12.5 30.6c0-2.9 1.1-5.3 3.3-7.3C13.5 22.3 11.5 20.1 11.5 17c0-4 3.2-6.2 6.5-5-.5-3.5 2-6 6-6z" opacity=".85"/></svg><span>Buttery Microwave, 15 pack</span></div>
          <img src="images/products/butter-microwave.jpg" alt="Buttery Microwave, 15 pack" loading="lazy" onload="this.classList.add(&#39;is-loaded&#39;)" onerror="this.remove()">
        </div>
        <div class="product__body">
          
          <h3 class="product__name">Buttery Microwave, 15 pack</h3>
          <p class="product__price">$25</p>
          <p class="product__allergen"><strong>Allergens:</strong> Contains milk.</p>
        </div>
      </li>
      <li class="product">
        <div class="product__img" style="--tin:#efe0b4">
          <div class="product__tin"><svg viewBox="0 0 48 48" fill="#0b1c14" aria-hidden="true"><path d="M24 6c4 0 6.5 3 6 6.5 3.3-1.2 6.5 1 6.5 5 0 3-2 5.2-4.3 6.2 2.2 2 3.3 4.4 3.3 7.3 0 6.4-5.6 12-11.5 12S12.5 37 12.5 30.6c0-2.9 1.1-5.3 3.3-7.3C13.5 22.3 11.5 20.1 11.5 17c0-4 3.2-6.2 6.5-5-.5-3.5 2-6 6-6z" opacity=".85"/></svg><span>Kettle Corn Microwave, 15 pack</span></div>
          <img src="images/products/kettle-corn.jpg" alt="Kettle Corn Microwave, 15 pack" loading="lazy" onload="this.classList.add(&#39;is-loaded&#39;)" onerror="this.remove()">
        </div>
        <div class="product__body">
          
          <h3 class="product__name">Kettle Corn Microwave, 15 pack</h3>
          <p class="product__price">$25</p>
          <p class="product__allergen"><strong>Allergens:</strong> No allergens listed.</p>
        </div>
      </li>
      <li class="product">
        <div class="product__img" style="--tin:#c8823a">
          <div class="product__tin"><svg viewBox="0 0 48 48" fill="#0b1c14" aria-hidden="true"><path d="M24 6c4 0 6.5 3 6 6.5 3.3-1.2 6.5 1 6.5 5 0 3-2 5.2-4.3 6.2 2.2 2 3.3 4.4 3.3 7.3 0 6.4-5.6 12-11.5 12S12.5 37 12.5 30.6c0-2.9 1.1-5.3 3.3-7.3C13.5 22.3 11.5 20.1 11.5 17c0-4 3.2-6.2 6.5-5-.5-3.5 2-6 6-6z" opacity=".85"/></svg><span>Caramel with Sea Salt</span></div>
          <img src="images/products/caramel-sea-salt.jpg" alt="Caramel with Sea Salt" loading="lazy" onload="this.classList.add(&#39;is-loaded&#39;)" onerror="this.remove()">
        </div>
        <div class="product__body">
          
          <h3 class="product__name">Caramel with Sea Salt</h3>
          <p class="product__price">$25</p>
          <p class="product__allergen"><strong>Allergens:</strong> Contains milk and soy. Processed with peanuts and tree nuts.</p>
        </div>
      </li>
      <li class="product">
        <div class="product__img" style="--tin:#8fc9d4">
          <div class="product__tin"><svg viewBox="0 0 48 48" fill="#0b1c14" aria-hidden="true"><path d="M24 6c4 0 6.5 3 6 6.5 3.3-1.2 6.5 1 6.5 5 0 3-2 5.2-4.3 6.2 2.2 2 3.3 4.4 3.3 7.3 0 6.4-5.6 12-11.5 12S12.5 37 12.5 30.6c0-2.9 1.1-5.3 3.3-7.3C13.5 22.3 11.5 20.1 11.5 17c0-4 3.2-6.2 6.5-5-.5-3.5 2-6 6-6z" opacity=".85"/></svg><span>Sea Salt Splash</span></div>
          <img src="images/products/sea-salt-splash.jpg" alt="Sea Salt Splash" loading="lazy" onload="this.classList.add(&#39;is-loaded&#39;)" onerror="this.remove()">
        </div>
        <div class="product__body">
          
          <h3 class="product__name">Sea Salt Splash</h3>
          <p class="product__price">$25</p>
          <p class="product__allergen"><strong>Allergens:</strong> Contains milk, soy, peanuts, and tree nuts.</p>
        </div>
      </li>
      <li class="product">
        <div class="product__img" style="--tin:#a8b98a">
          <div class="product__tin"><svg viewBox="0 0 48 48" fill="#0b1c14" aria-hidden="true"><path d="M24 6c4 0 6.5 3 6 6.5 3.3-1.2 6.5 1 6.5 5 0 3-2 5.2-4.3 6.2 2.2 2 3.3 4.4 3.3 7.3 0 6.4-5.6 12-11.5 12S12.5 37 12.5 30.6c0-2.9 1.1-5.3 3.3-7.3C13.5 22.3 11.5 20.1 11.5 17c0-4 3.2-6.2 6.5-5-.5-3.5 2-6 6-6z" opacity=".85"/></svg><span>Mountain Munch</span></div>
          <img src="images/products/mountain-munch.jpg" alt="Mountain Munch" loading="lazy" onload="this.classList.add(&#39;is-loaded&#39;)" onerror="this.remove()">
        </div>
        <div class="product__body">
          <span class="product__new">New this year</span>
          <h3 class="product__name">Mountain Munch</h3>
          <p class="product__price">$25</p>
          <p class="product__allergen"><strong>Allergens:</strong> Contains soy, peanuts, milk, and tree nuts.</p>
        </div>
      </li>
      <li class="product">
        <div class="product__img" style="--tin:#c69a6b">
          <div class="product__tin"><svg viewBox="0 0 48 48" fill="#0b1c14" aria-hidden="true"><path d="M24 6c4 0 6.5 3 6 6.5 3.3-1.2 6.5 1 6.5 5 0 3-2 5.2-4.3 6.2 2.2 2 3.3 4.4 3.3 7.3 0 6.4-5.6 12-11.5 12S12.5 37 12.5 30.6c0-2.9 1.1-5.3 3.3-7.3C13.5 22.3 11.5 20.1 11.5 17c0-4 3.2-6.2 6.5-5-.5-3.5 2-6 6-6z" opacity=".85"/></svg><span>Freedom Pretzels</span></div>
          <img src="images/products/freedom-pretzels.jpg" alt="Freedom Pretzels" loading="lazy" onload="this.classList.add(&#39;is-loaded&#39;)" onerror="this.remove()">
        </div>
        <div class="product__body">
          
          <h3 class="product__name">Freedom Pretzels</h3>
          <p class="product__price">$30</p>
          <p class="product__allergen"><strong>Allergens:</strong> Contains soy, wheat, and milk.</p>
        </div>
      </li>
      <li class="product">
        <div class="product__img" style="--tin:#e8b04a">
          <div class="product__tin"><svg viewBox="0 0 48 48" fill="#0b1c14" aria-hidden="true"><path d="M24 6c4 0 6.5 3 6 6.5 3.3-1.2 6.5 1 6.5 5 0 3-2 5.2-4.3 6.2 2.2 2 3.3 4.4 3.3 7.3 0 6.4-5.6 12-11.5 12S12.5 37 12.5 30.6c0-2.9 1.1-5.3 3.3-7.3C13.5 22.3 11.5 20.1 11.5 17c0-4 3.2-6.2 6.5-5-.5-3.5 2-6 6-6z" opacity=".85"/></svg><span>Cheese Lovers collection</span></div>
          <img src="images/products/cheese-lovers.jpg" alt="Cheese Lovers collection" loading="lazy" onload="this.classList.add(&#39;is-loaded&#39;)" onerror="this.remove()">
        </div>
        <div class="product__body">
          
          <h3 class="product__name">Cheese Lovers collection</h3>
          <p class="product__price">$50</p>
          <p class="product__allergen"><strong>Allergens:</strong> A mixed collection. Contains milk; check each item's label for full allergens.</p>
        </div>
      </li>
    </ul>

    <div class="callout callout--info">
      <p><strong>Allergen information</strong> comes from Pecatonica River Popcorn's published nutrition page. It is here because families ask, and because several Scouts in this pack have nut allergies. <strong>Always read the actual package before serving.</strong> The pack is not the manufacturer and cannot vouch for production changes.</p>
      <p>Full nutrition facts for every product: <a href="https://pecatonicariverpopcorn.com/nutrition-information/">pecatonicariverpopcorn.com</a></p>
    </div>

    <p class="muted">Military donations are also available for customers who want to support Scouting without taking product home. The online store carries larger gift tins and bundles that we do not stock in person.</p>

    <div class="callout">
      <p><strong>Caramel Corn and Kettle Corn go first.</strong> Every year. If your Scout is picking what to load in the wagon, start there, and expect Kettle Corn to be gone by mid season.</p>
    </div>
  </div>
</section>

<section class="section section--pine">
  <div class="wrap">
    <span class="eyebrow">What Scouts get</span>
    <h2>Rewards</h2>
    <p class="muted" style="max-width:66ch">Three milestones worth aiming at, and one thing every Scout earns no matter what they sell.</p>

    <div class="tiers" style="margin-top:1.75rem">
      <div class="tier">
        <div class="tier__amt">$525</div>
        <div class="tier__label">Sell this much</div>
        <h3>Your year is paid for</h3>
        <p>Registration and program fees, covered. Anything past this builds toward the next two.</p>
      </div>
      <div class="tier">
        <div class="tier__amt">$1,600</div>
        <div class="tier__label">Sell this much</div>
        <h3>Free summer camp at CCLT</h3>
        <p>A Cub Scout who sells <strong>$1,600</strong> earns one session of Cub Resident Camp at Camp Chief Little Turtle, free. Three days, two nights, aquatics, BB guns, archery, and the campfire.</p>
        <p class="muted">Camp credit is nontransferable, can only be used at CCLT, and Scouts may not combine their sales with a sibling's to reach it. Credit earned this season is used for the 2027 camp season.</p>
      </div>
      <div class="tier tier--top">
        <div class="tier__amt">$3,000</div>
        <div class="tier__label">Sell this much</div>
        <h3>Winner's Circle Club</h3>
        <p>Scouts who sell <strong>$3,000</strong> in popcorn join the council's Winner's Circle Club and <strong>pick one prize</strong> from the list below. Show and sell, take order, and online sales all count toward it.</p>
      </div>
    </div>

    <h3 style="margin-top:2.5rem">Winner's Circle: pick one</h3>
    <ul class="prizes">
      <li><span>Gift card</span>$200 Amazon</li>
      <li><span>Gift card</span>$200 Best Buy</li>
      <li><span>Gift card</span>$200 AMC</li>
      <li><span>Prize</span>Game table</li>
      <li><span>Prize</span>Drum set</li>
      <li><span>Prize</span>3D printer</li>
      <li><span>Prize</span>40 inch SmartCast TV</li>
      <li><span>Prize</span>Laptop</li>
    </ul>

    <div class="grid grid--2" style="margin-top:2.5rem">
      <div class="card">
        <h3>Every Scout: 4 percent back, in Amazon</h3>
        <p>This one has no minimum. Pack 3049 skips the prize catalog, takes the higher commission instead, and pays <strong>4 percent of each Scout's own sales</strong> straight back to them as an Amazon gift card at the end of the season. Sell $1,000, get $40 to spend on whatever you actually want.</p>
        <p class="muted">This is the pack's own reward and it stacks with everything above.</p>
      </div>
      <div class="card">
        <h3>Pie in the face</h3>
        <p>The pack's favorite tradition. Top sellers earn the right to put a pie in a leader's face, in front of everybody, at a pack meeting. Several leaders have learned not to volunteer.</p>
      </div>
    </div>

    <div class="callout callout--info">
      <p><strong>Crossing over to a troop?</strong> The council sets the Scouts BSA camp credit at <strong>$2,500</strong> in sales for one session of Scout Resident Camp. Worth knowing for Arrow of Light Scouts heading to a troop in the spring.</p>
    </div>

  </div>
</section>

<section class="section">
  <div class="wrap">
    <span class="eyebrow">Coach your Scout</span>
    <h2>The script, and what actually works</h2>
    <div class="grid grid--2">
      <div>
        <div class="card card--accent">
          <h3>The script</h3>
          <p class="oath" style="font-size:1.05rem">"Hello! My name is ______ and I am with Pack 3049. I am selling popcorn to earn my way to camp and support our camp outings. I have some great popcorn flavors available. My favorite flavor is ______, and I know you will love our popcorn. Would you consider supporting me?"</p>
          <p><strong>Always thank the customer, even when they say no.</strong> Be cordial and kind. That part is not a sales technique, it is the whole point.</p>
        </div>
      </div>
      <div>
        <h3>Selling tips</h3>
        <ul class="checklist checklist--yes">
          <li><strong>Be in uniform.</strong> A clean Class A does half the work.</li>
          <li><strong>Know the products.</strong> Names, flavors, and which one is your favorite.</li>
          <li><strong>Practice the pitch.</strong> Out loud, at home, before the first door.</li>
          <li><strong>Have confidence and smile.</strong> Let your Scout do the talking, not the parent.</li>
          <li><strong>Thank every customer.</strong> Every single one.</li>
        </ul>
        <h3 style="margin-top:1.75rem">Safety</h3>
        <ul class="checklist">
          <li>Buddy system, always. Never sell alone.</li>
          <li>An adult with them at every door and every storefront.</li>
          <li>Road rules: sidewalks, crosswalks, watch for cars backing out.</li>
          <li>Money stays with the adult, not in a Scout's pocket.</li>
          <li>Be home before dark.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <span class="eyebrow">If selling is not for you</span>
    <h2>Three ways to cover your year</h2>
    <div class="grid grid--3">
      <div class="card card--accent"><h3>Sell popcorn</h3><p>Reach the pack sales goal and your Scout's year is paid for. Order forms, storefronts, and online orders all count toward it.</p></div>
      <div class="card card--accent"><h3>Buyout</h3><p>Pay the pack's flat program amount instead and skip the sale entirely. No guilt, no follow up, no explanation needed.</p></div>
      <div class="card card--accent"><h3>Calendar fundraiser</h3><p>An alternative for families who would rather sell something other than popcorn.</p></div>
    </div>
    <div class="callout callout--info">
      <p><strong>And if none of that is realistic right now,</strong> talk to a Cubmaster. Financial assistance exists, the conversation stays private, and no child has ever been turned away from Pack 3049 over money.</p>
    </div>
  </div>
</section>

<section class="section" id="calculator">
  <div class="wrap">
    <span class="eyebrow">Do the math yourself</span>
    <h2>Buyout calculator</h2>
    <p class="muted" style="max-width:68ch">Type in what your Scout has sold so far and see exactly where you stand. Nothing is sent anywhere. The number stays in your own browser, so you can come back and update it as the season goes.</p>

    <form class="calc" id="buyout-calc" style="margin-top:1.75rem">
      <div class="calc__field">
        <div class="calc__input">
          <label for="calc-sales">Sales so far</label>
          <span class="hint">Total dollars sold: order form, storefronts, and online all count.</span>
          <div class="calc__box">
            <span class="calc__dollar" aria-hidden="true">$</span>
            <input type="number" id="calc-sales" min="0" step="1" inputmode="decimal" placeholder="0" autocomplete="off">
          </div>
        </div>
        <button type="button" class="calc__reset" id="calc-reset">Clear</button>
      </div>

      <div class="calc__grid" aria-live="polite">
        <div class="calc__stat">
          <span class="k">Credited to the pack</span>
          <span class="v" id="calc-credit">$0</span>
          <span class="n">38 cents of every dollar your Scout sells goes to Pack 3049.</span>
        </div>
        <div class="calc__stat calc__stat--owe" id="calc-owe-box">
          <span class="k" id="calc-owe-label">Buyout still owed</span>
          <span class="v" id="calc-owe">$200</span>
          <span class="n" id="calc-owe-note">Or sell $526 more and owe nothing.</span>
        </div>
        <div class="calc__stat">
          <span class="k">Your Scout's gift card</span>
          <span class="v" id="calc-back">$0</span>
          <span class="n">4 percent of their own sales, paid in Amazon at the end of the season.</span>
        </div>
      </div>

      <div class="calc__bar" id="calc-bar"><i></i></div>
      <p class="calc__scale"><span>$0</span><span>Year paid for at $525</span></p>

      <ul class="calc__next" id="calc-next">
        <li><span class="m">$525</span><span class="t">to cover your year</span></li>
        <li><span class="m">$1,600</span><span class="t">to free camp at CCLT</span></li>
        <li><span class="m">$3,000</span><span class="t">to the Winner's Circle Club</span></li>
      </ul>

      <p class="calc__note"><strong>How this works:</strong> the pack credits your Scout 38 cents on every dollar sold. The buyout is the pack's program cost per Scout, and whatever your sales have not already covered is what a buyout would be. Sell enough and it reaches zero. This is an estimate to help you plan, not a bill. The popcorn kernel's numbers are the official ones.</p>
    </form>

  </div>
</section>

<section class="section">
  <div class="narrow center">
    <h2>Questions about the sale?</h2>
    <p>Ask either Co-Cubmaster, or post in the <a href="{band}">BAND app</a>, where weekly sales updates go out all season.</p>
    <CONTACTS_HERE>
  </div>
</section>
""".replace("{band}", BAND).replace("{book}", "https://outlook.office365.com/book/CubScoutsPack3049Popcorn@indianatechedu.onmicrosoft.com/").replace("<CONTACTS_HERE>", CONTACTS),
)

# ---------------------------------------------------------------- CAMP
PAGES["camp.html"] = (
    "Summer Camp | Cub Scout Pack 3049",
    "Everything Pack 3049 families need for Cub Scout resident camp at Camp Chief Little Turtle: swim checks, departure day, the daily schedule, the packing list, campsite setup, health forms, and trading post hours.",
    """
<section class="hero hero--page">
  <div class="wrap">
    <span class="eyebrow">Pack 3049 summer camp</span>
    <h1>Camp Chief Little Turtle</h1>
    <p class="lede">Three days, two nights, and the single best thing the pack does all year. Everything you need to get your Scout there is on this page.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid--2">
      <div>
        <span class="eyebrow">The basics</span>
        <h2>At a glance</h2>
        <div class="rows">
          <div><span class="k">Dates</span><span class="v"><strong>Wednesday, July 22 through Friday, July 24, 2026</strong><br>Three days, two nights. Our pack attends the first three days of camp.</span></div>
          <div><span class="k">Location</span><span class="v">Camp Chief Little Turtle<br>2282 S 500 E, Pleasant Lake, IN 46779<br><a href="https://ccltbsa.org">ccltbsa.org</a></span></div>
          <div><span class="k">Meet at</span><span class="v">Cedar Creek Church, roughly 8:00 to 8:30 AM on July 22<br><span class="muted">Tentative. The final time is confirmed closer to camp.</span></span></div>
          <div><span class="k">Program</span><span class="v">Cub Scout Resident Camp</span></div>
          <div><span class="k">Our site</span><span class="v">Shawnee, the campsite Pack 3049 originally built</span></div>
        </div>
      </div>
      <div>
        <div class="card card--accent">
          <h3>2026 theme: Knights of the Turtle Kingdom</h3>
          <p>Since the passing of King Jack, the kingdom seeks brave and loyal knights to defend and rebuild the Turtle Kingdom. Scouts test their skills to become knights, and every pack is encouraged to build a Pack Shield with a Pack Crest.</p>
          <p><strong>There is an award for the best shield.</strong> Pack 3049 intends to win it.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--pine">
  <div class="wrap">
    <span class="eyebrow">Do these six things</span>
    <h2>Action items for every family</h2>
    <ol class="steps" style="margin-top:1.5rem;max-width:70ch">
      <li><strong>Optional:</strong> bring your Scout to a pre camp swim check on July 16 or July 21. Details below.</li>
      <li>Turn in your Scout's Scouting America Health Form, <strong>Parts A and B</strong>.</li>
      <li>Confirm your camp payment is complete.</li>
      <li>Adults staying at camp: complete <strong>Safeguarding Youth</strong> training.</li>
      <li>Start gathering gear from the packing list.</li>
      <li><strong>Pack a sack lunch for Day 1.</strong> Lunch is not provided on arrival day.</li>
    </ol>
    <ul class="jumpnav" style="margin-top:2.25rem">
      <li><a href="#swim">Swim check</a></li>
      <li><a href="#departure">Departure day</a></li>
      <li><a href="#schedule">Daily schedule</a></li>
      <li><a href="#packing">Packing list</a></li>
      <li><a href="#campsite">Campsite and teardown</a></li>
      <li><a href="#health">Health forms</a></li>
      <li><a href="#tradingpost">Trading post and meals</a></li>
    </ul>
  </div>
</section>

<section class="section" id="swim">
  <div class="wrap">
    <span class="eyebrow">Section 1</span>
    <h2>Before camp: the swim check</h2>
    <div class="callout callout--info">
      <p><strong>This is completely optional.</strong> If you cannot make either date, no worries at all. Swim testing can be done at camp instead. These dates just exist for your convenience.</p>
    </div>
    <div class="grid grid--2">
      <div>
        <p>Doing the swim check early saves time, because there is less waiting at camp, and it means more fun, because Scouts get straight into activities on arrival day. It is entirely your choice.</p>
        <p><strong>The swim check is for Cub Scouts and adults.</strong> Everyone who will be in the water at camp needs a swim certification, so adults attending camp should complete one too.</p>
        <h3>How check in works</h3>
        <ol class="steps">
          <li>Not a YMCA member? Go to the front desk and say you are here for the Cub Scout swim check. They will check you in.</li>
          <li>Come back to the Aquatics area.</li>
          <li>Pack leaders will be there to get your Scout checked in.</li>
          <li>The test takes 10 to 15 minutes at most, as long as there is not a long line.</li>
          <li>All paperwork is submitted to the camp coordinator and the Scout Office for you. You do not need to do anything else.</li>
          <li>Rinse off, change in the locker rooms, and head home.</li>
        </ol>
      </div>
      <div>
        <div class="card card--accent">
          <h3>Two dates to choose from</h3>
          <ul class="sched" style="margin-bottom:1rem">
            <li><span class="when">Thu Jul 16</span><span class="what">6:00 to 7:30 PM</span></li>
            <li><span class="when">Tue Jul 21</span><span class="what">6:00 to 7:30 PM</span></li>
          </ul>
          <p class="muted">Earliest arrival 6:00 PM, latest arrival 7:30 PM.</p>
          <p><strong>Jackson R. Lehman Family YMCA</strong><br>
          5680 YMCA Park Dr. W.<br>
          Fort Wayne, IN 46835</p>
          <p>Indoor pool, so rain or shine.</p>
          <p><strong>Wear and bring:</strong> come in your swimsuit. Bring a towel, flip flops, and anything else you need.</p>
          <p><a href="https://maps.google.com/?q=5680+YMCA+Park+Dr+W,+Fort+Wayne,+IN+46835">Get directions</a></p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint" id="departure">
  <div class="wrap">
    <span class="eyebrow">Section 2</span>
    <h2>Departure day, Wednesday July 22</h2>
    <p class="muted" style="max-width:70ch">This schedule is tentative and based on previous years. Exact times and final instructions go out closer to camp.</p>

    <div class="alert">
      <h3>Pack a lunch. Seriously.</h3>
      <p><strong>Lunch is NOT provided at camp on Day 1.</strong> Every Scout needs a packed sack lunch on departure day. Please double check this before you leave home. It is missed every single year.</p>
    </div>

    <div class="grid grid--2">
      <div>
        <h3>At Cedar Creek Church, about 8:00 to 8:30 AM</h3>
        <p>Everyone checks in at the church first. We verify that:</p>
        <ul class="checklist">
          <li>Health forms have been submitted</li>
          <li>Swim information is up to date</li>
          <li>Camp payments have been made</li>
        </ul>
        <p>Then we load everyone's gear into the trailer, hand out camp shirts, and carpool up to camp together.</p>
      </div>
      <div>
        <h3>Arriving at Camp Chief Little Turtle</h3>
        <ol class="steps">
          <li>Our camp coordinator checks in all medical documentation and required paperwork.</li>
          <li>Once check in is complete, everyone receives their camp wristbands.</li>
          <li>The trailer heads to our campsite while parents and Scouts hike in. <strong>Personal vehicles stay in the parking lot.</strong> Only the truck and trailer are allowed on campsite grounds.</li>
          <li>At the campsite we unload the trailer, set up tents, and get ready for a few days of adventure.</li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section" id="schedule">
  <div class="wrap">
    <span class="eyebrow">Section 3</span>
    <h2>Daily camp schedule</h2>
    <p class="muted">Subject to change. Our pack attends Wednesday July 22 through Friday July 24.</p>
    <div class="table-scroll">
      <table class="sched-table">
        <caption class="visually-hidden">Three day camp schedule by time</caption>
        <thead>
          <tr><th scope="col">Time</th><th scope="col">Day 1, Wed Jul 22</th><th scope="col">Day 2, Thu Jul 23</th><th scope="col">Day 3, Fri Jul 24</th></tr>
        </thead>
        <tbody>
          <tr><td>6:30 AM</td><td></td><td>Reveille</td><td>Reveille</td></tr>
          <tr><td>7:15 AM</td><td></td><td>Camp breakfast</td><td>Camp breakfast</td></tr>
          <tr><td>8:00 AM</td><td><strong>Meet and check in at Cedar Creek Church</strong>, 8:00 to 8:30 AM</td><td></td><td></td></tr>
          <tr><td>8:30 AM</td><td></td><td>Assembly and flag raising</td><td>Assembly and flag raising</td></tr>
          <tr><td>8:45 AM</td><td></td><td>Leader meeting</td><td>Leader meeting</td></tr>
          <tr><td>9:00 AM</td><td>Depart for camp, carpool</td><td>Session 1</td><td>Session 1</td></tr>
          <tr><td>10:00 AM</td><td rowspan="3">Unit arrival and campsite setup.<br><span class="evt-flag">Lunch is NOT provided.</span></td><td>Session 2</td><td>Session 2</td></tr>
          <tr><td>11:00 AM</td><td>Session 3</td><td>Session 3</td></tr>
          <tr><td>12:00 PM</td><td>Lunch</td><td>Lunch</td></tr>
          <tr><td>1:00 PM</td><td></td><td>Rest time</td><td>Rest time</td></tr>
          <tr><td>2:00 PM</td><td rowspan="2">Camp orientation. Staff guides meet units in the campsites.</td><td>Session 4</td><td>Session 4</td></tr>
          <tr><td>3:00 PM</td><td>Session 5</td><td>Session 5</td></tr>
          <tr><td>4:00 PM</td><td></td><td>Session 6</td><td>Session 6</td></tr>
          <tr><td>4:30 PM</td><td>Leader meeting</td><td></td><td></td></tr>
          <tr><td>5:30 PM</td><td>Camp dinner</td><td>Camp dinner</td><td>Camp dinner</td></tr>
          <tr><td>6:45 PM</td><td>Assembly and flag lowering</td><td>Assembly and flag lowering</td><td>Assembly and flag lowering</td></tr>
          <tr><td>7:15 PM</td><td><strong>Opening campfire</strong></td><td>Open program, 7:15 to 9:00 PM</td><td><strong>Closing campfire</strong></td></tr>
          <tr><td>10:00 PM</td><td>Taps, lights out</td><td>Taps, lights out</td><td>Taps, lights out</td></tr>
        </tbody>
      </table>
    </div>
    <p class="muted">Sessions run about 50 minutes. Dens move through the rotation together, and the specific rotation is assigned at camp.</p>

    <h3 style="margin-top:2.5rem">What the sessions are</h3>
    <div class="grid grid--3">
      <div class="card card--stem"><h3>Aquatics</h3><p>Water adventures at the waterfront. This is why the swim check matters.</p></div>
      <div class="card card--stem"><h3>RATA</h3><p>BB guns, slingshots, and archery at the ranges. Usually the runaway favorite.</p></div>
      <div class="card card--stem"><h3>Crafts</h3><p>Finding your way and art projects, indoors at the lodges when the sun is brutal.</p></div>
      <div class="card card--stem"><h3>Adventure</h3><p>Games, skits, and knife safety. Bears and older earn toward the Whittlin' Chip.</p></div>
      <div class="card card--stem"><h3>Flex</h3><p>Unit led time. Fishing, hiking, games, or whatever our pack decides to do with it.</p></div>
      <div class="card card--stem"><h3>Open program</h3><p>Thursday evening, 7:15 to 9:00 PM. Camp wide activities, families welcome.</p></div>
    </div>

    <h3 style="margin-top:2.5rem">Uniform guide</h3>
    <div class="grid grid--2">
      <div class="card">
        <h3>Class A</h3>
        <p>Official Scout uniform, neckerchief, slide, and optional hat.</p>
        <p><strong>Required for:</strong> dinner every day, the opening campfire on the first day, and the closing campfire on the last day.</p>
      </div>
      <div class="card">
        <h3>Class B</h3>
        <p>The pack T shirt we hand out on departure day, or another T shirt.</p>
        <p><strong>Worn:</strong> all other times during camp.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint" id="packing">
  <div class="wrap">
    <span class="eyebrow">Section 4</span>
    <h2>Packing checklist</h2>
    <div class="callout">
      <p><strong>Bring no more than you need for two nights and three days.</strong> Mark every item with your Scout's <strong>name</strong> and <strong>Pack 3049</strong>. Pack in a duffel bag or backpack. Light is right.</p>
    </div>
    <div class="grid grid--4" style="align-items:start">
      <div class="card">
        <p class="checklist__head">Clothing</p>
        <ul class="checklist">
          <li>Pajamas or other sleepwear</li>
          <li>Class A Scout shirt and neckerchief</li>
          <li>Pack 3049 Class B shirts, daily if possible</li>
          <li>Light jacket or sweatshirt</li>
          <li>Shorts (3)</li>
          <li>Pants (1)</li>
          <li>Underclothes (3)</li>
          <li>Camp hat</li>
          <li>Swimsuit and beach towel, wear on the first day</li>
          <li>Shoes, 2 pairs: tennis shoes and hiking shoes if you have them</li>
          <li>Rain poncho</li>
        </ul>
      </div>
      <div class="card">
        <p class="checklist__head">Toiletries and personal</p>
        <ul class="checklist">
          <li>Bath towel and wash cloth</li>
          <li>Toothbrush and toothpaste</li>
          <li>Soap and shampoo</li>
          <li>Comb</li>
        </ul>
        <p class="checklist__head" style="margin-top:1.4rem">Optional</p>
        <ul class="checklist">
          <li>Shower shoes</li>
          <li>Small carrying bag</li>
          <li>Camera</li>
          <li>Sunglasses</li>
          <li>Extra shirts</li>
          <li>Stamps and envelopes</li>
          <li>Religious materials</li>
          <li>Watch</li>
          <li>Folding pocket knife, Whittlin' Chip required</li>
          <li>Wallet and spending money</li>
          <li>Fishing equipment</li>
          <li>Personal first aid kit</li>
          <li>Cub Scout handbook</li>
        </ul>
      </div>
      <div class="card">
        <p class="checklist__head">Equipment and supplies</p>
        <ul class="checklist">
          <li>Sleeping bag and pad</li>
          <li>Pillow</li>
          <li><strong>Water bottle</strong></li>
          <li>Flashlight or head lamp, plus extra batteries</li>
          <li>Sunscreen, SPF 30 or higher</li>
          <li>Dirty clothes bag</li>
          <li>Camp chair</li>
          <li>Mosquito repellent</li>
          <li>Whittlin' Chip, for Bears, Webelos, and AOL</li>
        </ul>
        <p class="muted" style="margin-top:1rem">Coolers and drinks are fine to bring to the campsite.</p>
      </div>
      <div class="card">
        <p class="checklist__head">Do not bring</p>
        <ul class="checklist checklist--warn">
          <li>Food in tents</li>
          <li>Open toed shoes, sandals, or flip flops</li>
          <li>Electronics of any kind: music players, tablets, games, phones</li>
          <li>Bicycles</li>
          <li>Sheath or fixed blade knives</li>
          <li>Alcohol, cigarettes, or drugs</li>
          <li>Fireworks, flammables, or anything else dangerous</li>
        </ul>
      </div>
    </div>
    <div class="callout callout--info">
      <p><strong>No gear? Not a problem.</strong> The pack has tents and extra tarps to lend. Just ask a leader well before departure day, and do not go buy a camping setup for a first campout.</p>
    </div>
  </div>
</section>

<section class="section" id="campsite">
  <div class="wrap">
    <span class="eyebrow">Section 5</span>
    <h2>Campsite setup and Friday teardown</h2>
    <div class="callout">
      <p><strong>Our home at CCLT is the Shawnee campsite.</strong> Pack 3049 always camps at Shawnee. We are the pack that originally created that campsite, so we have a lot of legacy there. It is a large wooded site with a pavilion, four patrol sites, and it sits right by the shower house.</p>
    </div>
    <div class="grid grid--2">
      <div>
        <h3>Setting up on arrival, Wednesday</h3>
        <ol class="steps">
          <li>At the church in the morning, all campsite items are loaded into the trailer.</li>
          <li>Once we arrive at camp, all vehicles are left in the parking lot. Personal vehicles are not allowed to drive back to the campsite. Only the pack truck and trailer are permitted on campsite grounds.</li>
          <li>Everyone waits by the trailer while our coordinator turns in documentation to the camp staff.</li>
          <li>After check in and wristbands, the truck and trailer drive to the campsite while the pack, adults and Scouts together, hikes back.</li>
          <li>At the campsite we unload the trailer and everyone sets up. Each family sets up their own campsite and brings their own camping supplies.</li>
        </ol>
      </div>
      <div>
        <h3>Showers</h3>
        <p>The camp shower house is right by the Shawnee campsite. <strong>An adult from our pack must be present whenever our Scouts are using the shower facility.</strong> The camp issues one shower key per unit, and it stays with an adult leader for the whole of camp.</p>
        <p>Shower shoes are a good idea. They are on the packing list.</p>

        <h3 style="margin-top:2rem">Tearing down on Friday</h3>
        <p>Each family tears down their own tent and cleans their own site. Leave No Trace. <strong>Our campsite has to pass inspection before leaders are allowed to leave</strong>, so pack up sooner rather than later. You have two options:</p>
        <div class="card" style="margin-top:1rem">
          <h3>Option 1: preload your car</h3>
          <p>Tear down during free time and carry your supplies back to your vehicle. After the closing campfire, families usually take pictures with their Scouts and friends, and if your car is already loaded you can leave right after.</p>
        </div>
        <div class="card" style="margin-top:1rem">
          <h3>Option 2: send it back in the trailer</h3>
          <p>If you would rather not walk your gear to the car or tear down early, tear down after the closing campfire and load into the trailer, which a pack leader drives back to the church. <strong>Tell a leader if you choose this</strong>, so you get a call or text when the trailer reaches the church for pickup.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--pine" id="health">
  <div class="wrap">
    <span class="eyebrow">Section 6</span>
    <h2>Health forms, medications, and adult training</h2>
    <div class="grid grid--3">
      <div class="card">
        <h3>What has to be on file</h3>
        <ul class="checklist">
          <li>Scouting America Health Form, Parts A and B</li>
          <li>Dietary restrictions</li>
          <li>All medications, prescription and over the counter</li>
          <li>Any special dietary food items</li>
        </ul>
      </div>
      <div class="card">
        <h3>How medications work</h3>
        <p>Medications are turned in to our camp coordinator during check in at camp, along with all medical documentation. They are administered at the camp medical office.</p>
        <p><strong>Label every medication clearly with your Scout's name.</strong></p>
      </div>
      <div class="card">
        <h3>Required adult training</h3>
        <p>Every adult staying overnight at camp must complete <strong>Safeguarding Youth</strong> training beforehand. It is free, takes about 90 minutes, and is done online through your my.scouting.org account.</p>
        <p><a href="https://www.scouting.org/training/safeguarding-youth/">Take the training</a></p>
      </div>
    </div>
    <div class="callout">
      <p><strong>Questions about forms, medications, dietary needs, or logistics?</strong> Contact our camp coordinator through the pack. Reach out early rather than the week before, because health forms are what hold families up every year.</p>
      <p>Camp families also have their own <a href="{bandcamp}">BAND chat just for CCLT</a>. That is the fastest place to ask a packing question at 9 PM the night before departure.</p>
    </div>
  </div>
</section>

<section class="section" id="tradingpost">
  <div class="wrap">
    <span class="eyebrow">Section 7</span>
    <h2>Trading post and meal times</h2>
    <div class="grid grid--2">
      <div>
        <h3>Trading post and quartermaster hours</h3>
        <p>Scouts will want a little spending money for souvenirs and snacks. Hours during our stay:</p>
        <div class="rows">
          <div><span class="k">Day 1, Wed</span><span class="v">1:00 to 5:00 PM<br>6:15 to 7:00 PM<br>After the campfire until 9:00 PM</span></div>
          <div><span class="k">Day 2, Thu</span><span class="v">8:00 to 9:15 AM<br>12:30 to 2:00 PM<br>6:30 to 8:00 PM</span></div>
          <div><span class="k">Day 3, Fri</span><span class="v">8:00 to 9:15 AM<br>12:30 to 2:00 PM<br>6:30 to 8:00 PM<br>After the campfire until 9:00 PM</span></div>
        </div>
      </div>
      <div>
        <h3>Meals at the dining hall</h3>
        <p>Arrive at the dining hall <strong>with your whole unit five minutes before your scheduled meal time</strong> to wash hands and line up. A staff member directs you into the meal line once the entire unit is accounted for.</p>
        <p>Our pack's specific meal rotation times are shared at camp.</p>
        <h3 style="margin-top:2rem">About the campsites</h3>
        <p>There are twelve campsites at Camp Chief Little Turtle. Each one has several patrol sites, a pit latrine, wash stand, fire ring, picnic table, and plenty of firewood. Mosquito nets are available to check out through the camp quartermaster.</p>
        <p>The full campsite map and descriptions are on the camp's own site at <a href="https://ccltbsa.org">ccltbsa.org</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <span class="eyebrow">The rest of the year</span>
    <h2>Camping closer to home</h2>
    <div class="grid grid--3">
      <div class="card"><h3>Pack camp-in</h3><p>An indoor overnight at the church in the fall. Games, a movie, way too much pizza, and a sleeping bag on a gym floor. A great first overnight for Lions and Tigers.</p></div>
      <div class="card"><h3>Hikes</h3><p>Fall hikes at Metea County Park and other Allen County parks. Easy distances, real trails, and usually a scavenger hunt.</p></div>
      <div class="card"><h3>Spring campout</h3><p>A weekend at a local council camp once the weather turns. Tents, campfire cooking, and outdoor skills toward rank adventures.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="narrow center">
    <h2>Prepared. For fun. Ready for adventure.</h2>
    <p>Questions about camp, forms, medications, or gear? Call or email either Co-Cubmaster, any time.</p>
    <div class="contacts">
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Nicole Howard</div>
        <a href="tel:+12605572243">(260) 557-2243</a>
        <a href="mailto:howardfamily411@gmail.com">howardfamily411@gmail.com</a>
      </div>
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Dan Noll</div>
        <a href="tel:+12606025134">(260) 602-5134</a>
        <a href="mailto:steelers6615@gmail.com">steelers6615@gmail.com</a>
      </div>
    </div>
    <div class="btn-row">
      <a class="btn btn--primary" href="{bandcamp}">Join the camp BAND chat</a>
      <a class="btn btn--solid" href="{band}">The main pack BAND group</a>
    </div>
    <p class="muted" style="margin-top:1.25rem;max-width:64ch">Two different groups, on purpose. The <strong>camp chat</strong> is just for families going to CCLT: packing questions, carpools, and anything that comes up during the week itself. The <strong>pack group</strong> is where everything else lives all year.</p>
  </div>
</section>
""".replace("{band}", BAND).replace("{bandcamp}", BAND_CAMP),
)

# ---------------------------------------------------------------- GALLERY
PAGES["gallery.html"] = (
    "Photo Gallery | Cub Scout Pack 3049",
    "Photos from Pack 3049: pack meetings, the Pinewood Derby, summer camp, hikes, and service projects.",
    """
<section class="hero hero--page">
  <div class="wrap">
    <span class="eyebrow">Gallery</span>
    <h1>Proof it's this much fun</h1>
    <p class="lede">Derby day, muddy hikes, pies to the face, and a lot of proud kids holding badges.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">

    <p class="lede" style="max-width:68ch">Our photo albums live in the places pack families already check every week. Here is what
       you will find in them, and where to look.</p>

    <div class="grid grid--2" style="margin-top:2rem">
      <div class="card card--accent">
        <h3>Pinewood Derby</h3>
        <p>Build night at the church, where a block of pine and four nails turn into something
           that moves. Then race day: cars on the track, the whole pack leaning over the rail,
           and a winners' circle where every Scout gets something.</p>
      </div>
      <div class="card card--accent">
        <h3>Summer camp</h3>
        <p>A week at Camp Chief Little Turtle. Archery and BB range, swimming, the Shawnee
           campsite, and a closing campfire that most kids talk about until the next one.</p>
      </div>
      <div class="card card--accent">
        <h3>Pack meetings and awards</h3>
        <p>Rank advancement, the fall carnival, and yes, pie in the face night. This is where
           badges get handed out in front of everybody, which is the whole point.</p>
      </div>
      <div class="card card--accent">
        <h3>Outdoors and service</h3>
        <p>Fall hikes at Metea Park, marching in the Grabill Days parade, and the service
           projects our Scouts do for the community that chartered us.</p>
      </div>
    </div>

    <div class="cta-row" style="margin-top:2.25rem">
      <a class="btn btn--primary" href="{facebook}">See the photos on Facebook</a>
      <a class="btn btn--solid" href="{band}">Photos and updates on BAND</a>
    </div>
    <p class="muted" style="margin-top:1rem;max-width:64ch">The Facebook group is private to pack
       families, so ask to join and a leader will let you in.</p>
  </div>
</section>

<section class="section section--tint">
  <div class="narrow">
    <h2>Photo policy</h2>
    <p>We post photos of pack activities to show families what Scouting looks like. We do not publish Scouts' full names, ages, schools, or any contact information alongside photos. If you would rather your child not appear on this site or in pack social media, tell any leader and we will honor it, no explanation needed.</p>
    <p>Most of what we post day to day goes in the <a href="{facebook}">pack Facebook group</a>, which is private to pack families. To opt your child out, contact either Co-Cubmaster.</p>
    <div class="contacts">
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Nicole Howard</div>
        <a href="tel:+12605572243">(260) 557-2243</a>
        <a href="mailto:howardfamily411@gmail.com">howardfamily411@gmail.com</a>
      </div>
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Dan Noll</div>
        <a href="tel:+12606025134">(260) 602-5134</a>
        <a href="mailto:steelers6615@gmail.com">steelers6615@gmail.com</a>
      </div>
    </div>
  </div>
</section>
""".replace("{facebook}", FACEBOOK).replace("{band}", BAND),
)

# ---------------------------------------------------------------- FAQ
PAGES["faq.html"] = (
    "Parent Questions | Cub Scout Pack 3049",
    "Answers to the questions new Cub Scout families ask most: cost, time commitment, uniforms, girls in Scouting, popcorn, and what happens after 5th grade.",
    """
<section class="hero hero--page">
  <div class="wrap">
    <span class="eyebrow">Questions and answers</span>
    <h1>Everything parents ask</h1>
    <p class="lede">The honest answers, including the ones about time and money.</p>
  </div>
</section>

<section class="section">
  <div class="narrow">

    <h2>Getting started</h2>

    <details class="faq"><summary>What exactly is Cub Scouting?</summary><div class="faq__body">
      <p>Cub Scouting is the kindergarten through 5th grade program of Scouting America. Kids meet in small groups by grade, work through age appropriate adventures in a handbook, earn ranks, and get outdoors. The whole thing is built to be done with a parent alongside, not instead of one.</p>
    </div></details>

    <details class="faq"><summary>Can girls join?</summary><div class="faq__body">
      <p>Yes. Pack 3049 is a family pack and girls and boys are both full members, in the same dens, earning the same ranks.</p>
    </div></details>

    <details class="faq"><summary>My child is shy, or has never camped, or knows nobody in the pack.</summary><div class="faq__body">
      <p>That describes about half the pack on the first night. Dens are small, leaders are parents, and kids sort themselves out fast. Come try a meeting before you decide anything.</p>
    </div></details>

    <details class="faq"><summary>Can we join in the middle of the year?</summary><div class="faq__body">
      <p>Yes, any time. Registration is prorated by Scouting America, and your Scout's den leader will help catch up on adventures. Plenty of our best Scouts started in January.</p>
    </div></details>

    <h2 style="margin-top:2.5rem">Time and commitment</h2>

    <details class="faq"><summary>How much time does this take?</summary><div class="faq__body">
      <p>A den meeting is about an hour, two or three Mondays a month. Add a monthly pack meeting and a handful of bigger events across the year: a hike, the derby, the camp-in, Blue and Gold, and summer camp if you want it. Families take what they can and skip what they cannot.</p>
    </div></details>

    <details class="faq"><summary>Do parents have to stay?</summary><div class="faq__body">
      <p>For Lions, yes. Every kindergarten Scout has an adult partner at every meeting. For older dens a parent does not have to be in the room every week, but Cub Scouting works best when you are around, and Scouting America requires at least two registered adult leaders at every activity.</p>
    </div></details>

    <details class="faq"><summary>Do I have to be a leader?</summary><div class="faq__body">
      <p>No. But the pack only runs because parents step up, and there is a job at every size: den leader, treasurer, derby crew, popcorn help, or just driving to a hike. Ask what needs doing and we will find something that fits your life.</p>
    </div></details>

    <h2 style="margin-top:2.5rem">Money</h2>

    <details class="faq"><summary>What does it cost?</summary><div class="faq__body">
      <p><strong>$100 per Scout, per year</strong> to register with Pack 3049, with discounts for families with more than one Scout and for registered adult leaders. That is under $3 a week for a full year of Scouting. Most of it goes straight back out to Scouting America and the council, so the pack actually runs registration at a loss. Awards, badges, activities, and the banquet are all paid for by the popcorn sale. Full breakdown on the <a href="join.html">join page</a>.</p>
    </div></details>

    <details class="faq"><summary>Do we have to sell popcorn?</summary><div class="faq__body">
      <p>No. Popcorn is how most families cover their year without writing a check, and a Scout who reaches the pack goal is paid up. A Scout who sells $1,600 also earns free summer camp at CCLT, and every Scout gets 4 percent of their own sales back as an Amazon gift card. Families who would rather not sell can take the buyout or do the calendar fundraiser instead. See the <a href="popcorn.html">popcorn page</a>.</p>
    </div></details>

    <details class="faq"><summary>What if we cannot afford it?</summary><div class="faq__body">
      <p>Then we help, quietly. Financial assistance exists at both the pack and council level and no child has ever been turned away from Pack 3049 over money. Talk to a leader.</p>
    </div></details>

    <h2 style="margin-top:2.5rem">Uniforms and gear</h2>

    <details class="faq"><summary>What do we have to buy?</summary><div class="faq__body">
      <p>The Class A uniform shirt, the neckerchief and slide for your Scout's rank, and the handbook. That is it to start. Pants, hats, and belts are optional. Ask before you buy: the pack usually has used shirts and neckerchiefs to hand down.</p>
    </div></details>

    <details class="faq"><summary>Where do we buy it?</summary><div class="faq__body">
      <p>The Anthony Wayne Scout Shop, 8315 W. Jefferson Boulevard in Fort Wayne, <a href="tel:+12604329593">(260) 432-9593</a>. Monday to Friday 8:30 AM to 5:00 PM and Saturday 9:00 AM to 1:00 PM. Bring your Scout so the shirt gets fitted, and tell them you are with Pack 3049 in the Pokagon District so the patches are right.</p>
    </div></details>

    <details class="faq"><summary>Do we need camping gear right away?</summary><div class="faq__body">
      <p>No. Nothing before summer camp, and even then the pack has tents and tarps to lend. Do not go buy a setup for a first campout.</p>
    </div></details>

    <h2 style="margin-top:2.5rem">How the pack works</h2>

    <details class="faq"><summary>What is the difference between a den meeting and a pack meeting?</summary><div class="faq__body">
      <p>A den is your Scout's grade level group, usually six to twelve kids, and that is where the actual work of Scouting happens. A pack meeting is every den plus every family together once a month for awards, skits, and a theme. Louder, shorter, more fun.</p>
    </div></details>

    <details class="faq"><summary>How do I find out about schedule changes?</summary><div class="faq__body">
      <p>The <a href="{band}">BAND app</a> first, then the <a href="{facebook}">pack Facebook group</a>. Den leaders post reminders in BAND, and that is where a snow cancellation will show up.</p>
    </div></details>

    <details class="faq"><summary>How does Scouting keep kids safe?</summary><div class="faq__body">
      <p>Every registered adult completes Youth Protection Training and passes a background check, and it is renewed regularly. Two registered adults are required at every activity, one on one contact between an adult and a Scout is prohibited, and adults staying overnight complete additional Safeguarding Youth training. If something ever concerns you, tell a leader immediately.</p>
    </div></details>

    <details class="faq"><summary>What happens after 5th grade?</summary><div class="faq__body">
      <p>Arrow of Light Scouts cross over into a Scouts BSA troop, which is the program for 11 to 17 year olds. It is a bigger, more independent version of everything they have been doing. We work with local troops and help every family find the right fit before crossover.</p>
    </div></details>

    <div class="callout callout--info" style="margin-top:2.5rem">
      <p><strong>Did not find your question?</strong> Ask a Cubmaster. Nobody has ever been the first person to ask.</p>
    </div>
    <div class="contacts">
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Nicole Howard</div>
        <a href="tel:+12605572243">(260) 557-2243</a>
        <a href="mailto:howardfamily411@gmail.com">howardfamily411@gmail.com</a>
      </div>
      <div class="contacts__card">
        <span class="contacts__role">Co-Cubmaster</span>
        <div class="contacts__name">Dan Noll</div>
        <a href="tel:+12606025134">(260) 602-5134</a>
        <a href="mailto:steelers6615@gmail.com">steelers6615@gmail.com</a>
      </div>
    </div>
  </div>
</section>
""".replace("{band}", BAND).replace("{facebook}", FACEBOOK),
)

# ---------------------------------------------------------------- CONTACT
PAGES["contact.html"] = (
    "Contact | Cub Scout Pack 3049",
    "Get in touch with Cub Scout Pack 3049 in Leo, Indiana. Leadership, meeting location, Facebook group, BAND app, and the Anthony Wayne Scout Shop.",
    """
<section class="hero hero--page">
  <div class="wrap">
    <span class="eyebrow">Contact</span>
    <h1>Come find us</h1>
    <p class="lede">Email us, catch us on a Monday night, or join the group where the pack actually talks.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid--2">
      <div class="card card--accent">
        <h3>Nicole Howard</h3>
        <p class="muted" style="margin-top:-.5rem"><strong>Co-Cubmaster</strong></p>
        <p><a class="btn btn--primary" href="tel:+12605572243">(260) 557-2243</a></p>
        <p><a href="mailto:howardfamily411@gmail.com">howardfamily411@gmail.com</a></p>
        <p class="muted">Call, text, or email. Tell us your Scout's grade and we will connect you with the right den leader.</p>
      </div>
      <div class="card card--accent">
        <h3>Dan Noll</h3>
        <p class="muted" style="margin-top:-.5rem"><strong>Co-Cubmaster</strong></p>
        <p><a class="btn btn--primary" href="tel:+12606025134">(260) 602-5134</a></p>
        <p><a href="mailto:steelers6615@gmail.com">steelers6615@gmail.com</a></p>
        <p class="muted">Either Cubmaster can answer anything. Reach whichever one you get first.</p>
      </div>
      <div class="card card--accent">
        <h3>The pack inbox</h3>
        <p class="muted" style="margin-top:-.5rem"><strong>Goes to pack leadership</strong></p>
        <p><a class="btn btn--solid" href="mailto:cubpack3049@gmail.com">cubpack3049@gmail.com</a></p>
        <p class="muted">Best for anything that is not urgent, and where completed registration forms arrive.</p>
      </div>
      <div class="card card--accent">
        <h3>Come to a meeting</h3>
        <p><strong><a href="https://cedarcreekchurch.com">Cedar Creek Church</a></strong><br>
        12606 Leo Road<br>
        Fort Wayne, IN 46845</p>
        <p class="muted">Our home church, and where the pack meets.</p>
        <p>Mondays at 6:30 PM during the school year. Walk in, ask for a Cub Scout leader, and someone will find you.</p>
        <p><a href="https://maps.google.com/?q=12606+Leo+Rd,+Fort+Wayne,+IN+46845">Get directions</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <h2>Stay connected</h2>
    <div class="link-tiles">
      <a class="link-tile" href="{facebook}">
        <strong>Facebook group</strong>
        <span>Cub Scout Pack 3049. Photos, announcements, and event reminders for pack families.</span>
      </a>
      <a class="link-tile" href="{band}">
        <strong>BAND app, pack group</strong>
        <span>"Cub Scouts Pack 3049" on BAND. Where den leaders post weekly reminders, sign up sheets, and last minute changes. Open the invite on your phone or desktop to join.</span>
      </a>
      <a class="link-tile" href="https://cedarcreekchurch.com">
        <strong>Cedar Creek Church</strong>
        <span>Our home church and meeting place, 12606 Leo Road. Service times, directions, and what else happens there.</span>
      </a>
      <a class="link-tile" href="https://maps.google.com/?q=14133+Leo+Rd,+Leo,+IN+46765">
        <strong>American Legion Post 409</strong>
        <span>Jack Brinker Post, 14133 Leo Road. Our chartered organization, and the reason this pack exists.</span>
      </a>
      <a class="link-tile" href="https://www.awac.org/">
        <strong>Anthony Wayne Area Council</strong>
        <span>Our local council. District events, camp registration, training, and council calendars.</span>
      </a>
      <a class="link-tile" href="https://www.scouting.org/">
        <strong>Scouting America</strong>
        <span>National program information, adult training, and the Annual Health and Medical Record.</span>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid--2">
      <div>
        <h2>Pack leadership</h2>
        <p class="muted">Start with either Co-Cubmaster. They will point you to the right person.</p>
        <ul class="leader-list">
          <li><span class="role">Co-Cubmaster</span><span class="name">Nicole Howard</span><br>
            <a href="tel:+12605572243">(260) 557-2243</a> &middot; <a href="mailto:howardfamily411@gmail.com">howardfamily411@gmail.com</a></li>
          <li><span class="role">Co-Cubmaster</span><span class="name">Dan Noll</span><br>
            <a href="tel:+12606025134">(260) 602-5134</a> &middot; <a href="mailto:steelers6615@gmail.com">steelers6615@gmail.com</a></li>
          <li><span class="role">Committee Chair</span><span class="name">Michael Bechill</span><br>
            <span class="muted">Pack administration, popcorn, and camp logistics.</span></li>
          <li><span class="role">Assistant Cubmaster</span><span class="name">Nick Schall</span></li>
          <li><span class="role">Treasurer</span><span class="name">Jenni McAlexander</span></li>
          <li><span class="role">Secretary</span><span class="name">Dan Noll</span></li>
          <li><span class="role">Popcorn Kernel</span><span class="name">Michael Bechill</span><br>
            <span class="muted">Assistant Kernel: Tammy Swanson</span></li>
          <li><span class="role">Camp Coordinators</span><span class="name">Chad McAlexander and Seth Hughes</span></li>
          <li><span class="role">Den Leaders</span><span class="name">Tigers, Wolves, Bears, Webelos, Arrow of Light</span><br>
            <span class="muted">One per den, introduced when your Scout joins. The Lion den leader position is currently open.</span></li>
          <li><span class="role">We are looking for help with</span><span class="name">Lion Den Leader, Pack Trainer, Assistant Treasurer, Advancement Coordinator</span><br>
            <span class="muted">If any of those sound like you, tell a Cubmaster, or start the <a href="register.html#adult">adult application</a>. Most of these take less time than you would think.</span></li>
        </ul>
        <p class="muted" style="margin-top:1rem">Interested in helping? The pack always has open positions, and most of them take less time than you would think.</p>
      </div>
      <div>
        <h2>Our chartered organization</h2>
        <div class="card card--accent">
          <h3>Jack Brinker American Legion Post 409</h3>
          <p>14133 Leo Road<br>Leo, IN 46765</p>
          <p><a href="tel:+12606272628">(260) 627-2628</a></p>
          <p>Every Scouting unit is owned by a chartered organization that provides its charter, its leadership approval, and a home in the community. Pack 3049 is chartered by Post 409, and the Legion has stood behind this pack and the young people of Leo for decades.</p>
          <p class="muted">If you are a veteran looking for a way to serve again, they would like to meet you.</p>
          <p><a href="https://maps.google.com/?q=14133+Leo+Rd,+Leo,+IN+46765">Get directions</a></p>
        </div>
      </div>

      <div>
        <h2>Anthony Wayne Scout Shop</h2>
        <div class="card">
          <p>Uniforms, handbooks, patches, neckerchiefs, and gear. Same building as the council service center.</p>
          <p><strong>8315 W. Jefferson Boulevard</strong><br>Fort Wayne, IN 46804</p>
          <p><a href="tel:+12604329593">(260) 432-9593</a></p>
          <p><strong>Hours</strong><br>
          Monday to Friday, 8:30 AM to 5:00 PM<br>
          Saturday, 9:00 AM to 1:00 PM</p>
          <p class="muted">Call ahead for rank specific items or hard to find sizes. Ask about Pack 3049 in the Pokagon District so your unit numerals and district patch are right.</p>
          <p><a href="https://maps.google.com/?q=8315+W+Jefferson+Blvd,+Fort+Wayne,+IN+46804">Get directions</a></p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="narrow center">
    <h2>Thinking about joining?</h2>
    <p>Start on the <a href="join.html">join page</a>, then come see us on a Monday.</p>
    <p><a class="btn btn--primary" href="register.html">Register a Scout</a></p>
  </div>
</section>
""".replace("{facebook}", FACEBOOK).replace("{band}", BAND),
)

# ---------------------------------------------------------------- REGISTER
PAGES["register.html"] = (
    "Register | Cub Scout Pack 3049",
    "Register a Scout with Cub Scout Pack 3049 in Leo, Indiana. The official Scouting America youth application, filled out on your phone in about five minutes.",
    """
<section class="hero hero--page">
  <div class="wrap">
    <span class="eyebrow">Registration</span>
    <h1>Sign your Scout up</h1>
    <p class="lede">One form, about five minutes, and nothing due today. A leader follows up about your Scout's den and meeting nights.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <section class="reg" id="register">
      <span class="reg__tag">Registration is open</span>
      <h2>Join Pack 3049 in about five minutes</h2>
      <p class="reg__lede">Answer the questions in plain language on your phone. We fill out the
         official Scouting America youth application for you, then email the completed, signed PDF
         to you and to <a href="mailto:cubpack3049@gmail.com">cubpack3049@gmail.com</a>. No printing,
         no form numbers, no paperwork to hand back at a meeting.</p>
      <div class="reg__grid">
        <ol class="reg__steps">
          <li><b>Have two things handy</b>
              <span>Your Scout's date of birth and the school and grade they are in this year.</span></li>
          <li><b>Answer the questions</b>
              <span>Plain language, no form numbers. Sign at the end with your finger.</span></li>
          <li><b>Watch your inbox</b>
              <span>The finished application arrives as a PDF for your records, the pack gets its
              copy at the same time, and a leader reaches out about your Scout's den and meeting nights.</span></li>
        </ol>
        <div class="reg__cta">
          <a class="reg__btn" href="__YOUTH_APPLICATION_URL__">Start the application</a>
          <p class="reg__note">Takes about five minutes. Nothing is due today.</p>
          <a class="reg__alt" id="adult" href="__ADULT_APPLICATION_URL__">Volunteering too? Adult application</a>
        </div>
      </div>
      <p class="reg__fine">No payment is collected online. A leader follows up about the national
         registration fee, the council fee, and pack dues, and about the ways we help families who
         need it. Questions before you sign up? Call or email a Cubmaster on the
         <a href="contact.html">contact page</a>.</p>
    </section>

  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <span class="eyebrow">While you are here</span>
    <h2>What happens next</h2>
    <div class="grid grid--3">
      <div class="card card--accent">
        <h3>You get an email</h3>
        <p>The completed application arrives as a PDF for your records, and the same file lands in the pack inbox at <a href="mailto:cubpack3049@gmail.com">cubpack3049@gmail.com</a>. Nothing to print, nothing to hand in.</p>
      </div>
      <div class="card card--accent">
        <h3>A leader reaches out</h3>
        <p>One of the Cubmasters will contact you about your Scout's den, which Mondays they meet, and what to bring the first night. Which is nothing.</p>
      </div>
      <div class="card card--accent">
        <h3>Adults register separately</h3>
        <p>Any parent who will be a den leader, drive to camp, or stay overnight fills out their own <a href="#adult">adult application</a>. It runs the same way and takes about as long.</p>
        <p class="muted">We do not ask for your Social Security number online. Council needs one for the background check, so a leader asks you for it in person when the form is submitted.</p>
      </div>
      <div class="card card--accent">
        <h3>Then you just show up</h3>
        <p>Mondays at 6:30 PM at Cedar Creek Church. Come in regular clothes. We will sort out the uniform once your Scout has decided they like it here.</p>
      </div>
    </div>
    <div class="callout callout--info">
      <p><strong>Not ready to sign up yet?</strong> That is completely fine. Read <a href="join.html">what it costs and what a year looks like</a>, check the <a href="calendar.html">calendar</a>, or just come to a Monday meeting and watch. Nobody will pressure you.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="narrow center">
    <h2>Questions before you sign up?</h2>
    <p>Call or email either Co-Cubmaster. They would rather answer a question now than have you wonder.</p>
    <CONTACTS_HERE>
  </div>
</section>
""".replace("<CONTACTS_HERE>", CONTACTS),
)

# ---------------------------------------------------------------- 404
PAGES["404.html"] = (
    "Page not found | Cub Scout Pack 3049",
    "That page could not be found.",
    """
<section class="hero hero--page">
  <div class="wrap">
    <span class="eyebrow">404</span>
    <h1>This trail dead ends</h1>
    <p class="lede">The page you were looking for is not here. Try one of these instead.</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="index.html">Back to the home page</a>
      <a class="btn btn--ghost" href="register.html">Register a Scout</a>
      <a class="btn btn--ghost" href="contact.html">Contact a leader</a>
    </div>
  </div>
</section>
""",
)
