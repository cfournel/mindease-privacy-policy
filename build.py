#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator for onirahypno.com.

    python3 build.py

Writes the whole site (home + theme pages per language, privacy policy,
sitemap, robots.txt, 404, llms.txt, WebMCP tools) into the repo root from the copy in `content.py`.
Generated files are committed — GitHub Pages serves them as-is, there is no
build step on the Pages side.

Everything cross-cutting that SEO depends on — canonical URLs, reciprocal
hreflang alternates, breadcrumbs, JSON-LD — is derived here rather than typed
per page, so adding a language or a theme cannot silently produce a half-linked
page. Rerun after any edit to `content.py`; `git status` shows what changed.
"""

import datetime
import html
import json
import os
import re
import shutil
import subprocess

from content import SITE, THEMES, GUIDES, LANGS

ROOT = os.path.dirname(os.path.abspath(__file__))
ORIGIN = SITE["origin"]

# The Onira mark: a sun over calm waves. Kept in step with the launcher glyph in
# app/src/main/res/drawable/ic_launcher_foreground.xml (same geometry, scaled from
# that file's 108 viewport to 24) — if one changes, change both.
# The Onira mark: a sun over calm waves. Kept in step with the launcher glyph in
# app/src/main/res/drawable/ic_launcher_foreground.xml (same geometry, scaled from
# that file's 108 viewport to 24) — if one changes, change both.
MARK_SHAPES = ('<circle cx="12" cy="9.8" r="2.7" fill="none"/>'
               '<path d="M4.4 14.7C6.7 12.9 8.4 16.4 10.7 14.7C12.9 12.9 14.7 16.4 16.9 14.7'
               'C17.8 14 18.7 14.2 19.6 14.7" fill="none"/>'
               '<path d="M4.4 16.9C6.7 15.1 8.4 18.7 10.7 16.9C12.9 15.1 14.7 18.7 16.9 16.9'
               'C17.8 16.2 18.7 16.4 19.6 16.9" fill="none" opacity=".7"/>')

MARK = ('<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="1.4" stroke-linecap="round" aria-hidden="true">' + MARK_SHAPES +
        '</svg>')

# Same shapes on the app's sage background, for the browser tab. The PNG and .ico
# fallbacks beside it are downscaled from the Play Store icon, so tab, home screen
# and store listing all show one glyph.
FAVICON_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">'
               '<rect width="24" height="24" rx="5" fill="#5E7F6A"/>'
               '<g stroke="#fff" stroke-width="1.4" stroke-linecap="round">'
               + MARK_SHAPES + '</g></svg>')


# ------------------------------------------------------------------ paths ----

def home_url(lang):
    return "/" if not lang["base"] else "/%s/" % lang["base"]


def theme_url(lang, key):
    prefix = "/%s" % lang["base"] if lang["base"] else ""
    return "%s/%s/%s/" % (prefix, lang["theme_dir"], lang["themes"][key]["slug"])


def guide_url(lang, key):
    prefix = "/%s" % lang["base"] if lang["base"] else ""
    return "%s/%s/%s/" % (prefix, lang["guide_dir"], lang["guides"][key]["slug"])


def privacy_url(lang):
    # One policy document, in English, shared by every language.
    return "/privacy/"


def out_path(url):
    """`/fr/hypnose/sommeil/` -> `<repo>/fr/hypnose/sommeil/index.html`"""
    rel = url.strip("/")
    return os.path.join(ROOT, rel, "index.html") if rel else os.path.join(ROOT, "index.html")


def esc(s):
    return html.escape(s, quote=False)


# --------------------------------------------------------------- template ----

def head(lang, title, desc, url, alternates, jsonld):
    """alternates: [(hreflang, path)], first entry also used for x-default."""
    links = "".join(
        '\n<link rel="alternate" hreflang="%s" href="%s%s">' % (code, ORIGIN, path)
        for code, path in alternates
    )
    links += '\n<link rel="alternate" hreflang="x-default" href="%s%s">' % (ORIGIN, alternates[0][1])
    blocks = "".join(
        '\n<script type="application/ld+json">%s</script>' % json.dumps(b, ensure_ascii=False)
        for b in jsonld
    )
    if SITE.get("search_console"):
        blocks = ('\n<meta name="google-site-verification" content="%s">'
                  % esc(SITE["search_console"])) + blocks
    return """<!doctype html>
