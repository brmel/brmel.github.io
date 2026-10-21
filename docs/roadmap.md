# Roadmap

Open work that needs the owner. Each item comes from what comparable sites do well (Karpathy,
Lilian Weng, Bruce Dawson, Julia Evans, Dan Luu, Daniel Lemire, Fabien Sanglard and others). Ship a
step, run `./scripts/check.sh` and the `verify-site` skill, record any decision in
[decisions](decisions.md), and delete the item here.

## Still open (owner)

1. **Projects as results.** One metric per project against a baseline, one "considered and
   rejected" line, a year range, and a sentence defining `active` (B13). Sources:
   [Discord](https://discord.com/blog/how-discord-stores-trillions-of-messages),
   [Notion](https://www.notion.com/blog/sharding-postgres-at-notion),
   [MacWright](https://macwright.com/projects/).
2. **Tech articles as evidence.** A "measured on" sentence (machine, OS build, tool versions) where
   there are numbers; references on the articles that have none; one companion code repo with a
   folder per article; Compiler Explorer links under the C++ snippets. Footnote styles land with the
   first article that uses a footnote. Sources: Daniel Lemire, Fabien Sanglard, Arthur O'Dwyer.
3. **A rating scale** on the Adventures index: what 3, 4 and 5 mean. Source:
   [The Infatuation](https://www.theinfatuation.com/ratings-explainer).

## Open choices for the owner

| Choice | Trade-off |
|---|---|
| One quiet way to reach you (email on the resume, or an issue link) | every site above has one; without it nobody can report an error |
| A visible feed link (footer or Tech index) | the one subscription channel that needs no social account |
| Tech as a dated title list instead of cards, once it passes about 20 articles | how Karpathy, Sanglard, Luu and Aras list writing |
| A licence line for code snippets | the copy button invites copying; say whether readers may |
| An AI-assistance note on pages an LLM helped edit | Matt Godbolt's one-line form |
| Cite-this lines on reference articles (ellipse, edge measurement) | Lemire, Lilian Weng, Eugene Yan |
