import glob, os, sys, tomllib

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
PUB = os.path.join(ROOT, "public")
CONFIG = tomllib.load(open(os.path.join(ROOT, "config.toml"), "rb"))
BASE = CONFIG["baseURL"].rstrip("/")
SECTIONS = CONFIG["params"]["mainSections"]
LANGS = [lang for lang in CONFIG["languages"] if lang != CONFIG["defaultContentLanguage"]]


def pages(name="*.html"):
    for path in sorted(glob.glob(os.path.join(PUB, "**", name), recursive=True)):
        rel = os.path.relpath(path, PUB)
        html = open(path, encoding="utf-8", errors="ignore").read()
        if rel.startswith("reports" + os.sep) or "http-equiv=refresh" in html[:800]:
            continue
        yield rel, html


def url_of(rel):
    return "/" + rel.replace(os.sep, "/").removesuffix("index.html")


def finish(fails, ok):
    if fails:
        print(f"\n❌ {len(fails)} problem(s):")
        for f in fails:
            print("  " + f)
        sys.exit(1)
    print("✅ " + ok)