<html lang="%(code)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(origin)s%(url)s">%(links)s
<meta property="og:type" content="website">
<meta property="og:site_name" content="Onira">
<meta property="og:locale" content="%(code)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(origin)s%(url)s">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#5E7F6A">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/site.css">
<script src="/assets/webmcp.js" defer></script>%(blocks)s
</head>
<body>
""" % {
        "code": lang["code"], "title": esc(title), "desc": esc(desc),
        "origin": ORIGIN, "url": url, "links": links, "blocks": blocks,
    }


def header(lang, alternates, title):
    """The wordmark spells out the page's own <title>, not just "Onira"."""
    langs = "".join(
        '<a href="%s" hreflang="%s" %s>%s</a>' % (
            path, code,
            'aria-current="true"' if code == lang["code"] else "",
            next(l["label"] for l in LANGS if l["code"] == code),
        )
        for code, path in alternates
    )
    # A text button, not the Play badge: Google's badge guidelines forbid resizing
    # or redrawing the artwork, and the real badge already sits in the page body
    # (see cta()). This one only has to be reachable without scrolling.
    return """<header class="site-head"><div class="wrap">
  <a class="mark" href="%s">%s<span>%s</span></a>
  <div class="head-end">
    <nav class="langs" aria-label="%s">%s</nav>
    <a class="get" href="%s" rel="noopener">%s</a>
  </div>
</div></header>
<main class="wrap">
""" % (
        home_url(lang), MARK, esc(title), esc(lang["ui"]["langs_label"]), langs,
        SITE["play"], esc(lang["ui"]["head_cta"]),
    )


def badges():
    """Reciprocal directory badges, in every footer.

    Every <img> carries its displayed width/height and loads lazily, for the
    same reason the screenshots do: the footer must not reflow as they arrive,
    and none of them may become the LCP element.
    """
    if not SITE.get("badges"):
        return ""
    links = " ".join(
        '<a href="%s" target="_blank" rel="noopener noreferrer">'
        '<img src="%s" alt="%s" width="%d" height="%d" loading="lazy" '
        'decoding="async"></a>'
        % (esc(b["href"]), esc(b["src"]), esc(b["alt"]), b["width"], b["height"])
        for b in SITE["badges"])
    return '\n  <p class="badges">%s</p>' % links


def footer(lang):
    ui = lang["ui"]
    items = "".join("<li>%s</li>" % i for i in [
        '<a href="%s">%s</a>' % (home_url(lang), esc(ui["home_crumb"])),
        '<a href="%s">%s</a>' % (privacy_url(lang), esc(ui["foot_privacy"])),
        '<a href="%s" rel="noopener">%s</a>' % (SITE["play"], esc(ui["foot_play"])),
    ])
    return """</main>
<footer class="site-foot"><div class="wrap">
  <ul>%s</ul>
  <p>%s</p>%s
</div></footer>
</body>
</html>
""" % (items, esc(lang["ui"]["foot_tag"]), badges())


def cta(lang):
    """Official Google Play badge, localised, served from assets/badges/.

    Google's badge guidelines require the artwork unmodified, so it is an <img>
    rather than a redrawn button: no recolouring for dark mode, no cropping, and
    the width/height attributes match the file's own aspect ratio.
    """
    ui = lang["ui"]
    return ('<p><a class="cta" href="%s" rel="noopener">'
            '<img src="/assets/badges/%s.png" width="216" height="84" '
            'alt="%s" loading="lazy" decoding="async"></a></p>\n'
            '<p class="muted">%s</p>\n'
            % (SITE["play"], lang["code"], esc(ui["badge_alt"]), esc(ui["cta_note"])))


def how_it_works(lang):
    ui = lang["ui"]
    steps = "".join("<li>%s</li>" % esc(s) for s in ui["how_steps"])
    return "<h2>%s</h2>\n<ol class=\"steps\">%s</ol>\n" % (esc(ui["how_title"]), steps)


def privacy_and_safety(lang):
    """The privacy card gets its own full-width figure rather than a slot in the
    gallery grid: it is a text poster, and its headline is unreadable at thumbnail
    size. It is also the one capture that exists per language."""
    ui = lang["ui"]
    _, alt, caption = next(i for i in ui["screens"] if i[0] == "privacy")
    figure = ('<figure class="shot-wide">'
              '<img src="/assets/screens/privacy-%s.webp" width="540" height="1200" '
              'loading="lazy" decoding="async" alt="%s">'
              '<figcaption>%s</figcaption></figure>\n'
              % (lang["code"], esc(alt), esc(caption)))
    return ("<h2>%s</h2>\n<p>%s</p>\n%s<p><a href=\"%s\">%s</a></p>\n"
            "<h2>%s</h2>\n<div class=\"callout\"><p>%s</p></div>\n" % (
                esc(ui["privacy_title"]), esc(ui["privacy_body"]), figure,
                privacy_url(lang), esc(ui["privacy_link"]),
                esc(ui["safety_title"]), esc(ui["safety_body"])))


