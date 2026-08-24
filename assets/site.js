/* Pack 3049 - small progressive enhancements. No dependencies. */
(function () {
  "use strict";

  // Mobile nav toggle
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Close" : "Menu";
    });
  }

  // Current year in the footer
  var y = document.querySelectorAll("[data-year]");
  for (var i = 0; i < y.length; i++) {
    y[i].textContent = new Date().getFullYear();
  }

  // Calendar page: dim events that have already passed this program year.
  var rows = document.querySelectorAll("[data-date]");
  var today = new Date();
  today.setHours(0, 0, 0, 0);
  for (var j = 0; j < rows.length; j++) {
    var d = new Date(rows[j].getAttribute("data-date") + "T00:00:00");
    if (!isNaN(d) && d < today) {
      rows[j].style.opacity = "0.5";
    }
  }
})();

/* Event banner: hide itself once the event has passed. */
(function () {
  "use strict";
  var bars = document.querySelectorAll("[data-until]");
  var now = new Date();
  now.setHours(0, 0, 0, 0);
  for (var i = 0; i < bars.length; i++) {
    var d = new Date(bars[i].getAttribute("data-until") + "T23:59:59");
    if (!isNaN(d) && d < now) { bars[i].remove(); }
  }
})();

/* ---------------------------------------------------------------------------
   Buyout calculator.

   The formula is the one the pack has always used, verified against the 2024
   "money owed" letter, where it reproduced all nine published amounts exactly:

       owed = max(0, BUYOUT - sales * RATE)

   Change the four numbers below when the committee sets this year's figures.
   Everything else on the calculator follows from them.
--------------------------------------------------------------------------- */
(function () {
  "use strict";

  var BUYOUT = 200;    // pack program cost per Scout, the full cash buyout
  var RATE   = 0.38;   // pack commission credited on a Scout's sales
  var BACK   = 0.04;   // paid to the Scout as an Amazon gift card
  var CAMP   = 1600;   // free Cub Resident Camp at CCLT
  var CIRCLE = 3000;   // Winner's Circle Club

  var form = document.getElementById("buyout-calc");
  if (!form) { return; }

  var input   = document.getElementById("calc-sales");
  var elCred  = document.getElementById("calc-credit");
  var elOwe   = document.getElementById("calc-owe");
  var elOweBx = document.getElementById("calc-owe-box");
  var elOweK  = document.getElementById("calc-owe-label");
  var elOweN  = document.getElementById("calc-owe-note");
  var elBack  = document.getElementById("calc-back");
  var bar     = document.getElementById("calc-bar");
  var fill    = bar.querySelector("i");
  var next    = document.getElementById("calc-next");
  var reset   = document.getElementById("calc-reset");

  var GOAL = BUYOUT / RATE;   // sales that clear the obligation, about $526

  function money(n) {
    return "$" + Math.round(n).toLocaleString("en-US");
  }

  function store(v) {
    try { window.localStorage.setItem("pack3049-sales", v); } catch (e) {}
  }
  function recall() {
    try { return window.localStorage.getItem("pack3049-sales"); } catch (e) { return null; }
  }

  function milestone(li, amount, sales, label) {
    var hit = sales >= amount - 0.5;   // match the rounded display
    li.className = hit ? "is-hit" : "";
    li.querySelector(".m").textContent = hit ? "Earned" : money(amount - sales);
    li.querySelector(".t").textContent = hit ? label + ", earned" : label;
  }

  function update() {
    var sales = parseFloat(input.value);
    if (isNaN(sales) || sales < 0) { sales = 0; }

    var credit = sales * RATE;
    var owed = Math.max(0, BUYOUT - credit);

    elCred.textContent = money(credit);
    elBack.textContent = money(sales * BACK);
    elOwe.textContent = money(owed);

    if (owed < 0.5) {   // rounds to $0, so call it cleared
      elOweBx.className = "calc__stat calc__stat--clear";
      elOweK.textContent = "You owe nothing";
      elOweN.textContent = "Your Scout's year is paid for. Everything from here is theirs.";
      bar.className = "calc__bar is-clear";
    } else {
      elOweBx.className = "calc__stat calc__stat--owe";
      elOweK.textContent = "Buyout still owed";
      elOweN.textContent = "Or sell " + money((owed / RATE)) + " more and owe nothing.";
      bar.className = "calc__bar";
    }

    fill.style.width = Math.min(100, (sales / GOAL) * 100) + "%";

    var items = next.children;
    milestone(items[0], GOAL, sales, "to cover your year");
    milestone(items[1], CAMP, sales, "to free camp at CCLT");
    milestone(items[2], CIRCLE, sales, "to the Winner's Circle Club");

    store(input.value);
  }

  var saved = recall();
  if (saved !== null && saved !== "") { input.value = saved; }

  input.addEventListener("input", update);
  form.addEventListener("submit", function (e) { e.preventDefault(); update(); });
  reset.addEventListener("click", function () {
    input.value = "";
    store("");
    update();
    input.focus();
  });

  update();
})();

/* ---------------------------------------------------------------------------
   Registration link guard.

   The application URLs arrived as PASTE_..._URL_HERE placeholders. Until real
   ones are in place, make that impossible to miss rather than letting a family
   tap a dead button. Once the href is a real URL this does nothing at all.
--------------------------------------------------------------------------- */
(function () {
  "use strict";
  var links = document.querySelectorAll(".reg a[href]");
  for (var i = 0; i < links.length; i++) {
    var href = links[i].getAttribute("href") || "";
    if (href.indexOf("PASTE_") === -1) { continue; }
    links[i].setAttribute("href", "contact.html");
    links[i].setAttribute("aria-describedby", "reg-unset-" + i);
    var warn = document.createElement("span");
    warn.className = "reg__unset";
    warn.id = "reg-unset-" + i;
    warn.textContent = "This application link has not been set up yet. "
      + "Contact a Cubmaster and they will register your Scout directly.";
    links[i].insertAdjacentElement("afterend", warn);
  }
})();

/* ---------------------------------------------------------------------------
   Event countdown label.

   An element with data-event-date="YYYY-MM-DD" relabels itself against the
   reader's own clock: Tonight, Tomorrow night, This Friday, and so on. Written
   once, correct every day, and it never says "tomorrow" on the day itself.
--------------------------------------------------------------------------- */
(function () {
  "use strict";
  var DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday",
              "Thursday", "Friday", "Saturday"];
  var tags = document.querySelectorAll("[data-event-date]");
  var today = new Date();
  today.setHours(0, 0, 0, 0);

  for (var i = 0; i < tags.length; i++) {
    var parts = (tags[i].getAttribute("data-event-date") || "").split("-");
    if (parts.length !== 3) { continue; }
    var when = new Date(+parts[0], +parts[1] - 1, +parts[2]);
    if (isNaN(when)) { continue; }
    var days = Math.round((when - today) / 86400000);
    var label;
    if (days < 0)       { continue; }              // the removal script handles this
    else if (days === 0) { label = "Tonight"; }
    else if (days === 1) { label = "Tomorrow night"; }
    else if (days < 7)   { label = "This " + DAYS[when.getDay()]; }
    else                 { label = DAYS[when.getDay()] + " the " + when.getDate(); }
    tags[i].textContent = label;
  }
})();
