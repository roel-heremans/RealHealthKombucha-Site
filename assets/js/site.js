// Real Health Kombucha — small progressive enhancements (no dependencies).
(function () {
  "use strict";

  // Phone/tablet menu toggle.
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".menu-toggle");
  if (header && toggle) {
    var setOpen = function (open) {
      header.classList.toggle("nav-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    };
    toggle.addEventListener("click", function () {
      setOpen(!header.classList.contains("nav-open"));
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setOpen(false);
    });
    document.addEventListener("click", function (e) {
      if (!header.contains(e.target)) setOpen(false);
    });
  }

  // Flavour carousel: native horizontal scroll (works without JS);
  // arrows step one card, dots follow the scroll position.
  document.querySelectorAll("[data-carousel]").forEach(function (root) {
    var track = root.querySelector(".carousel-track");
    var cards = track.children;
    var dots = root.querySelectorAll(".carousel-dots span");
    var current = function () {
      var best = 0, min = Infinity;
      for (var i = 0; i < cards.length; i++) {
        var d = Math.abs(cards[i].offsetLeft - track.offsetLeft - track.scrollLeft);
        if (d < min) { min = d; best = i; }
      }
      return best;
    };
    var atEnd = function () { return track.scrollLeft >= track.scrollWidth - track.clientWidth - 2; };
    var update = function () {
      var c = atEnd() ? cards.length - 1 : current();
      dots.forEach(function (dot, i) { dot.classList.toggle("is-active", i === c); });
    };
    var go = function (step) {
      var n = cards.length;
      var i = (current() + step + n) % n;
      if (step > 0 && atEnd()) i = 0;                          // wrap to the first card
      if (step < 0 && track.scrollLeft <= 2) i = n - 1;        // wrap to the end
      track.scrollTo({ left: cards[i].offsetLeft - track.offsetLeft, behavior: "smooth" });
    };
    var prev = root.querySelector(".carousel-prev");
    var next = root.querySelector(".carousel-next");
    if (prev) prev.addEventListener("click", function () { go(-1); });
    if (next) next.addEventListener("click", function () { go(1); });
    track.addEventListener("scroll", update, { passive: true });
    update();
  });

  // Opt-in fade-up on scroll: add data-reveal to an element.
  var items = document.querySelectorAll("[data-reveal]");
  if (!("IntersectionObserver" in window)) {
    items.forEach(function (el) { el.classList.add("is-visible"); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        io.unobserve(entry.target);
      }
    });
  }, { rootMargin: "0px 0px -10% 0px" });
  items.forEach(function (el) { io.observe(el); });
})();