def screens(lang, only=None):
    """Phone captures. The app's UI is only captured in French so far, so those
    files are shared across languages; the privacy card, which is generated, has a
    file per language. Alt text and captions are localised either way.

    Every image is lazy-loaded and carries its intrinsic width/height, which is
    what keeps CLS at 0 and the images out of the LCP measurement.
    """
    items = [i for i in lang["ui"]["screens"]
             if i[0] != "privacy" and (only is None or i[0] in only)]
    figures = []
    for key, alt, caption in items:
        name = "privacy-%s" % lang["code"] if key == "privacy" else key
        figures.append(
            '<li><figure>'
            '<img src="/assets/screens/%s.webp" width="540" height="1200" '
            'loading="lazy" decoding="async" alt="%s">'
            '<figcaption>%s</figcaption></figure></li>'
            % (name, esc(alt), esc(caption)))
    return '<ul class="shots">%s</ul>\n' % "".join(figures)


def theme_cards(lang, exclude=None):
    lis = []
    for key in themes_for(lang):
        if key == exclude:
            continue
        t = lang["themes"][key]
        lis.append('<li><a href="%s"><strong>%s</strong><span>%s</span></a></li>'
                   % (theme_url(lang, key), esc(t["nav"]), esc(t["card"])))
    return '<ul class="cards">%s</ul>\n' % "".join(lis)


def guide_cards(lang, exclude=None):
    lis = []
    for key in guides_for(lang):
        if key == exclude:
            continue
        g = lang["guides"][key]
        lis.append('<li><a href="%s"><strong>%s</strong><span>%s</span></a></li>'
                   % (guide_url(lang, key), esc(g["nav"]), esc(g["card"])))
    return '<ul class="cards">%s</ul>\n' % "".join(lis)


# ----------------------------------------------------------------- dates ----
#
# Every URL used to carry SITE["updated"] as its <lastmod>, which meant a
# freshly published page announced itself to Google as unchanged since whenever
# that constant was last touched -- the opposite of the signal a new page needs,
# and the reason resubmitting the sitemap by hand never helped.
#
# The date is now per page and derived from git: if what we just generated
# differs from the committed copy, the page changed today; otherwise it keeps
# the date of the last commit that touched it. Pages that did not change keep
# their old date, so "everything changed" is never claimed.
#
# The dateModified inside a guide's JSON-LD is part of the page, so it is
# rendered as LASTMOD_TOKEN and both sides are normalised before comparison --
# otherwise the page would differ from itself on every build.

LASTMOD_TOKEN = "@@LASTMOD@@"
LASTMOD = {}
_TODAY = datetime.date.today().isoformat()
_DATEMOD_RE = re.compile(r'("dateModified":\s*")[^"]*(")')


def _git(*args):
    """Run git in the repo, or return None outside one / on any failure."""
    try:
        out = subprocess.run(("git",) + args, cwd=ROOT, stdout=subprocess.PIPE,
                             stderr=subprocess.DEVNULL, check=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    return out.stdout.decode("utf-8", "replace")


def _normalise(markup):
    return _DATEMOD_RE.sub(r"\1" + LASTMOD_TOKEN + r"\2", markup)


def in_git_repo():
    """Cached: is this checkout a git repo at all?"""
    if not hasattr(in_git_repo, "_answer"):
        in_git_repo._answer = _git("rev-parse", "--git-dir") is not None
    return in_git_repo._answer


def page_lastmod(relpath, markup):
    """The date this page last actually changed, as an ISO string.

    Outside a git checkout there is nothing to compare against, so the old
    frozen constant is all we have. Inside one, a page missing from HEAD is a
    page being published right now -- which must read as today, not as the
    constant, since that is the whole case this exists for.
    """
    if not in_git_repo():
        return SITE["updated"]
    committed = _git("show", "HEAD:" + relpath)
    if committed is None:
        return _TODAY                   # not in HEAD yet: brand new page
    if _normalise(committed) != _normalise(markup):
        return _TODAY                   # content changed in this build
    logged = _git("log", "-1", "--format=%cs", "--", relpath)
    return (logged or "").strip() or _TODAY


def write(url, markup):
    path = out_path(url)
    relpath = os.path.relpath(path, ROOT)
    stamp = page_lastmod(relpath, markup)
    LASTMOD[url] = stamp
    markup = markup.replace(LASTMOD_TOKEN, stamp)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(markup)
    return path


# ------------------------------------------------------------------ pages ----

def themes_for(lang):
    """Theme keys published in this language, in the global THEMES order.

    A theme need not exist in every language: search demand differs by market
    (quitting an ex is a large Spanish intent and a marginal English one), and
    a page is only worth having where people look for it.
    """
    return [key for key in THEMES if key in lang["themes"]]


def guides_for(lang):
    """Guide keys published in this language, in the global GUIDES order."""
    return [key for key in GUIDES if key in lang["guides"]]


def langs_with(key):
    """Languages that publish a given theme."""
    return [l for l in LANGS if key in l["themes"]]


def langs_with_guide(key):
    """Languages that publish a given guide."""
    return [l for l in LANGS if key in l["guides"]]


def alternates_home():
    return [(l["code"], home_url(l)) for l in LANGS]


def alternates_theme(key):
    """hreflang set of a theme — only the languages that actually publish it.

    Pointing an alternate at a page that does not exist is worse than having no
    alternate at all, so a theme published in two languages carries two.
    """
    return [(l["code"], theme_url(l, key)) for l in langs_with(key)]


def alternates_guide(key):
    """hreflang set of a guide — same rule as a theme: only where it is published."""
    return [(l["code"], guide_url(l, key)) for l in langs_with_guide(key)]


def nav_langs(key=None, guide=None):
    """Language switcher targets — always every language.

    Distinct from the hreflang set: a reader on an English-only theme page must
    still be able to reach the French site, so a language that lacks the theme
    (or the guide) falls back to its home page.
    """
    out = []
    for l in LANGS:
        if key and key in l["themes"]:
            out.append((l["code"], theme_url(l, key)))
        elif guide and guide in l["guides"]:
            out.append((l["code"], guide_url(l, guide)))
        else:
            out.append((l["code"], home_url(l)))
    return out


def build_home(lang):
    h = lang["home"]
    url = home_url(lang)
    alts = alternates_home()
    app_ld = {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": "Onira",
        "operatingSystem": "Android",
        "applicationCategory": "HealthApplication",
        "description": h["desc"],
        "url": ORIGIN + url,
        "inLanguage": lang["code"],
        "installUrl": SITE["play"],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
    }
    site_ld = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Onira",
        "url": ORIGIN + "/",
        "inLanguage": [l["code"] for l in LANGS],
    }
    body = ["<h1>%s</h1>\n" % esc(h["h1"]), '<p class="lede">%s</p>\n' % esc(h["lede"])]
    body.append(cta(lang))
    body += ["<p>%s</p>\n" % esc(p) for p in h["intro"]]
    body.append(how_it_works(lang))
    body.append("<h2>%s</h2>\n" % esc(lang["ui"]["screens_title"]))
    body.append(screens(lang))
    body.append("<h2>%s</h2>\n" % esc(h["themes_title"]))
    body.append(theme_cards(lang))
    body.append("<h2>%s</h2>\n" % esc(lang["ui"]["guides_title"]))
    body.append(guide_cards(lang))
    body.append(privacy_and_safety(lang))
    markup = (head(lang, h["title"], h["desc"], url, alts, [site_ld, app_ld])
              + header(lang, alts, h["title"]) + "".join(body) + footer(lang))
    return write(url, markup)


