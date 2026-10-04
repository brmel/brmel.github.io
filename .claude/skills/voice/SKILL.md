---
name: voice
description: Write or edit user-facing copy on the Ibraverse site in English, French or Arabic so it sounds like Brahim, a senior C++ developer talking about his own work, rather than polished AI copy. Use for page bodies, titles, descriptions, pitches, ledes, lessons, resume entries, captions, alt text, i18n strings and the descriptions in config.toml.
---

# Voice

The full guide is [docs/voice.md](../../../docs/voice.md): who is writing, the tells to cut, and the
English, French (fr-CA) and Arabic rules, terminology and typography. Read the section for the
language you are writing before you start.

## Hard rules

- Never change a fact, number, unit, date, name, claim, link target, code block, shortcode, image
  path or front-matter key. Don't strengthen or weaken a claim, and don't invent experiences,
  opinions, anecdotes or numbers.
- Editing is sentence-level. If more than about a quarter of a paragraph's sentences changed, it is a
  rewrite: back off unless a rewrite was asked for.
- Edit each language on its own terms. Don't retranslate French or Arabic from English, and don't
  copy a sentence that exists in only one language into another.
- Cut the tells: closing aphorisms, "X, not Y" more than once a page, em dashes as glue (one per
  paragraph at most), "the X is the point", throat-clearing openers, intensifiers ("actually",
  "genuinely"), "The work…" where "I…" is meant, marketing adjectives.
- Keep the first person, the chronology, the numbers with their units, existing honest hedges, and
  correct but slightly non-native phrasing.
- British/Canadian spelling in English; non-breaking spaces before `: ; ? !` in French;
  `، ؛ ؟ « »` and `‎C++‎` with direction marks in Arabic.

## Check after each file

Digits and URLs must be unchanged unless a fact was deliberately corrected:

```bash
diff <(git show HEAD:<path> | grep -oE '[0-9]+([.,][0-9]+)*|https?://[^ )"]+') \
     <(grep -oE '[0-9]+([.,][0-9]+)*|https?://[^ )"]+' <path>)
```

Then `./scripts/check.sh` (description lengths, uniqueness, valid HTML) and the `verify-site` skill
for any page whose layout could change (titles, labels, i18n strings).
