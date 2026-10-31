# Backlog

Open work that needs a decision, content, or a change outside this repo. Remove an item in the change
that closes it; record any decision it took in [decisions](decisions.md).

| ID | Item | Blocked on |
|---|---|---|
| H1 | Response headers GitHub Pages cannot set: year-long `immutable` cache on fingerprinted files and fonts (today `max-age=600`), brotli, HSTS, `X-Content-Type-Options`, `Referrer-Policy`. Done when Lighthouse cache audits pass and Mozilla Observatory grades A. | Whether to put Cloudflare in front of Pages (DNS change) or move to Cloudflare Pages with a `_headers` file. |
| B7 | `https://www.ibraverse.ca` fails TLS: the certificate does not cover `www`. Point the `www` CNAME at `brmel.github.io` so Pages issues one. | DNS. |
| B8 | Report generators: `assets/reports/hydro-quebec-outage.html` loads full Plotly 2.32.0 from `cdn.plot.ly` (self-host `plotly-cartesian`), repeats the default template per chart, carries thousands of long decimals. The forecast heatmap caption says "darker" while every cell is one blue. One structure for both report articles. | The generators live outside this repo. |
| B9 | Consent: Québec Law 25 expects tracking that can profile a visitor to be off by default; analytics loads for everyone. | Owner decision on a consent choice. |
| B13 | 7 of 10 projects are `active` ("In progress"), including ones with a live link. | Content, and a definition of `active`. |
| B15 | Facts to confirm in the copy: "local model option (Example 2)", the undefined "TNV", and Perception and Vision disagreeing on when screenshots are taken, in the Domia article; the barcode-flight description says "airport gate" while the story happens at security, and "dark as foreground colour" while the image shows light bars; TikiPro's three languages, now stated nowhere on its page. | Owner. |
| B17 | The RAG workflow SVG in `content/tech/rag-montreal-pools/index.md` scales its labels to about 6px on phones. | Content. |
