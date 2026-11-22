#!/usr/bin/env python3
"""Weekly backlink watch for onirahypno.com (marketing/BACKLINKS.md in the app repo).

Three checks, one Markdown report:

1. Known links (backlinks.json): is the page still up, does it still link to the
   site or the Play listing, and is that link followed or nofollow?
2. Roundups: new "best hypnosis / sleep app" articles in EN/FR/ES that do not
   mention Onira yet: the outreach list (write to the author, by hand).
3. Unlinked mentions: pages that name Onira without a link: ask for one.

2 and 3 need a search API. They use the Brave Search API when BRAVE_API_KEY is set
(free tier, https://brave.com/search/api/); without it only check 1 runs. Pages
already seen are remembered in ~/gsc-reports/backlink_state.json, so a report only
lists what is new since the last run.

Nothing is sent to anyone: the script only reads public pages. Outreach stays manual.

Usage: python3 backlink_watch.py [--no-search]
Report: ~/gsc-reports/backlinks-YYYY-MM-DD.md (next to gsc_report.py's reports).
"""
import argparse
import datetime
import html.parser
import json
import os
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
OUT_DIR = pathlib.Path.home() / "gsc-reports"
STATE = OUT_DIR / "backlink_state.json"
UA = "Mozilla/5.0 (X11; Linux x86_64) backlink-watch/1.0"
TARGETS = ("onirahypno.com", "play.google.com/store/apps/details?id=com.oytaub.mindease",
           "huggingface.co/oytaub/hypnos-e2b-enfres")
BRAND = ("onira",)

# Queries a roundup author would rank for. Kept short: the free API tier is per month.
ROUNDUP_QUERIES = [
    ("en", "best self hypnosis app"),
    ("en", "best hypnosis apps for sleep"),
    ("en", "best hypnosis app android"),
    ("en", "offline AI meditation app android"),
    ("fr", "meilleure application hypnose"),
    ("fr", "application autohypnose sommeil"),
    ("es", "mejor app de hipnosis"),
    ("es", "app autohipnosis para dormir"),
]
MENTION_QUERIES = ['"Onira" hypnosis -site:onirahypno.com',
                   '"Onira" hypnose -site:onirahypno.com',
                   '"Onira" hipnosis -site:onirahypno.com']
# A roundup lists several apps: its title says so. Technique articles, product pages and
# APK mirrors also rank for these queries and are not outreach targets.
ROUNDUP_TITLE = re.compile(
    r"\b(best|top \d+|\d+ (best|top)|compared|comparison|vs|ranked|tested|meilleur(e)?s?|"
    r"comparatif|top|mejor(es)?|comparad[ao]s?|comparativa)\b.*\b(apps?|applications?|aplicaciones|appli)\b|"
    r"\b(apps?|applications?|aplicaciones)\b.*\b(compared|comparatif|comparad[ao]s?|valent le coup|valen la pena)\b",
    re.I)
SKIP_HOSTS = ("uptodown.com", "appbrain.com", "apkpure.com", "onirahypno.com", "play.google.com", "apps.apple.com", "youtube.com",
              "reddit.com", "facebook.com", "instagram.com", "tiktok.com", "x.com", "twitter.com")


class Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            a = dict(attrs)
            self.links.append((a.get("href") or "", (a.get("rel") or "").lower()))

    def handle_data(self, data):
        self.text.append(data)


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en,fr,es"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read(3_000_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return None, str(e)


def inspect(url):
    """(status, [(href, rel)] pointing at us, mentions brand in text)."""
    status, body = fetch(url)
    if not body or status != 200:
        return status, [], False
    p = Links()
    try:
        p.feed(body)
    except Exception:
        pass
    ours = [(h, r) for h, r in p.links if any(t in h for t in TARGETS)]
    text = " ".join(p.text).lower()
    return status, ours, any(b in text for b in BRAND)


