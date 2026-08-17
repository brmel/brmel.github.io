# Comments

Comments run on [giscus](https://giscus.app), which stores every thread as a
GitHub Discussion in this repository.

## Why this and not something else

| | |
|---|---|
| **No tracking, no ads** | Disqus is both. This site's only other third-party script is analytics; adding an ad network to it would undo that. |
| **No backend** | Static site on GitHub Pages. Anything with a database is a service to run, secure and pay for. |
| **The audience already has accounts** | Readers arriving from a C++ memory article or a scikit-learn bug report use GitHub daily. |
| **Threads live next to the work** | A discussion about an article sits beside the issue and the commit it produced. |

## It is off until you turn it on

`layouts/partials/comments.html` renders **nothing** unless every id below is
filled in. A half-configured widget can never ship.

## Enabling it

Discussions is on, the ids below are filled in, and the widget is written and
styled. One step is left, and it needs a human with repo access:

1. **Install the giscus app**: <https://github.com/apps/giscus> → Configure →
   grant it `brmel/brmel.github.io`. Until this is done the widget answers
   *"giscus is not installed on this repository"*.
2. **Flip the flag**: `enabled = true` in `[params.comments]`.

Already done, for the record:

| | |
|---|---|
| Discussions | enabled on the repository |
| Category | `Announcements` — only the owner opens a thread, readers reply |
| `repoId` | `R_kgDOPJVQtA` |
| `categoryId` | `DIC_kwDOPJVQtM4DDjn9` |

## Where it appears

`params.comments.sections` decides, and it lists projects, tech, thoughts and
adventures. The resume, the home page and every section index are excluded: a
comment box under a CV is an invitation nobody wants to accept.

A single page can still opt out with `comments: false` in its front matter.

## Theme and language

`assets/js/comments.js` builds the widget at runtime rather than in the
template, because the theme is a runtime fact: a static `data-theme` would load
the thread in light and flip it a beat later for anyone reading in dark. The
same script keeps the iframe in step when the toggle is used, and the language
comes from the page, so `/fr/` and `/ar/` load their own.