def build_theme(lang, key):
    t = lang["themes"][key]
    ui = lang["ui"]
    url = theme_url(lang, key)
    alts = alternates_theme(key)

    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "inLanguage": lang["code"],
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in t["faq"]
        ],
    }
    crumbs_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": ui["home_crumb"],
             "item": ORIGIN + home_url(lang)},
            {"@type": "ListItem", "position": 2, "name": t["nav"],
             "item": ORIGIN + url},
        ],
    }

    body = ['<p class="crumbs"><a href="%s">%s</a> &rsaquo; %s</p>\n'
            % (home_url(lang), esc(ui["home_crumb"]), esc(t["nav"]))]
    body.append("<h1>%s</h1>\n" % esc(t["h1"]))
    body.append('<p class="lede">%s</p>\n' % esc(t["lede"]))
    body.append("<h2>%s</h2>\n" % esc(t["why_title"]))
    body += ["<p>%s</p>\n" % esc(p) for p in t["why"]]
    body.append("<h2>%s</h2>\n<ul>%s</ul>\n" % (
        esc(ui["works_title"]), "".join("<li>%s</li>" % esc(w) for w in t["works_on"])))
    body.append(how_it_works(lang))
    body.append("<h2>%s</h2>\n<p>%s</p>\n" % (esc(ui["expect_title"]), esc(t["expect"])))
    body.append(screens(lang, only={"session"}))
    body.append(cta(lang))
    body.append('<h2>%s</h2>\n<div class="faq">%s</div>\n' % (
        esc(ui["faq_title"]),
        "".join("<h3>%s</h3><p>%s</p>" % (esc(q), esc(a)) for q, a in t["faq"])))
    body.append(privacy_and_safety(lang))
    body.append("<h2>%s</h2>\n%s" % (esc(ui["related_title"]), theme_cards(lang, exclude=key)))
    body.append("<h2>%s</h2>\n%s" % (esc(ui["guides_title"]), guide_cards(lang)))

    markup = (head(lang, t["title"], t["desc"], url, alts, [crumbs_ld, faq_ld])
              + header(lang, nav_langs(key), t["title"]) + "".join(body) + footer(lang))
    return write(url, markup)