def link_type(ours):
    if not ours:
        return "none"
    rels = {r for _, r in ours}
    if any(not any(k in r for k in ("nofollow", "ugc", "sponsored")) for r in rels):
        return "followed"
    return "nofollow"


def brave(query, lang):
    key = os.environ.get("BRAVE_API_KEY")
    url = "https://api.search.brave.com/res/v1/web/search?" + urllib.parse.urlencode(
        {"q": query, "count": 20, "search_lang": lang, "freshness": "py"})
    req = urllib.request.Request(url, headers={"Accept": "application/json",
                                               "X-Subscription-Token": key})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = json.load(r)
    time.sleep(1.1)  # free tier: 1 request per second
    return [(x["url"], x.get("title", "")) for x in data.get("web", {}).get("results", [])]


def host(url):
    return urllib.parse.urlparse(url).netloc.lower().removeprefix("www.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-search", action="store_true", help="only re-check the known links")
    args = ap.parse_args()

    OUT_DIR.mkdir(exist_ok=True)
    state = json.loads(STATE.read_text()) if STATE.exists() else {"seen": {}}
    known = json.loads((HERE / "backlinks.json").read_text())
    today = datetime.date.today().isoformat()
    out = ["# Backlinks, %s" % today, ""]

    out += ["## Known links", "", "| Source | HTTP | Link to us | Note |", "|---|---|---|---|"]
    lost = 0
    for k in known:
        status, ours, _ = inspect(k["url"])
        lt = link_type(ours)
        note = k.get("note", "")
        if status in (403, 429):
            lt, note = "?", "blocks scripts (bot protection), check by hand " + note
        elif status != 200:
            note = "**page unreachable** " + note
        elif lt == "none":
            note = "**link gone (or rendered by JavaScript)** " + note
            lost += 1
        elif k.get("expect") and lt != k["expect"]:
            note = "**was %s** %s" % (k["expect"], note)
        out.append("| [%s](%s) | %s | %s | %s |" % (k["name"], k["url"], status, lt, note.strip()))
    out.append("")

    if args.no_search or not os.environ.get("BRAVE_API_KEY"):
        out += ["_Search skipped (no BRAVE_API_KEY or --no-search): no roundups or mentions._", ""]
    else:
        known_hosts = {host(k["url"]) for k in known}
        roundups, mentions = [], []
        for lang, q in ROUNDUP_QUERIES:
            for url, title in brave(q, lang):
                h = host(url)
                if url in state["seen"] or any(s in h for s in SKIP_HOSTS) or h in known_hosts:
                    continue
                if not ROUNDUP_TITLE.search(title):
                    continue
                state["seen"][url] = today
                status, ours, named = inspect(url)
                if status == 200 and not ours:
                    roundups.append((lang, q, title, url, named))
        for q in MENTION_QUERIES:
            for url, title in brave(q, "en"):
                h = host(url)
                if url in state["seen"] or any(s in h for s in SKIP_HOSTS):
                    continue
                state["seen"][url] = today
                status, ours, named = inspect(url)
                if status == 200 and named and not ours:
                    mentions.append((title, url))
        out += ["## New roundups without Onira (outreach list)", ""]
        out += ["- [%s] [%s](%s), query \"%s\"%s" % (l, t or u, u, q, " (names Onira, no link)" if n else "")
                for l, q, t, u, n in roundups] or ["Nothing new."]
        out += ["", "## Unlinked mentions (ask for a link)", ""]
        out += ["- [%s](%s)" % (t or u, u) for t, u in mentions] or ["Nothing new."]
        out.append("")

    out += ["Check the trend in Search Console too (gsc_report.py): \"Detected, currently not "
            "indexed\" going down is the goal, not the link count."]
    report = OUT_DIR / ("backlinks-%s.md" % today)
    report.write_text("\n".join(out) + "\n")
    STATE.write_text(json.dumps(state, indent=1, sort_keys=True))
    print("\n".join(out))
    print("\nSaved to %s" % report)
    return 1 if lost else 0


if __name__ == "__main__":
    raise SystemExit(main())
