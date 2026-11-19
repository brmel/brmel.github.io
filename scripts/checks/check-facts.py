#!/usr/bin/env python3
import html, os, re, tomllib
from gate import PUB, ROOT, finish

FACTS = tomllib.load(open(os.path.join(ROOT, "data", "facts.toml"), "rb"))
PERSON = FACTS["person"]


def text_of(path):
    raw = open(path, encoding="utf-8", errors="ignore").read()
    raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    return re.sub(r"\s+", " ", text.replace("\u00a0", " ").replace("\u202f", " ")).strip()


def norm(s):
    return re.sub(r"\s+", " ", s.replace("\u00a0", " ").replace("\u202f", " ")).strip()


fails = []
RESUME = {"en": "resume/index.html", "fr": "fr/resume/index.html", "ar": "ar/resume/index.html"}
HOME = {"en": "index.html", "fr": "fr/index.html", "ar": "ar/index.html"}

for lang, rel in RESUME.items():
    text = text_of(os.path.join(PUB, rel))
    for entry in FACTS["experience"][lang]:
        for field in ("period", "role", "org"):
            want = entry.get(field)
            if want and norm(want) not in text:
                fails.append(f"{rel}: {field} \"{want}\" not on the built page")

for lang, rel in HOME.items():
    text = text_of(os.path.join(PUB, rel))
    name = PERSON["name_ar"] if lang == "ar" else PERSON["name"]
    if norm(name) not in text:
        fails.append(f"{rel}: person name \"{name}\" not on the built home page")

llms = text_of(os.path.join(PUB, "llms.txt"))
for want in (PERSON["name"], PERSON["current_role"], PERSON["current_org"]):
    if norm(want) not in llms:
        fails.append(f"llms.txt: \"{want}\" missing from the citable facts")

kmeans = FACTS["claims"]["kmeans"]
text = text_of(os.path.join(PUB, kmeans["page"]))
for want in kmeans["contains"]:
    if want not in text:
        fails.append(f"{kmeans['page']}: claim \"{want}\" missing")

resume_html = open(os.path.join(PUB, RESUME["en"]), encoding="utf-8", errors="ignore").read()
for url in PERSON["same_as"]:
    if url not in resume_html:
        fails.append(f"resume: sameAs link {url} missing from the built page")

finish(fails, "canonical facts match the built site in EN, FR and AR")