def build_guide(lang, key):
    """A question page: the direct answer first, then the reasoning, then the app.

    Ordering is the whole point of these pages. Someone arriving from a search
    has a question, not an intent to install; answering it in the first screen is
    what earns the rest of the page, and the CTA sits after the method rather
    than in front of it.
    """
    g = lang["guides"][key]
    ui = lang["ui"]
    url = guide_url(lang, key)
    alts = alternates_guide(key)

    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "inLanguage": lang["code"],
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in g["faq"]
        ],
    }
    crumbs_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": ui["home_crumb"],
             "item": ORIGIN + home_url(lang)},
            {"@type": "ListItem", "position": 2, "name": g["nav"],
             "item": ORIGIN + url},
        ],
    }
    # The lede answers the headline question in one paragraph, which is the shape
    # a featured snippet is picked from — hence Article rather than a bare page,
    # and hence the answer block sitting above every <h2>.
    article_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": g["h1"],
        "description": g["desc"],
        "inLanguage": lang["code"],
        "mainEntityOfPage": ORIGIN + url,
        "author": {"@type": "Organization", "name": "Onira", "url": ORIGIN + "/"},
        "publisher": {"@type": "Organization", "name": "Onira", "url": ORIGIN + "/"},
        "dateModified": LASTMOD_TOKEN,
    }

    body = ['<p class="crumbs"><a href="%s">%s</a> &rsaquo; %s</p>\n'
            % (home_url(lang), esc(ui["home_crumb"]), esc(g["nav"]))]
    body.append("<h1>%s</h1>\n" % esc(g["h1"]))
    body.append('<p class="lede">%s</p>\n' % esc(g["lede"]))
    body.append('<div class="callout"><p><strong>%s</strong> %s</p></div>\n'
                % (esc(ui["guide_answer_title"]), esc(g["answer"])))
    for title, paras, bullets in g["sections"]:
        body.append("<h2>%s</h2>\n" % esc(title))
        body += ["<p>%s</p>\n" % esc(t) for t in paras]
        if bullets:
            body.append("<ol class=\"steps\">%s</ol>\n"
                        % "".join("<li>%s</li>" % esc(b) for b in bullets))
    body.append("<h2>%s</h2>\n" % esc(ui["guide_cta_title"]))
    body.append(screens(lang, only={"session"}))
    body.append(cta(lang))
    body.append('<h2>%s</h2>\n<div class="faq">%s</div>\n' % (
        esc(ui["faq_title"]),
        "".join("<h3>%s</h3><p>%s</p>" % (esc(q), esc(a)) for q, a in g["faq"])))
    body.append(privacy_and_safety(lang))
    body.append("<h2>%s</h2>\n%s" % (esc(ui["works_title"]), theme_cards(lang)))
    related = guide_cards(lang, exclude=key)
    if "<li>" in related:
        body.append("<h2>%s</h2>\n%s" % (esc(ui["guides_title"]), related))

    markup = (head(lang, g["title"], g["desc"], url, alts, [crumbs_ld, article_ld, faq_ld])
              + header(lang, nav_langs(guide=key), g["title"]) + "".join(body) + footer(lang))
    return write(url, markup)


PRIVACY_BODY = """<h1>Privacy Policy</h1>
<p class="muted">Last updated: 29 August 2026</p>

<p class="lede">Onira is designed so that your personal reflections and generated
hypnosis sessions never leave your device.</p>

<h2>What stays on your device</h2>
<ul>
  <li>The problem category and any free-text details you enter to generate a session.</li>
  <li>The generated hypnosis script itself.</li>
  <li>Your language preference, narration speed, and whether you&rsquo;ve purchased &ldquo;Remove Ads&rdquo;.</li>
</ul>

<div class="callout">
  <p>All script generation runs <strong>entirely on-device</strong> using a
  locally-stored AI model. Your input and the generated script are never
  transmitted to Onira&rsquo;s developer or any third party.</p>
</div>

<h2>What does leave your device</h2>
<ul>
  <li><strong>Advertising</strong> &mdash; unless you&rsquo;ve purchased &ldquo;Remove Ads&rdquo;,
    the app shows ads via Google AdMob. AdMob may collect device identifiers and usage
    data per Google&rsquo;s own privacy policy to serve and measure ads. Onira does not
    send your session content, category selection, or free-text input to AdMob or any
    ad network.</li>
  <li><strong>Purchases</strong> &mdash; the &ldquo;Remove Ads&rdquo; purchase is processed by
    Google Play Billing; standard Google Play purchase data applies (see Google
    Play&rsquo;s privacy policy).</li>
  <li><strong>Session ratings</strong> &mdash; if you rate a finished session (1&ndash;5
    stars), the app sends that star count &mdash; together with the session category,
    your interface language and the app version &mdash; to Google Firebase, so the
    developer can see the average rating. Nothing identifies you, and no free-text you
    have typed is included. If you choose to write to support after a low rating, that
    message is composed in your own email app and sent by you; the app never sends it
    on its own.</li>
  <li><strong>Model download</strong> &mdash; on first use, the app downloads the AI model
    weights (~2.6&nbsp;GB) over the network. This is a one-way download of app
    functionality, not a data upload &mdash; no user data is sent as part of this
    download.</li>
</ul>

<h2>Data retention and deletion</h2>
<p>Since your inputs and generated scripts are stored only in the app&rsquo;s local
storage, uninstalling the app deletes all of it. There is no server-side account or
profile to delete because none exists.</p>

<h2>Children&rsquo;s privacy</h2>
<p>Onira is not directed at children and is not intended for users under 13 (or the
minimum age of digital consent in your jurisdiction).</p>

<h2>Contact</h2>
<p>Questions about this policy can be sent to
<a href="mailto:%(email)s">%(email)s</a>.</p>
""" % {"email": SITE["email"]}


