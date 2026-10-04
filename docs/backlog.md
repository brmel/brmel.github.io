# Backlog

Open work that needs a decision, content, or a change outside this repo. Remove an item in the change
that closes it; record any decision it took in [decisions](decisions.md).

| ID | Item | Blocked on |
|---|---|---|
| H1 | Response headers GitHub Pages cannot set: year-long `immutable` cache on fingerprinted files and fonts (today `max-age=600`), brotli, HSTS, `X-Content-Type-Options`, `Referrer-Policy`. Done when Lighthouse cache audits pass and Mozilla Observatory grades A. | Whether to put Cloudflare in front of Pages (DNS change) or move to Cloudflare Pages with a `_headers` file. |
| B7 | `https://www.ibraverse.ca` fails TLS: the certificate does not cover `www`. Point the `www` CNAME at `brmel.github.io` so Pages issues one. | DNS. |
| B8 | Report generators: `assets/reports/hydro-quebec-outage.html` loads full Plotly 2.32.0 from `cdn.plot.ly` (self-host `plotly-cartesian`), repeats the default template per chart, carries thousands of long decimals and folium maps with a CARTO "API key required" watermark. The forecast heatmap caption says "darker" while every cell is one blue. One structure for both report articles. | The generators live outside this repo. |
| B9 | Consent: Québec Law 25 expects tracking that can profile a visitor to be off by default; analytics loads for everyone. | Owner decision on a consent choice. |
| B10 | The home `<title>` is "Ibraverse" alone in every language. | Needs a fork of PaperMod's `head.html` (see decisions, titles). |
| B11 | Search results render from the theme's `fastsearch.js` as title and "»" only; matching the list-card look needs a fork of that script. | Decision on forking the script. |
| B12 | Project cards carry no image (9 of 12 projects have a gallery); field notes have no photos. | Content. |
| B13 | Resume video posters read as stock; 7 of 12 projects are `active` ("In progress"), including ones with a live link. | Content, and a definition of `active`. |
| B14 | About 45% of the theme's CSS rules match nothing; trimming them means overriding theme CSS files. | Decision; the single bundle stays (see decisions). |
| B15 | Facts to confirm in the copy: "~17.4 million TB" for 2^64 bytes (it is 18.4 million TB or 16 million TiB) and "~16 TB" of x64 user space (128 TB today) in both Windows memory articles; `M_IMAGE`/`M_READ` where Windows uses `MEM_IMAGE`/`PAGE_READONLY` in the deep dive; MemoryTracer spelled three ways across the two articles; "local model option (Example 2)" and the undefined "TNV" in the Domia article; "dark as foreground colour" in barcode-flight while the image shows light bars; Leorra's lede says it never shipped while a lesson says it did; Farkad's "six pillars" vs "areas". | Owner. |
| B16 | `/ar/tags/` and `/fr/tags/` list topic names and links from the English site; the Arabic home feed shows English tag names. | Decision on translating topic names. |
| B17 | The RAG workflow SVG in `content/tech/rag-montreal-pools/index.md` scales its labels to about 6px on phones. | Content. |
| B18 | Notch safe areas need `viewport-fit=cover`, and a dark `theme-color` needs to follow the theme toggle; both mean forking PaperMod's `head.html` or a line of JS. | Decision on the fork. |
