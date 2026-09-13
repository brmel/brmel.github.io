#!/usr/bin/env python3
import collections, json, os, subprocess, sys, tempfile

BASE = (sys.argv[1] if len(sys.argv) > 1 else "https://ibraverse.ca").rstrip("/")
LIGHTHOUSE = "lighthouse@12.8.2"
LINKINATOR = "linkinator@8.1.0"
PAGES = [
    ("home", "/"), ("home-fr", "/fr/"), ("home-ar", "/ar/"), ("resume", "/resume/"),
    ("projects", "/projects/"), ("project", "/projects/meteodata/"), ("tech", "/tech/"),
    ("article", "/tech/windows-memory-management-deep-dive/"),
    ("report", "/tech/montreal-forecast-reliability/"),
    ("adventure", "/adventures/auberge-estonia-rawdon/"),
    ("thought", "/thoughts/estimates-and-the-five-percent/"), ("search", "/search/"),
]
NOINDEX = {"search"}
CATEGORIES = ("performance", "accessibility", "best-practices", "seo")
BUDGET = {"performance": 98, "accessibility": 100, "best-practices": 100, "seo": 100}
METRICS = ("largest-contentful-paint", "cumulative-layout-shift", "total-blocking-time")
SCORED = ("binary", "numeric", "metricSavings")


def lighthouse(url, preset, out):
    cmd = ["npx", "--yes", LIGHTHOUSE, url, "--output=json", f"--output-path={out}",
           "--quiet", "--chrome-flags=--headless=new"]
    if preset == "desktop":
        cmd.append("--preset=desktop")
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    report = json.load(open(out))
    scores = {c: round(report["categories"][c]["score"] * 100) for c in CATEGORIES}
    metrics = [report["audits"][m]["displayValue"].replace("\xa0", " ") for m in METRICS]
    failing = [k for k, a in report["audits"].items()
               if a.get("scoreDisplayMode") in SCORED and a.get("score") is not None
               and a["score"] < 0.9 and k not in METRICS]
    return scores, metrics, failing


def broken_links():
    run = subprocess.run(["npx", "--yes", LINKINATOR, BASE + "/", "--recurse", "--retry",
                          "--skip", "linkedin.com", "--format", "json"],
                         capture_output=True, text=True)
    links = json.loads(run.stdout)["links"]
    return len(links), [f"{l['status']} {l['url']} <- {l.get('parent', '')}"
                        for l in links if l["state"] == "BROKEN"]


over, failing_audits = [], collections.Counter()
print(f"{'page':10} {'mode':7} perf a11y  bp  seo  LCP      CLS    TBT")
with tempfile.TemporaryDirectory() as tmp:
    for name, path in PAGES:
        for preset in ("mobile", "desktop"):
            scores, metrics, failing = lighthouse(BASE + path, preset, os.path.join(tmp, "r.json"))
            print(f"{name:10} {preset:7} " + " ".join(f"{scores[c]:>4}" for c in CATEGORIES)
                  + "  " + " ".join(f"{m:8}" for m in metrics))
            failing_audits.update(failing)
            for c, floor in BUDGET.items():
                if scores[c] < floor and not (c == "seo" and name in NOINDEX):
                    over.append(f"{name} {preset}: {c} {scores[c]} < {floor}")

checked, broken = broken_links()
print(f"\nlinks: {checked} checked, {len(broken)} broken")
for b in broken:
    print("  " + b)
print("\naudits below 0.9 (runs):")
for audit, n in failing_audits.most_common():
    print(f"  {n:>2}  {audit}")

if over or broken:
    print(f"\n❌ {len(over)} score(s) under budget, {len(broken)} broken link(s)")
    for o in over:
        print("  " + o)
    sys.exit(1)
print("\n✅ every page within budget, no broken links")
