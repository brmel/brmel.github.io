/*
 * Operating Protocol — page interactions
 *
 *  - data-theme toggle persisted in localStorage; falls back to OS
 *  - smooth anchor scroll that respects the sticky topbar height
 */
(function () {
  'use strict';

  var root  = document.documentElement;
  var THEME = 'protocol-theme';

  var resolveTheme = function () {
    return root.getAttribute('data-theme') ||
      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  };

  var stored = localStorage.getItem(THEME);
  if (stored === 'dark' || stored === 'light') root.setAttribute('data-theme', stored);

  var toggle = document.querySelector('[data-theme-toggle]');
  if (toggle) {
    var paint = function () {
      var t = resolveTheme();
      toggle.textContent = t === 'dark' ? '☀' : '☾';
      toggle.setAttribute('aria-label', t === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    };
    paint();
    toggle.addEventListener('click', function () {
      var next = resolveTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem(THEME, next); } catch (e) {}
      paint();
    });
  }

  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href').slice(1);
      if (!id) return;
      var target = document.getElementById(id);
      if (!target) return;
      e.preventDefault();
      var bar    = document.querySelector('.topbar');
      var offset = bar ? bar.getBoundingClientRect().height + 8 : 0;
      var top    = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top: top, behavior: 'smooth' });
      history.replaceState(null, '', '#' + id);
    });
  });
})();
