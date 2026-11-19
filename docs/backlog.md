# Backlog

Open work that needs a decision, content, or a change outside this repo. Remove an item in the change
that closes it; record any decision it took in [decisions](decisions.md).

| ID | Item | Blocked on |
|---|---|---|
| H1 | Response headers GitHub Pages cannot set: year-long `immutable` cache on fingerprinted files and fonts (today `max-age=600`), brotli, HSTS, `X-Content-Type-Options`, `Referrer-Policy`. Done when Lighthouse cache audits pass and Mozilla Observatory grades A. | Whether to put Cloudflare in front of Pages (DNS change) or move to Cloudflare Pages with a `_headers` file. |
| A1 | `scripts/audit.py` fails every page here at performance 89–91 because local Lighthouse reports a speed index near 13 s, and `https://example.com` gets the same (13.9 s, Chrome 157 headless). PageSpeed Insights gives the home page, the resume and the newest report 100. Done when the audit measures speed index correctly. | Finding why headless Chrome paints about 9 s late on this machine. |
| B8 | Report generators: `assets/reports/hydro-quebec-outage.html` loads full Plotly 2.32.0 from `cdn.plot.ly` (self-host `plotly-cartesian`), repeats the default template per chart, carries thousands of long decimals. The forecast heatmap caption says "darker" while every cell is one blue. One structure for both report articles. | The generators live outside this repo. |
| B13 | 7 of 10 projects are `active` ("In progress"), including ones with a live link. | Content, and a definition of `active`. |
| B17 | The RAG workflow SVG in `content/tech/rag-montreal-pools/index.md` scales its labels to about 6px on phones. | Content. |
| B18 | Three MemoryTracer screenshots are stored twice (~324 KB): the project gallery (`content/projects/memorytracer/gallery/`) and byte-identical copies in the two Windows memory articles. Found by the Nov 17, 2026 consolidation audit (issue #23). | Kept while page bundles stay self-contained — the figure shortcode and the project gallery read bundle resources only. Revisit if a shared-image mechanism ever lands. |
| B19 | Decide how Rekba and TikiPro are presented on the site: keep, de-emphasize from the homepage flow, or remove — options and trade-offs in [rekba-tikipro-presentation](rekba-tikipro-presentation.md). Raised by the Nov 17, 2026 consolidation sprint (issue #23, workstream 6); nothing changes until it is decided. | Founder decision. |
