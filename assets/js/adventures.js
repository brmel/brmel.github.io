/* ============================================================================
   IBRAVERSE — ADVENTURES  (js/adventures.js)
   Two behaviours for /adventures/ articles, both progressive-enhancement:
   1. Reels: click a card to load its embed (YouTube inline; IG/TikTok open in
      a new tab). Nothing third-party loads until the visitor asks for it.
   2. Reveal: fade/slide elements marked .reveal as they scroll into view
      (CSS handles the motion + honours prefers-reduced-motion).
   ========================================================================== */
(function () {
  // --- reels: click to load ---
  document.querySelectorAll('.reel').forEach(function (reel) {
    reel.addEventListener('click', function () {
      if (reel.classList.contains('is-playing')) return;
      var embed = reel.getAttribute('data-embed');
      var href = reel.getAttribute('data-href');
      if (embed) {
        var f = document.createElement('iframe');
        f.src = embed;
        f.loading = 'lazy';
        f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
        f.setAttribute('allowfullscreen', '');
        reel.appendChild(f);
        reel.classList.add('is-playing');
      } else if (href) {
        window.open(href, '_blank', 'noopener');
      }
    });
  });

  // --- reveal on scroll ---
  if (!('IntersectionObserver' in window)) return;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -10% 0px' });
  document.querySelectorAll('.adventures .reveal').forEach(function (el, i) {
    el.style.transitionDelay = (i * 60) + 'ms';
    io.observe(el);
  });
})();
