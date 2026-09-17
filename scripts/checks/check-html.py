#!/usr/bin/env python3
import base64, glob, hashlib, io, json, os, subprocess, sys, tarfile, urllib.request
from gate import PUB, finish
VERSION = "26.9.7"
INTEGRITY = "sha512-ZwoNfGQQBWCAEFMtz1fokv4PBC+WhF13QQA+Q/AFNyqnb57aAApnsyquMT+9dK8H96jzuGz9eydYMeaSisyYow=="
JAR = os.path.join(os.path.expanduser("~"), ".cache", "ibraverse", f"vnu-{VERSION}.jar")

if not os.path.exists(JAR):
    tgz = urllib.request.urlopen(f"https://registry.npmjs.org/vnu-jar/-/vnu-jar-{VERSION}.tgz").read()
    digest = "sha512-" + base64.b64encode(hashlib.sha512(tgz).digest()).decode()
    if digest != INTEGRITY:
        sys.exit(f"❌ vnu-jar {VERSION} does not match its pinned integrity")
    os.makedirs(os.path.dirname(JAR), exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(tgz)) as t:
        open(JAR, "wb").write(t.extractfile("package/build/dist/vnu.jar").read())

pages = sorted(f for f in glob.glob(os.path.join(PUB, "**", "*.html"), recursive=True)
               if not os.path.relpath(f, PUB).startswith("reports" + os.sep))
run = subprocess.run(["java", "-jar", JAR, "--errors-only", "--format", "json", *pages],
                     capture_output=True, text=True)
errors = [m for m in json.loads(run.stderr)["messages"] if m.get("type") == "error"]

print(f"validated {len(pages)} pages with the Nu HTML Checker {VERSION}")
finish([f"{os.path.relpath(m['url'].removeprefix('file:'), PUB)}:{m.get('lastLine', '?')}: {m['message']}" for m in errors],
       "every page is valid HTML")
