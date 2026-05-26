/* Operating Protocol — minimal interactions
   Safe to drop into a PaperMod site; degrades cleanly if removed. */
(function () {
  'use strict';

  // ---- Theme toggle (standalone — PaperMod has its own; remove this block if integrating) ----
  var root = document.documentElement;
  var stored = localStorage.getItem('protocol-theme');
  if (stored === 'dark' || stored === 'light') {
    root.setAttribute('data-theme', stored);
  }

  var btn = document.querySelector('[data-theme-toggle]');
  if (btn) {
    var sync = function () {
      var current = root.getAttribute('data-theme');
      if (!current) {
        current = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      }
      btn.textContent = current === 'dark' ? '☀' : '☾';
      btn.setAttribute('aria-label', current === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    };
    sync();
    btn.addEventListener('click', function () {
      var current = root.getAttribute('data-theme') ||
        (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      var next = current === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      localStorage.setItem('protocol-theme', next);
      sync();
    });
  }

  // ---- Smooth anchor scroll, respecting sticky topbar height ----
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href').slice(1);
      if (!id) return;
      var target = document.getElementById(id);
      if (!target) return;
      e.preventDefault();
      var bar = document.querySelector('.topbar');
      var offset = bar ? bar.getBoundingClientRect().height + 8 : 0;
      var top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top: top, behavior: 'smooth' });
      history.replaceState(null, '', '#' + id);
    });
  });
})();
