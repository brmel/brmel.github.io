# The k-means loop that could never stop

Pillar: Engineering Judgment (3 of 10)
Status: queued — not started

## Working titles

- EN: The k-means loop that could never stop
- FR: La boucle k-means qui ne pouvait jamais s'arrêter
- AR: حلقة k-means التي لا تتوقف أبدًا

## The claim it must end on

scikit-learn issue #28055: three stopping conditions that could never hold
at the same time, so the loop ran forever. Reported from production work;
the fix shipped in scikit-learn 1.4.1 (PR #28165). The piece ends on the
judgment, not the bug: a stopping rule that cannot fire is a bug you ship
on purpose.

## Source material that already exists

- `content/tech/scikit-learn-kmeans-infinite-loop/` — the published article
  and the repro image (EN; FR/AR are part of this package's work).
- The upstream issue and PR, linked from the article.

## The five cuts

1. ibraverse article (EN/FR/AR, `new-article` scaffold)
2. LinkedIn carousel
3. LinkedIn text post (site link in the first comment)
4. Instagram carousel
5. Instagram reel or story + Facebook retelling (FR/AR)