def build_privacy():
    en = LANGS[0]
    url = "/privacy/"
    alts = [(en["code"], url)]
    title = "Privacy Policy — Onira"
    markup = (head(en, title,
                   "Onira generates hypnosis sessions entirely on your device. This policy "
                   "explains what stays on your phone and what does not.",
                   url, alts, [])
              + header(en, alternates_home(), title) + PRIVACY_BODY + footer(en))
    return write(url, markup)


def build_404():
    en = LANGS[0]
    body = ("<h1>Page not found</h1>\n"
            '<p class="lede">That page does not exist. Start from the home page, or pick a '
            "theme below.</p>\n" + theme_cards(en))
    title = "Page not found — Onira"
    markup = (head(en, title, "This page does not exist.",
                   "/404.html", [(en["code"], "/")], [])
              + header(en, alternates_home(), title) + body + footer(en))
    path = os.path.join(ROOT, "404.html")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(markup)
    return path


def build_sitemap():
    entries = []
    for lang in LANGS:
        entries.append((home_url(lang), alternates_home(), "1.0"))
    for key in THEMES:
        for lang in langs_with(key):
            entries.append((theme_url(lang, key), alternates_theme(key), "0.8"))
    for key in GUIDES:
        for lang in langs_with_guide(key):
            entries.append((guide_url(lang, key), alternates_guide(key), "0.7"))
    entries.append(("/privacy/", [("en", "/privacy/")], "0.3"))

    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for url, alts, priority in entries:
        out.append("  <url>")
        out.append("    <loc>%s%s</loc>" % (ORIGIN, url))
        for code, path in alts:
            out.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>'
                       % (code, ORIGIN, path))
        out.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/>'
                   % (ORIGIN, alts[0][1]))
        out.append("    <lastmod>%s</lastmod>"
                   % LASTMOD.get(url, SITE["updated"]))
        out.append("    <priority>%s</priority>" % priority)
        out.append("  </url>")
    out.append("</urlset>")
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    return path


