---
title: "Hydro-Québec Outage Analysis"
date: 2026-06-01
draft: false
layout: "standalone"
hideAutoHeader: true
fullBleed: true
summary: "A two-month reliability study of Hydro-Québec's public outage feed — regional reliability, Montréal boroughs, ETA accuracy, causes, and the data pipeline behind it. Interactive charts + map."
tags: ["Data Analysis", "Plotly", "Hydro-Québec", "Reliability", "Web Scraping"]
# English-only by design: no index.fr.md / index.ar.md, and the standalone
# layout carries no language switcher, so this article never appears translated.
---

<!-- The report is a self-contained HTML document (Plotly charts, Leaflet map,
     inline data) served verbatim from /static/reports/. It's embedded in an
     isolated iframe so it renders exactly as generated, with no CSS/JS clash
     against the site. The standalone layout supplies the brand top nav, footer,
     SEO, and Google Analytics around it. -->

<iframe id="hydroReport"
        class="report-frame"
        src="/reports/hydro-quebec-outage-2026-06-01.html"
        title="Hydro-Québec Outage Reliability Report"
        loading="lazy"></iframe>

<style>
  .report-frame { width: 100%; border: 0; display: block; min-height: 100vh; background: var(--bg); }
</style>

<script>
  (function () {
    var f = document.getElementById('hydroReport');
    if (!f) return;
    function fit() {
      try {
        var d = f.contentWindow.document;
        var h = Math.max(d.documentElement.scrollHeight, d.body.scrollHeight);
        if (h > 200) f.style.height = h + 'px';
      } catch (e) {}
    }
    f.addEventListener('load', function () {
      fit();
      // Plotly/Leaflet lay out after load — re-fit, and observe further changes.
      [200, 600, 1500, 3000].forEach(function (t) { setTimeout(fit, t); });
      try { new ResizeObserver(fit).observe(f.contentWindow.document.body); } catch (e) {}
    });
    window.addEventListener('resize', fit);
  })();
</script>
