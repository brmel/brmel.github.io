# Ibraverse

Personal site of Brahim Redouane Mellah, senior C++ engineer in Montréal: resume, projects, technical
articles and field notes in English, French and Arabic. Live at **[ibraverse.ca](https://ibraverse.ca)**.

A Hugo static site on the vendored PaperMod theme, built and deployed to GitHub Pages by
`.github/workflows/site.yml`.

## Run it

Needs Hugo 0.148.0 extended; the checks also need Python 3 and Java.

```bash
hugo server -M         # http://localhost:1313
./scripts/check.sh     # build and every check, as CI runs them
```

## Read next

| Doc | Covers |
|---|---|
| [AGENTS.md](AGENTS.md) | rules, commands and workflow for anyone changing the repo, person or agent |
| [ARCHITECTURE.md](ARCHITECTURE.md) | templates, stylesheets, content model, languages, scripts |
| [docs/brand-guidelines.md](docs/brand-guidelines.md) | mark, eyebrow, colour, type, sections |
| [docs/voice.md](docs/voice.md) | how the copy reads in EN, FR and AR |
| [docs/projects-playbook.md](docs/projects-playbook.md), [docs/adventures-playbook.md](docs/adventures-playbook.md), [docs/paridata-playbook.md](docs/paridata-playbook.md) | publishing a project, a field note, a PariData coupon |
| [docs/decisions.md](docs/decisions.md) | why things are the way they are |
| [docs/backlog.md](docs/backlog.md) | open work |
| [docs/brand-kit/00-README.md](docs/brand-kit/00-README.md) | logo, social templates, channel art |