def build_robots():
    path = os.path.join(ROOT, "robots.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % ORIGIN)
    return path


APP_SUMMARY = ("Onira is a free Android app that writes a personal self-hypnosis session "
               "with an AI model running entirely on the phone, then narrates it aloud. "
               "Nothing the user types or receives leaves the device.")

APP_NOTES = [
    "Onira is a relaxation and self-hypnosis tool, not therapy, medical or psychiatric "
    "advice, and not a substitute for professional care or emergency services.",
    "Free, no account, no subscription; a one-time purchase removes ads. Sessions "
    "are available in English, French and Spanish. Not every theme or guide is "
    "published in every language: each page exists where people search for it.",
]

PRIVACY_SUMMARY = ("Session generation runs on-device; inputs and scripts are never "
                   "uploaded. Ads (Google AdMob, unless removed), Play Billing purchases "
                   "and anonymous 1-5 star session ratings (Firebase) are the only data "
                   "that leaves the phone. No account exists, so uninstalling deletes "
                   "everything.")


def site_index():
    """Every page an agent may be pointed at, per language, from content.py."""
    out = {}
    for lang in LANGS:
        out[lang["code"]] = {
            "language": lang["name"],
            "home": home_url(lang),
            "themes": [{"name": lang["themes"][k]["nav"], "summary": lang["themes"][k]["card"],
                        "description": lang["themes"][k]["desc"], "url": theme_url(lang, k)}
                       for k in themes_for(lang)],
            "guides": [{"name": lang["guides"][k]["nav"], "summary": lang["guides"][k]["card"],
                        "description": lang["guides"][k]["desc"], "url": guide_url(lang, k)}
                       for k in guides_for(lang)],
        }
    return out


def build_llms_txt():
    """/llms.txt, in the llmstxt.org shape: H1, blockquote summary, free notes,
    then H2 sections of `- [name](url): notes` links, with `Optional` last."""
    index = site_index()
    out = ["# Onira", "", "> " + APP_SUMMARY, ""]
    out += [n + "\n" for n in APP_NOTES]
    out += ["## App", "",
            "- [Onira on Google Play](%s): install page; Android, free with ads" % SITE["play"],
            "- [Privacy policy](%s/privacy/): %s" % (ORIGIN, PRIVACY_SUMMARY),
            "- [Home page](%s/): what the app does and how a session is built" % ORIGIN,
            ""]
    for code, entry in index.items():
        out += ["## Session themes (%s)" % entry["language"], ""]
        out += ["- [%s](%s%s): %s" % (t["name"], ORIGIN, t["url"], t["description"])
                for t in entry["themes"]]
        out.append("")
        if entry["guides"]:
            out += ["## Guides (%s)" % entry["language"], ""]
            out += ["- [%s](%s%s): %s" % (g["name"], ORIGIN, g["url"], g["description"])
                    for g in entry["guides"]]
            out.append("")
    out += ["## Optional", ""]
    out += ["- [Home page (%s)](%s%s)" % (e["language"], ORIGIN, e["home"])
            for c, e in index.items() if e["home"] != "/"]
    out += ["- [Sitemap](%s/sitemap.xml): every page with its hreflang alternates" % ORIGIN,
            "- [Support](mailto:%s): contact address" % SITE["email"]]
    path = os.path.join(ROOT, "llms.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    return path


def webmcp_tools(codes):
    """WebMCP tool declarations. Schemas live here as data so they are static JSON
    Schema; the script only attaches an `execute` per name."""
    language = {"type": "string", "enum": codes,
                "description": "Language code; defaults to the current page's language."}
    return [
        {"name": "get_app_info",
         "description": "What Onira is, its price, platform, install link, privacy "
                        "summary and support contact.",
         "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
         "annotations": {"readOnlyHint": True}},
        {"name": "list_session_themes",
         "description": "List the hypnosis session themes (sleep, anxiety, stress, ...) "
                        "published in a language, with a summary and page URL for each.",
         "inputSchema": {"type": "object", "properties": {"language": language},
                         "additionalProperties": False},
         "annotations": {"readOnlyHint": True}},
        {"name": "list_guides",
         "description": "List the guide pages that answer common questions about "
                        "self-hypnosis in a language, with a summary and page URL for each.",
         "inputSchema": {"type": "object", "properties": {"language": language},
                         "additionalProperties": False},
         "annotations": {"readOnlyHint": True}},
        {"name": "open_page",
         "description": "Navigate this tab to a page of onirahypno.com. Only paths "
                        "returned by list_session_themes, list_guides or get_app_info "
                        "are accepted.",
         "inputSchema": {"type": "object",
                         "properties": {"path": {"type": "string",
                                                 "description": "Site path, e.g. /hypnosis/sleep/"}},
                         "required": ["path"], "additionalProperties": False}},
    ]


WEBMCP_JS = """// Generated by build.py from content.py; do not edit.
// WebMCP tools so in-browser AI agents can read the site without scraping it.
(function () {
  var mc = navigator.modelContext;
  if (!mc) return;
  var DATA = __DATA__;

  function reply(value) {
    return {content: [{type: "text", text: JSON.stringify(value)}]};
  }
  function lang(input) {
    var code = (input && input.language) || document.documentElement.lang;
    return DATA.index[code] ? code : "en";
  }
  var handlers = {
    get_app_info: function () { return reply(DATA.app); },
    list_session_themes: function (input) {
      var l = lang(input);
      return reply({language: l, home: DATA.index[l].home, themes: DATA.index[l].themes});
    },
    list_guides: function (input) {
      var l = lang(input);
      return reply({language: l, guides: DATA.index[l].guides});
    },
    open_page: function (input) {
      var path = input && input.path;
      if (DATA.pages.indexOf(path) === -1) {
        return reply({error: "Unknown path", path: path});
      }
      setTimeout(function () { location.assign(path); }, 0);
      return reply({navigating_to: DATA.origin + path});
    }
  };
  var tools = DATA.tools.map(function (t) {
    return Object.assign({}, t, {execute: handlers[t.name]});
  });
  if (typeof mc.registerTool === "function") {
    tools.forEach(function (t) { try { mc.registerTool(t); } catch (e) {} });
  } else if (typeof mc.provideContext === "function") {
    mc.provideContext({tools: tools});
  }
})();
"""


def build_webmcp():
    index = site_index()
    pages = ["/privacy/"]
    for entry in index.values():
        pages += [entry["home"]] + [p["url"] for p in entry["themes"] + entry["guides"]]
    data = {
        "origin": ORIGIN,
        "app": {"name": "Onira", "summary": APP_SUMMARY, "notes": APP_NOTES,
                "platform": "Android", "price": "Free; one-time purchase removes ads",
                "install_url": SITE["play"], "privacy": PRIVACY_SUMMARY,
                "privacy_url": "/privacy/", "support_email": SITE["email"],
                "languages": {c: e["language"] for c, e in index.items()},
                "homes": {c: e["home"] for c, e in index.items()}},
        "index": index,
        "pages": pages,
        "tools": webmcp_tools(list(index)),
    }
    path = os.path.join(ROOT, "assets", "webmcp.js")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(WEBMCP_JS.replace("__DATA__", json.dumps(data, ensure_ascii=False)))
    return path


def clean():
    """Drop generated language/theme trees so renamed slugs don't leave orphans."""
    for lang in LANGS:
        subdirs = [lang["theme_dir"], lang["guide_dir"]]
        for d in filter(None, [lang["base"]] + [
                os.path.join(lang["base"], sub) if lang["base"] else sub
                for sub in subdirs]):
            target = os.path.join(ROOT, d)
            if os.path.isdir(target):
                shutil.rmtree(target)
    for d in ("privacy",):
        target = os.path.join(ROOT, d)
        if os.path.isdir(target):
            shutil.rmtree(target)


def build_favicon_svg():
    path = os.path.join(ROOT, "assets", "favicon.svg")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(FAVICON_SVG + "\n")
    return path


# ------------------------------------------------------------ validation ----
#
# content.py is hand-written nested data, and the shapes that go wrong are
# always the same: a guide section written as [heading, paragraphs] with the
# bullet list left off, or an FAQ pair that grew a third element. Unchecked,
# that surfaces as "ValueError: not enough values to unpack" from deep inside a
# template, naming nothing -- and because it fires mid-run, it leaves the tree
# half regenerated, which then makes audit.py report hundreds of failures that
# are all downstream of the one real problem.
#
# So: check every shape first, name the exact entry, and write nothing until it
# all passes.

THEME_KEYS = ("slug", "nav", "card", "title", "desc", "h1", "lede",
              "why_title", "why", "works_on", "expect", "faq")
GUIDE_KEYS = ("slug", "nav", "card", "title", "desc", "h1", "lede", "answer",
              "sections", "faq")


def _strings(value, where, problems):
    if not isinstance(value, (list, tuple)):
        problems.append("%s: expected a list, got %s" % (where, type(value).__name__))
        return
    for i, item in enumerate(value):
        if not isinstance(item, str):
            problems.append("%s[%d]: expected a string, got %s"
                            % (where, i, type(item).__name__))


def _faq(entries, where, problems):
    if not isinstance(entries, (list, tuple)):
        problems.append("%s: expected a list of (question, answer) pairs" % where)
        return
    for i, pair in enumerate(entries):
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            problems.append("%s[%d]: expected (question, answer), got %d element(s)"
                            % (where, i, len(pair) if hasattr(pair, "__len__") else 1))


def validate_content():
    """Fail loudly, and by name, before a single file is written."""
    problems = []

    for lang in LANGS:
        code = lang["code"]

        for key, theme in lang.get("themes", {}).items():
            where = "%s theme %r" % (code, key)
            if key not in THEMES:
                problems.append("%s: not listed in THEMES" % where)
            for field in THEME_KEYS:
                if field not in theme:
                    problems.append("%s: missing %r" % (where, field))
            _strings(theme.get("why", []), where + " why", problems)
            _strings(theme.get("works_on", []), where + " works_on", problems)
            _faq(theme.get("faq", []), where + " faq", problems)

        for key, guide in lang.get("guides", {}).items():
            where = "%s guide %r" % (code, key)
            if key not in GUIDES:
                problems.append("%s: not listed in GUIDES" % where)
            for field in GUIDE_KEYS:
                if field not in guide:
                    problems.append("%s: missing %r" % (where, field))
            sections = guide.get("sections", [])
            if not isinstance(sections, (list, tuple)):
                problems.append("%s sections: expected a list" % where)
                continue
            for i, section in enumerate(sections):
                label = "%s section %d" % (where, i)
                if not isinstance(section, (list, tuple)) or len(section) != 3:
                    got = len(section) if hasattr(section, "__len__") else 1
                    heading = section[0] if got else "?"
                    problems.append(
                        "%s (%r): expected [heading, paragraphs, bullets] -- got %d "
                        "element(s). An empty bullet list is written []." 
                        % (label, heading, got))
                    continue
                if not isinstance(section[0], str):
                    problems.append("%s: heading must be a string" % label)
                _strings(section[1], label + " paragraphs", problems)
                _strings(section[2], label + " bullets", problems)
            _faq(guide.get("faq", []), where + " faq", problems)

    if problems:
        print("content.py is malformed -- nothing was written:\n")
        for problem in problems:
            print("  " + problem)
        raise SystemExit(1)


def main():
    validate_content()
    clean()
    written = [build_favicon_svg()]
    for lang in LANGS:
        written.append(build_home(lang))
        for key in themes_for(lang):
            written.append(build_theme(lang, key))
        for key in guides_for(lang):
            written.append(build_guide(lang, key))
    written.append(build_privacy())
    written.append(build_404())
    written.append(build_sitemap())
    written.append(build_robots())
    written.append(build_llms_txt())
    written.append(build_webmcp())
    for path in written:
        print(os.path.relpath(path, ROOT))
    print("\n%d files written" % len(written))


if __name__ == "__main__":
    main()
