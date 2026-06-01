/* ============================================================================
   IBRAVERSE — ADVENTURES  (js/adventures.js)
   Reels: click a card to load its embed (YouTube inline; IG/TikTok open in a
   new tab). Nothing third-party loads until the visitor asks for it.
   ========================================================================== */
(function () {
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
})();
