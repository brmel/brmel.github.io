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

1. **Make the repository public** if it is not already — giscus reads
   Discussions through the public API.
2. **Enable Discussions**: repo → Settings → General → Features → tick
   *Discussions*.
3. **Create a category for it**: repo → Discussions → Categories → New.
   Name it `Comments` and choose the **Announcements** format, so only you can
   open a thread and readers can only reply. Without this anyone can create
   threads that are not attached to any page.
4. **Install the app**: <https://github.com/apps/giscus> → Configure → grant it
   this repository.
5. **Get the ids**: go to <https://giscus.app>, enter `brmel/brmel.github.io`,
   pick *Discussion title contains page pathname* and the category from step 3.
   The generated snippet contains `data-repo-id` and `data-category-id`.
6. **Fill in `config.toml`**:

   ```toml
   [params.comments]
     enabled    = true
     repo       = "brmel/brmel.github.io"
     repoId     = "R_..."           # from step 5
     category   = "Comments"
     categoryId = "DIC_..."         # from step 5
   ```

7. `./scripts/check.sh` and open any article. The thread appears under the
   section navigation.

## Turning it off for one page

```yaml
comments: false
```

## Theme

giscus runs in an iframe and cannot read this site's CSS, so it is told which
theme to use at load and told again over `postMessage` whenever the reader
toggles. Both halves are needed — without the second, it stays light on a dark
page.
