# Voice

How the site's copy sounds in English, French and Arabic, for writing new copy and for editing
existing copy. It covers page bodies, front-matter strings (`title`, `description`, `pitch`, `lede`,
`lessons`, resume entries), `i18n/*.yaml` and the descriptions in `config.toml`.

## 1. Who is writing

1. Brahim, a senior C++ developer in Montréal (Matrox Imaging, then Zebra), writing in the first
   person about work he did himself.
2. The reader is another engineer: a hiring manager who codes, a peer from C++ or machine vision, a
   student from Algiers or Polytechnique.
3. Plain and chronological: what the problem was, what he tried, what he measured, what broke, what
   he would do again.
4. Confident about what he measured and modest about the rest. Claims rest on numbers; adjectives
   and slogans are cut.
5. Trilingual, and it shows a little. Correct but slightly non-native phrasing is part of the voice
   and stays.

Models in the repo: the body of `content/tech/scikit-learn-kmeans-infinite-loop/index.md` ("I
noticed that a weird behaviour happens…", "resolved quickly, in my opinion"), the story in
`content/tech/barcode-flight/index.md` ("The security guy told me…") and the middle of
`content/tech/windows-memory-management-overview/index.md`. Openers, closers and lesson leads are
where the tells below collect.

## 2. Rules for every language

### Facts are fixed

- Never change a fact, number, unit, date, name, claim, link or meaning. Never strengthen or weaken a
  claim: "the only way" stays "the only way", "most" never becomes "all".
- Never invent experiences, opinions, anecdotes, jokes, hedges or numbers. Deleting is allowed.
- Edit each language on its own terms. Do not retranslate FR or AR from EN, and do not copy a sentence
  that exists in one language into another.
- Fix clear errors (typos, agreement, a wrong term). Leave non-native phrasing that reads fine ("Your
  feedback and inputs are very welcome").

### Editing existing copy

- The unit of change is a sentence or a clause. Do not restructure a section, reorder paragraphs or
  merge bullets.
- If more than about a quarter of a paragraph's sentences have changed, it is a rewrite: back off.
- Rename a heading only when it is clearly a tell, and grep for links to its anchor first.

### Never touch

Front-matter keys and YAML structure (`>-`, `|-`, nesting, quoting); code blocks and inline code;
shortcodes; URLs, link targets and image paths; product and module names (Aurora Imaging Library,
Model Finder, MemoryTracer, VMMap, GTest, UR10e); resume `period` ranges (`2024 — Present`);
`Author — [Title](url)` source lines; metric `value`s, `rating`, `date`, `aliases`; the Markdown
structure (headings, lists, bold lesson leads).

- When `pitch` and `description` are identical, keep them identical.
- Inside double-quoted YAML strings (`lessons`), escape any inner `"`. Never introduce an unquoted
  `: ` in a plain scalar.
- After each file, digits and URLs must be unchanged; this prints nothing when they are:

```bash
diff <(git show HEAD:FILE | grep -oE '[0-9]+([.,][0-9]+)*|https?://[^ )"]+') \
     <(grep -oE '[0-9]+([.,][0-9]+)*|https?://[^ )"]+' FILE)
```

### Tells to cut

| Tell | Example | Fix |
|---|---|---|
| An aphorism closing a paragraph or lesson | "A memory tool that has never been compared to a known-good one is a number generator." | Delete it when the sentence before already proved the point; otherwise state the concrete consequence. |
| "X, not Y" antithesis | "a correctness fix, not an optimisation" | At most one per page. Say the X plainly. |
| Em dash as all-purpose glue | "— and found two I had wrong." | At most one per paragraph. Use a comma, colon, parentheses or a full stop. |
| "The X is the point / the product" | "The failure case is the point." | Say what is meant: "is what I wanted to show". |
| Stiff or throat-clearing openers | "What that consists of:", "Here is how hard it is to say…" | Start with the fact or the event. |
| Intensifiers | "actually", "exactly", "genuinely" | Cut them unless they contrast with a belief stated earlier. |
| Impersonal "The work …" | "The work spans the whole stack" | Use "I …". |
| Uncontracted negatives everywhere (EN) | "does not", "cannot", "is not" in every sentence | Contract where you would say it aloud, especially in stories. |
| Marketing adjectives | "world-class", "spectacular", "hidden gem", "must-visit" | Drop the adjective. |
| Tricolons and mirrored clauses | "everything you can change is data, everything you can replace sits behind one interface" | Keep one if it carries facts. Never add one. |

### What to keep

- Chronology and the first person: "I noticed", "I tried", "I checked", "I filed".
- Numbers with their unit and context ("Twenty verified findings on a real site in 215 ms").
- Honest hedges already there ("in my opinion", "I think"). Add no new ones.
- Specific nouns: the module, the API, the tool, the trail junction.
- Short connectives a person uses: "So", "But", "Then", "That's why"; in Arabic «فـ»، «لكن»، «ثم»، «لذلك».

### Per section

| Section | What the copy does |
|---|---|
| Home, resume | States verifiable facts in the first person. No adjective that would not survive an interview. |
| Projects | Says what problem, for whom, why it was built and what it became, for a reader who has never heard of it. README prose is written for contributors and is never reused. Lessons include at least one real failure. |
| Tech | Teaches one thing with the real image, measurement and code. |
| Adventures | Gives one genuine con per piece and a verdict. Field-note and social formats: [voice-tone](brand-kit/01-guides/voice-tone.md). |

## 3. English

- **Introduce yourself in one flat line**: job, place. Julia Evans: "I'm a software developer. I live
  in Montreal."
- **Open with what happened.** Bruce Dawson: "This story begins, as they so often do, when I noticed
  that my machine was behaving poorly."
- **Numbers are measurements in ordinary sentences**, with the unit and the comparison: "24 cores (48
  hyper-threads) and they were 50% idle."
- **Say where your knowledge stops.** Dawson: "I'm not familiar with this part of Windows but…"
- **Humour is dry, rare and aimed at yourself or the bug.** Keep existing humour; add none.
- **Credit people by name.**
- **Headings are labels**: "The bug", "The story", "The product".
- **Posts end on the last fact**, with no moral.
- **Spelling is British/Canadian**: colour, behaviour, optimisation. Never flip to -ize or -or.
- Use contractions in stories and project pages, and at most one em dash per paragraph.

Before → after:

1. "What that consists of:" → "In practice, that means:"
2. "…before trusting any of it — and found two I had wrong. A memory tool that has never been compared
   to a known-good one is a number generator." → "…before trusting any of it, and found two I had wrong."
3. "Here is how hard it is to say how much memory a process is using: the people who build Windows have
   not agreed on it." → "Even the people who build Windows don't agree on how much memory a process is
   using."
4. "A public C++ API is a promise you cannot withdraw." → "Once a C++ API is public, you can't take it
   back."
5. "The useful metric is how it fails, not how often." → "How it fails tells you more than how often it
   fails."

## 4. French (fr-CA)

The main tell in French is calque: English idioms carried over word for word.

- **"Je", in a spoken but correct register.** Dislocation is natural French and breaks an aphorism
  ("Une API publique, on ne peut plus la reprendre"). "ça" in stories, "cela" in the resume.
- **Translate a concept when a French term is in real use; keep the English when nobody agrees on
  one.** Patrice Roy (h-deb.ca) writes "fil d'exécution", "verrou", "tampon" and keeps "mutex",
  "thread-safe". Microsoft's French page on working set uses four different terms, so *working set*
  stays.
- **Use OQLF terms when they are established in use** (courriel, bogue, télécharger, infonuagique).
  Do not force a rare one (*cadriciel*).
- **Fix calques before rhythm**: "toute la pile", "la moitié facile", "ne ressemblent à rien dans un
  diff", "là où vivent réellement les cartes d'embarquement".
- Common nouns stay lowercase in titles and alt text ("Code-barres en mode sombre").

| English | On this site | Basis |
|---|---|---|
| bug / debug | bogue / déboguer | OQLF GDT |
| email | courriel | OQLF GDT |
| race condition | situation de compétition | FR Wikipedia; GDT "concurrence critique" |
| backward compatibility | rétrocompatibilité ("compatibilité ascendante" is ambiguous) | OQLF GDT |
| thread / multithreading | multithreading; *fil d'exécution* when explaining | FR Wikipedia, h-deb.ca |
| working set, build, commit, diff, pipeline, backend, sanitizer | English, no italics | no settled term |
| memory-mapped file | fichier mappé en mémoire | Microsoft FR |
| heap / stack | tas / pile | standard |
| benchmark | banc d'essai | site usage |
| cloud | infonuagique | OQLF |
| QA, UI, API | unchanged, plural "les API" | site usage |

Typography:

- A non-breaking space (U+00A0) before `:`, `;`, `?` and `!`. Never a plain space, never none.
- Quotes are « » with U+00A0 inside.
- Apostrophes match the file being edited (straight `'` in content); do not mass-convert.
- Numbers: "15 000", "3,87/4", "1 %", with U+00A0 as the separator and before `%` and units.
- Dashes are " — " with spaces, and rare.

Before → after:

1. "conditions de course dans une bibliothèque" → "situations de compétition dans une bibliothèque"
2. "j'investigue et corrige des bogues, et j'assiste directement les clients dont les applications
   tombent en production" → "je cherche la cause des bogues et je les corrige, et j'assiste directement
   les clients dont les applications plantent en production"
3. "Les deux ne ressemblent à rien dans un diff." → "Dans un diff, les deux passent inaperçus."
4. "Mais j'ai réalisé : mon téléphone était en mode sombre" → "Puis je me suis rendu compte que mon
   téléphone était en mode sombre"

## 5. Arabic

Modern Standard Arabic, simple and close to how developers write on Hsoub; no literary register, no
darja. The main tell is translated syntax: يتم / قام بـ + verbal noun, English idioms, gender mismatch,
dashes everywhere.

- **Verb first, active voice, first person.** «يُحفَظ كل توقع كبيانات لحظة نشره، ويُتحقَّق منه آليًا»
  (`content/projects/paridata/index.ar.md`) is the house model.
- **Arabic term first, English in parentheses on first mention only**: «تنقيح الأخطاء (debugging)».
- **Product, tool and API names stay in Latin script**: MemoryTracer, VMMap, GTest. Never transliterate.
- **Terminology is not settled, so be consistent within a page.**
- Opening a sentence with و or فـ is natural, and «أما … فـ» is good Arabic. Keep them.

| English | On this site | Basis |
|---|---|---|
| code | الشيفرة; «مراجعة الكود» as a fixed term | Hsoub; Arabic Wikipedia |
| bug / debugging | علّة or خطأ برمجي / تنقيح، تصحيح الأخطاء | Arabic Wikipedia |
| thread / multithreading | خيط / تعدّد الخيوط | Hsoub |
| race condition | حالة تسابق («حالات السباق» acceptable) | Arabic Wikipedia |
| compiler | مصرِّف | Arabic Wikipedia, Hsoub |
| memory leak | تسرّب الذاكرة | Arabic Wikipedia |
| virtual memory / working set | الذاكرة الافتراضية / مجموعة العمل (working set) on first mention | Arabic Wikipedia |
| regression testing | اختبار الانحدار | Arabic Wikipedia |
| machine vision / concurrency | الرؤية الآلية / التزامن | Arabic Wikipedia |
| barcode | الباركود | common usage |

Punctuation, numbers and direction:

- «،» «؛» «؟» inside Arabic sentences, no space before and one after. Quotes are « ».
- Digits stay Western (2019, 15,000, 3.87/4).
- Every `C++` in Arabic text, titles, descriptions and `.ar.md` lists (`stack`, `tools`, `items`) is
  written `‎C++‎` with U+200E marks. Without them the trailing "+" signs take the Arabic direction and
  display as "++C". Lists need it too: `layouts/partials/func/dots.html` joins them into one RTL line.
  Other tokens need it only when they start or end with punctuation (`C#`, `.NET`). Never add marks
  inside URLs, code or shortcodes; count them with `grep -c $'\xe2\x80\x8e'`.

Before → after:

1. «وما يتضمّنه ذلك:» → «عمليًا:»
2. «لذا قمت ببساطة بالتبديل إلى الوضع الفاتح…» → «فبدّلت ببساطة إلى الوضع الفاتح…»
3. «مسألة ذاكرة وإنتاجية قبل أن يكون مسألة تعلّم آلة.» → «مسألةُ ذاكرة وإنتاجية أولًا، ثم مسألةُ تعلّم آلة.»
4. «وكلاهما لا يبدو شيئًا في الفروق.» → «وكلاهما يمرّ دون أن يُلاحَظ عند قراءة التعديلات.»

## 6. Sources

English
- Bruce Dawson: https://randomascii.wordpress.com/about/, https://randomascii.wordpress.com/2017/07/09/24-core-cpu-and-i-cant-move-my-mouse/
- Jeff Preshing: https://preshing.com/about/, https://preshing.com/20120612/an-introduction-to-lock-free-programming/
- Julia Evans: https://jvns.ca/about/, https://jvns.ca/blog/2016/03/16/tcpdump-is-amazing/
- Aras Pranckevičius: https://aras-p.info/, https://aras-p.info/blog/2026/06/28/Joys-of-cancelling-a-TBB-task-group/
- Eli Bendersky: https://eli.thegreenplace.net/pages/about, https://eli.thegreenplace.net/2025/benchmarking-utility-for-python.html
- Fabien Sanglard: https://fabiensanglard.net/, https://fabiensanglard.net/quake_shareware_cd/index.html
- Dan Luu https://danluu.com/about/; Arthur O'Dwyer https://quuxplusone.github.io/blog/about/; Simon Willison https://simonwillison.net/about/ (third-person bio, the counter-example); Satya Mallick https://learnopencv.com/about/
- Raymond Chen's author bio: https://devblogs.microsoft.com/oldnewthing/wp-json/wp/v2/users/1069

French
- OQLF punctuation spacing: https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles
- OQLF GDT: https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/1299091/bogue, https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8353974/courriel, https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8360295/concurrence-critique, https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8371318/retrocompatible
- OQLF on borrowings: https://vitrinelinguistique.oqlf.gouv.qc.ca/25442/les-emprunts-a-langlais/lemprunt-linguistique-definition-contexte-et-traitement
- Microsoft FR, working set: https://learn.microsoft.com/fr-fr/windows/win32/memory/working-set
- Patrice Roy: https://h-deb.ca/, https://h-deb.ca/Sujets/Parallelisme/Verrous-SWMR.html, https://h-deb.ca/Sujets/Divers--cplusplus/allocateurs_pmr.html
- Zeste de Savoir C++ course: https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/
- Collège de Rosemont, OQLF equivalents: https://www.crosemont.qc.ca/wp-content/uploads/2020/10/Anglicismes-dans-linformatique.pdf
- Anglicisms among francophone IT students: https://tidsskrift.dk/her/article/view/152910

Arabic
- Hsoub Academy C++: https://academy.hsoub.com/programming/cpp/ and https://academy.hsoub.com/programming/cpp/اختبار-الوحدات-وأدوات-تنقيح-الشيفرات-وتصحيح-الأخطاء-في-cpp-r1190/
- Hsoub I/O developer posts: https://io.hsoub.com/programming
- Arabic Wikipedia: https://ar.wikipedia.org/wiki/ذاكرة_افتراضية, https://ar.wikipedia.org/wiki/اختبار_الانحدار, and the articles تشعب (حوسبة)، حالة تسابق، خطأ برمجي، تنقيح (حوسبة)، مصرف (حوسبة)
- Wikidata FR/AR titles: https://www.wikidata.org/w/api.php?action=wbgetentities&sites=enwiki&titles=Thread_(computing)|Software_bug|Race_condition|Code_review&props=sitelinks
- Gengo, common Arabic errors: https://gengo.com/ar/translators/resources/most-common-mistakes-en
- W3C, bidi controls: https://www.w3.org/International/questions/qa-bidi-unicode-controls
