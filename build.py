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
import urllib.parse

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


# The CDN (Cloudflare) caches site.css for hours, so a new page could arrive with the
# old stylesheet: its URL carries a hash of its contents, which changes with every edit.
import hashlib
with open(os.path.join(ROOT, "assets", "site.css"), "rb") as _f:
    CSS_VERSION = hashlib.sha256(_f.read()).hexdigest()[:10]

# The site dresses for the moment of the day like the app does (#45 there):
# dawn before 11 h, a clear sky until 18 h, the night after that. The visitor's
# hour always decides, a dark system theme does not (a dark-mode visitor at 8 h
# saw the night and took it for a bug). Runs in <head>, before
# the first paint, so the page never flashes the wrong sky. Without JavaScript the
# CSS falls back to midday, or the night under prefers-color-scheme: dark.
MOMENT_JS = ("(function(){var h=new Date().getHours(),m=h>=5&&h<11?'morning':h>=11&&h<18?'midday':'evening';"
             "var q=/[?&]moment=(morning|midday|evening)/.exec(location.search);if(q)m=q[1];"
             "document.documentElement.dataset.moment=m;"
             "var c={morning:'#FFC9A8',midday:'#A9D9E3',evening:'#3C3A78'}[m];"
             "document.querySelector('meta[name=theme-color]').content=c})()")

# The home screen's landscape (app SkyScene.kt): a sky fading into the page, the
# sun (or the moon, with stars) and two hills, the near one the colour of the page.
# Every colour is a CSS variable of the current moment, so one markup serves all three.
SCENE = ('<div class="scene" aria-hidden="true">'
         '<svg class="stars" viewBox="0 0 400 160" preserveAspectRatio="none">'
         + "".join('<circle cx="%d" cy="%d" r="%.1f"/>' % c for c in (
             (180, 18, 1.2), (232, 52, 1.6), (268, 14, 1), (300, 96, 1.4), (338, 40, 1.8),
             (372, 118, 1.1), (390, 22, 1.3), (212, 120, 1), (24, 10, 1.2), (96, 26, 1),
             (252, 140, 1.2), (352, 74, 1)))
         + '</svg><span class="celestial"></span>'
         '<svg class="hills" viewBox="0 0 1440 140" preserveAspectRatio="none">'
         '<path class="far" d="M0 70C240 20 480 20 720 55S1200 110 1440 50V140H0Z"/>'
         '<path class="near" d="M0 110C300 70 560 80 820 100S1260 120 1440 90V140H0Z"/>'
         '</svg></div>')

# Theme tiles wear the app's category colours and motifs (CategoryArt.kt); themes
# the app has no category for borrow the nearest one.
MOTIFS = {
    "leaf": '<path d="M20 4C31 12 33 26 20 37C7 26 9 12 20 4Z"/><path d="M20 12V33" stroke="#fff" stroke-opacity=".55" stroke-width="2" stroke-linecap="round"/>',
    "moon": '<path d="M25 5a15 15 0 1 0 10 25A13 13 0 0 1 25 5Z"/>',
    "sun": '<circle cx="20" cy="20" r="7.5"/><g stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M20 3v5M20 32v5M3 20h5M32 20h5M8 8l3.5 3.5M28.5 28.5 32 32M8 32l3.5-3.5M28.5 11.5 32 8"/></g>',
    "waves": '<g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M3 13c5-5 9 5 14 0s9 5 14 0 6-2 6-2"/><path d="M3 21c5-5 9 5 14 0s9 5 14 0 6-2 6-2"/><path d="M3 29c5-5 9 5 14 0s9 5 14 0 6-2 6-2"/></g>',
    "wind": '<g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M4 12h26"/><path d="M4 20h32"/><path d="M4 28h20"/></g>',
    "target": '<g fill="none" stroke="currentColor" stroke-width="3"><circle cx="20" cy="20" r="15"/><circle cx="20" cy="20" r="8.5"/></g><circle cx="20" cy="20" r="3.5"/>',
    "stones": '<ellipse cx="20" cy="32" rx="12" ry="5"/><ellipse cx="20" cy="22" rx="9" ry="4.2"/><ellipse cx="20" cy="13" rx="6" ry="3.6"/>',
    "star": '<path d="M20 3C22 14 26 18 37 20 26 22 22 26 20 37 18 26 14 22 3 20 14 18 18 14 20 3Z"/>',
}
THEME_ART = {
    "anxiety": ("#86C49A", "leaf"), "sleep": ("#A897EA", "moon"),
    "confidence": ("#F1C75B", "sun"), "stress": ("#F2A07E", "waves"),
    "smoking": ("#8CC4E8", "wind"), "focus": ("#6CBDB5", "target"),
    "weight": ("#EE9DB4", "stones"), "fear": ("#D7B48A", "star"),
    "letting_go": ("#9DB4E8", "waves"), "motivation": ("#F2A07E", "sun"),
    "pain": ("#EE9DB4", "leaf"), "ibs": ("#86C49A", "waves"),
    "emotional_recovery": ("#A897EA", "star"), "anger": ("#F2A07E", "waves"),
    "burnout": ("#F1C75B", "leaf"), "night_waking": ("#8CC4E8", "moon"),
    "habits": ("#6CBDB5", "wind"), "learning": ("#9DB4E8", "target"),
}


def motif(key):
    color, name = THEME_ART.get(key, ("#D7B48A", "star"))
    return color, ('<svg class="motif" viewBox="0 0 40 40" fill="currentColor" aria-hidden="true">'
                   '%s</svg>' % MOTIFS[name])


# ------------------------------------------------------------------ paths ----

_PAGE = "site"


def play_url(slot):
    """Play listing link tagged for Play Console's acquisition report.

    Play reads utm_* only from the `referrer` parameter. The campaign names the
    page ("fr-home", "en-sleep", "guide-en-does-self-hypnosis-work"), the content
    names the slot on it (header, footer, cta), so the report says which page and
    which button an install came from. JSON-LD keeps the bare URL.
    """
    ref = urllib.parse.urlencode({
        "utm_source": "onirahypno.com", "utm_medium": "site",
        "utm_campaign": _PAGE, "utm_content": slot})
    return "%s&referrer=%s" % (SITE["play"], urllib.parse.quote(ref, safe=""))


def home_url(lang):
    return "/" if not lang["base"] else "/%s/" % lang["base"]


def theme_url(lang, key):
    prefix = "/%s" % lang["base"] if lang["base"] else ""
    return "%s/%s/%s/" % (prefix, lang["theme_dir"], lang["themes"][key]["slug"])


def guide_url(lang, key):
    prefix = "/%s" % lang["base"] if lang["base"] else ""
    return "%s/%s/%s/" % (prefix, lang["guide_dir"], lang["guides"][key]["slug"])


PRESS_URL = "/fr/presse/"


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
<meta property="og:image" content="%(origin)s/assets/og.png">
<meta property="og:image:width" content="1024">
<meta property="og:image:height" content="500">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="%(origin)s/assets/og.png">
<meta name="theme-color" content="#F1F6F2">
<script>%(moment)s</script>
<link rel="preload" href="/assets/fonts/nunito.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/young-serif.woff2" as="font" type="font/woff2" crossorigin>
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/site.css?v=%(css_v)s">
<script src="/assets/webmcp.js" defer></script>%(blocks)s
</head>
<body>
""" % {
        "code": lang["code"], "title": esc(title), "desc": esc(desc),
        "origin": ORIGIN, "url": url, "links": links, "blocks": blocks,
        "moment": MOMENT_JS,
        "css_v": CSS_VERSION,
    }


def header(lang, alternates, title, scene=True):
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
    return """%s<header class="site-head"><div class="wrap">
  <a class="mark" href="%s" aria-label="%s">%s<span>Onira</span></a>
  <div class="head-end">
    <nav class="langs" aria-label="%s">%s</nav>
    <a class="get" href="%s" rel="noopener">%s</a>
  </div>
</div></header>
<main class="wrap">
""" % (
        SCENE if scene else "", home_url(lang), esc(title), MARK, esc(lang["ui"]["langs_label"]), langs,
        esc(play_url("header")), esc(lang["ui"]["head_cta"]),
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
        '<a href="%s" rel="noopener">%s</a>' % (esc(play_url("footer")), esc(ui["foot_play"])),
    ] + (['<a href="%s">Presse</a>' % PRESS_URL] if lang["code"] == "fr" else []))
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
            % (esc(play_url("cta")), lang["code"], esc(ui["badge_alt"]), esc(ui["cta_note"])))


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


def news(lang):
    """What changed in the app lately: a short boxed list under the call to action of the
    home page. Kept to the latest release; older items go, they are in the store notes."""
    h = lang["home"]
    if not h.get("news"):
        return ""
    items = "".join("<li>%s</li>" % esc(i) for i in h["news"])
    return ('<section class="news"><h2>%s</h2><ul>%s</ul></section>\n'
            % (esc(h["news_title"]), items))


def screens(lang, only=None):
    """Phone captures, one file per language (`<key>-<code>.webp`, captured on a
    Pixel 7 for the 0.16 look; the app repo's marketing/assets/screens_raw).

    Every image is lazy-loaded and carries its intrinsic width/height, which is
    what keeps CLS at 0 and the images out of the LCP measurement.
    """
    items = [i for i in lang["ui"]["screens"]
             if i[0] != "privacy" and (only is None or i[0] in only)]
    figures = []
    for key, alt, caption in items:
        name = "%s-%s" % (key, lang["code"])
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
        color, art = motif(key)
        lis.append('<li><a href="%s" style="--c:%s"><strong>%s</strong><span>%s</span>%s</a></li>'
                   % (theme_url(lang, key), color, esc(t["nav"]), esc(t["card"]), art))
    return '<ul class="cards tiles">%s</ul>\n' % "".join(lis)


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
    global _PAGE
    _PAGE = "%s-home" % lang["code"]
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
        "screenshot": [ORIGIN + "/assets/screens/%s-%s.webp" % (n, lang["code"])
                       for n in ("home", "day", "custom", "session")
                       if any(s[0] == n for s in lang["ui"]["screens"])],  # pt/de have no "day" capture yet
        "featureList": lang["ui"]["features"],
    }
    site_ld = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Onira",
        "url": ORIGIN + "/",
        "inLanguage": [l["code"] for l in LANGS],
    }
    hero_shot = next(i for i in lang["ui"]["screens"] if i[0] == "home")
    # The home page's landscape lives inside the hero, so its hills always meet the
    # page right under the hero however tall the text wraps.
    body = ['<section class="hero">' + SCENE + '<div class="hero-text">'
            "<h1>%s</h1>\n" % esc(h["h1"]), '<p class="lede">%s</p>\n' % esc(h["lede"]),
            cta(lang),
            '</div><figure class="hero-phone"><img src="/assets/screens/home-%s.webp" '
            'width="540" height="1200" fetchpriority="high" decoding="async" alt="%s"></figure>'
            "</section>\n" % (lang["code"], esc(hero_shot[1]))]
    body.append(news(lang))
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
              + header(lang, alts, h["title"], scene=False) + "".join(body) + footer(lang))
    return write(url, markup)


def build_theme(lang, key):
    global _PAGE
    _PAGE = "%s-%s" % (lang["code"], key)
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
    global _PAGE
    _PAGE = "guide-%s-%s" % (lang["code"], key)
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


# Generated from the app repo's docs/PRIVACY_POLICY.md (source of truth); regenerate rather than edit by hand.
PRIVACY_BODY = '<h1>Onira Privacy Policy</h1>\n\n<p class="muted">Last updated: 2026-11-20</p>\n\n<p>Onira ("the app") can write your personalized sessions in two places: on your phone, where nothing you type leaves your device, or with Onira Cloud, on Onira&rsquo;s own server. On a new install Onira Cloud is selected, so that personalized sessions work on every phone without a large download; <strong>nothing is sent until you agree to it</strong>, the first time you start a personalized session. Ready-made sessions never send anything.</p>\n\n<h2>What stays on your device</h2>\n\n<ul>\n  <li>The problem category and any free-text details you enter to generate a session.</li>\n  <li>The generated hypnosis script itself.</li>\n  <li>Your language preference, narration speed, and whether you&rsquo;ve purchased "Remove Ads".</li>\n  <li>If you follow a journey (a series of sessions around one goal, such as sleep or stopping smoking): the goal, your answers to its questions, the optional date you set, the personal anchor and the short notes you write, and the ratings you give before and after each session (how it is going, how you feel). They are used to adapt your next sessions and to show your progress, and they never leave your device (except as described under cloud generation below). Ending the journey deletes them.</li>\n</ul>\n\n<p>When sessions are written on your phone, generation runs <strong>entirely on-device</strong> using a locally-stored AI model: your input and the generated script are not transmitted to Onira&rsquo;s developer or any third party.</p>\n\n<h2>What does leave your device</h2>\n\n<ul>\n  <li><strong>Cloud generation (Onira Cloud, only after you agree)</strong>: on a new install, the first time you start a personalized session (one where you typed something, or a journey session), Onira asks whether to write it with Onira Cloud. Only if you agree (or if you turn on "Write sessions in the cloud" in Settings, after the same consent screen), the app sends, over an encrypted (HTTPS) connection to Onira&rsquo;s own server (api.onirahypno.com), what is needed to write each block of your session: the session theme, your interface language, any free-text details you typed (shortened), the listener restrictions you set (for example no breathing cues) and, for a journey session, the facts that session is written from: the goal, the current phase and session number, your answers to the goal&rsquo;s questions, the anchor and notes you wrote (shortened), the trend of your ratings (not the ratings themselves), the days left until the date you set and, for stopping smoking, whether you said you smoked since the last session. The server writes the text and returns it; the text is not stored and not written to logs. The server does keep technical records without any session content: a random one-time code that links the rewarded ad you watched to your session, and a session ticket with its use count. No account is created and nothing identifies you. Choose "Keep it on my phone" in that question, or turn the setting off at any time, to keep generation fully on-device.</li>\n  <li><strong>Cloud subscription (optional)</strong>: if you subscribe to Onira Cloud, the purchase is processed by Google Play Billing. When you start a cloud session, the app sends the subscription&rsquo;s purchase token to Onira&rsquo;s server, which asks Google Play whether the subscription is active and counts your sessions for the day (up to 20). The server keeps that token (as a one-way hash for the daily count) and no personal information; no account is created.</li>\n  <li><strong>Advertising</strong>: unless you&rsquo;ve purchased "Remove Ads", the app shows ads via Google AdMob. Cloud sessions always include one rewarded ad, even with "Remove Ads". AdMob may collect device identifiers and usage data per Google&rsquo;s own privacy policy to serve and measure ads. Onira does not send your session content, category selection, or free-text input to AdMob or any ad network.</li>\n  <li><strong>Purchases</strong>: the "Remove Ads" purchase is processed by Google Play Billing; standard Google Play purchase data applies (see Google Play&rsquo;s privacy policy).</li>\n  <li><strong>Session ratings</strong>: if you rate a finished session (1-5 stars), the app sends that star count — together with the session category, your interface language, the app version, how the session was made (ready-made, replayed, generated on the device or in the cloud), how many minutes you listened, and whether any part of it had to be replaced — to Google Firebase, so the developer can see the average rating and understand a low one. Nothing identifies you, and no free-text you have typed is included. If you choose to write to support after a low rating, that message is composed in your own email app and sent by you; the app never sends it on its own.</li>\n  <li><strong>Anonymous usage counters</strong>: the app adds one to a daily counter, held at Google Firebase, when a step is reached: the app is opened, an onboarding screen is shown, a session is started (ready-made, personalized on the device, personalized in the cloud, or part of a journey, together with its theme such as "Sleep", whether it is the phone&rsquo;s first, second, third to fifth or later session, and whether it is started on a later day than the first opening; that session count stays on your phone), a session is listened to the end, a generated part of a session had to be redone or replaced, the button to share Onira or a link to review it on Google Play is tapped, or the AI model download starts, fails or finishes. The app opening and each started session are also counted under the app&rsquo;s language (English, French or Spanish), never your country. Only the number goes up. No identifier, no account, no device information, no session content and no text you typed is sent, so these counts cannot be linked to you. You can turn this off at any time with "Share anonymous usage statistics" in Settings.</li>\n  <li><strong>Model download</strong>: on first use, the app downloads the AI model weights (about 1.65 GB) over the network. This is a one-way download of app functionality, not a data upload — no user data is sent as part of this download.</li>\n  <li><strong>Narration voice download</strong>: the app also downloads Onira&rsquo;s narration voice for your language (about 80 MB), in the background and only on an unmetered connection such as Wi-Fi, from Hugging Face, the same host as the AI model. Like the model, it is a one-way download: nothing about you or your sessions is sent, and Hugging Face sees only the network request itself, as any website would.</li>\n</ul>\n\n<h2>Data retention and deletion</h2>\n\n<p>Your inputs and generated scripts are stored only in the app&rsquo;s local storage, so uninstalling the app deletes all of it. Text generated in the cloud is not kept on the server. There is no server-side account or profile to delete because none exists.</p>\n\n<h2>Children&rsquo;s privacy</h2>\n\n<p>Onira is not directed at children and is not intended for users under 13 (or the minimum age of digital consent in your jurisdiction).</p>\n\n<h2>Contact</h2>\n\n<p>Questions about this policy can be sent to <a href="mailto:support@onirahypno.com.">support@onirahypno.com.</a></p>\n'


def build_privacy():
    global _PAGE
    _PAGE = "privacy"
    en = LANGS[0]
    url = "/privacy/"
    alts = [(en["code"], url)]
    title = "Privacy Policy — Onira"
    markup = (head(en, title,
                   "Onira writes hypnosis sessions on your phone or, only if you agree, on its own "
                   "server. This policy explains what stays on your phone and what does not.",
                   url, alts, [])
              + header(en, alternates_home(), title) + PRIVACY_BODY + footer(en))
    return write(url, markup)


def press_downloads():
    """Download block of the press page. Files live under /assets/press/, not under
    /fr/, because clean() wipes the whole language tree on every build."""
    shots = "".join(
        '<li><figure><a href="/assets/press/captures-fr/%s"><img src="/assets/press/captures-fr/%s" '
        'width="540" height="960" alt="%s" loading="lazy" decoding="async"></a></figure></li>'
        % (f, f, esc(alt)) for f, alt in [
            ("2_home.png", "Onira : écran d'accueil, choix du thème et champ libre"),
            ("3_confirm.png", "Onira : confirmation de la demande et durée de la séance"),
            ("4_session.png", "Onira : séance en cours, fond à respiration lente"),
            ("5_favorites.png", "Onira : séances favorites"),
            ("6_settings.png", "Onira : réglages de la voix, du rythme et des volumes"),
        ])
    return """<h2>Télécharger le dossier</h2>
<p class="callout"><a href="/assets/press/onira-presse-fr.zip"><strong>Dossier de presse complet (zip, 4,5 Mo)</strong></a><br>
PDF mis en page, icône, logo, captures d'écran et vidéos de présentation.</p>
<ul>
<li><a href="/assets/press/onira-dossier-de-presse-fr.pdf">Dossier de presse en PDF</a></li>
<li><a href="/assets/press/onira-icone-512.png">Icône (512×512)</a></li>
<li><a href="/assets/press/onira-logo-200.png">Logo</a></li>
<li><a href="/assets/press/video/preview_16x9.mp4">Vidéo de présentation, format 16:9 (MP4)</a></li>
<li><a href="/assets/press/video/preview_9x16.mp4">Vidéo de présentation, format 9:16 (MP4)</a></li>
<li><a href="https://www.youtube.com/watch?v=DtMTGlBu2vM" rel="noopener">Vidéo de présentation sur YouTube</a></li>
</ul>
<h3>Captures d'écran (1080×1920)</h3>
<p class="muted">Ce sont les visuels de la fiche Google Play, déjà publics. Usage libre pour parler d'Onira.</p>
<ul class="shots">%s</ul>
""" % shots


def build_press():
    global _PAGE
    _PAGE = "press"
    fr = next(l for l in LANGS if l["code"] == "fr")
    url = PRESS_URL
    title = "Onira — Dossier de presse"
    with open(os.path.join(ROOT, "press_fr.html"), encoding="utf-8") as fh:
        body = fh.read().replace("@@DOWNLOADS@@", press_downloads())
    body = ('<h1>%s</h1>\n<p class="lede">Application Android d\'auto-hypnose dont l\'IA tourne '
            'sur le téléphone. Texte, visuels et contact pour la presse.</p>\n' % esc(title)
            + '<div class="press">\n' + body + "</div>\n")
    markup = (head(fr, title,
                   "Dossier de presse d'Onira, application Android d'auto-hypnose : présentation, "
                   "chiffres clés, texte à reprendre, visuels et contact.",
                   url, [(fr["code"], url)], [])
              + header(fr, alternates_home(), title) + body + footer(fr))
    return write(url, markup)


def build_404():
    global _PAGE
    _PAGE = "404"
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
    entries.append((PRESS_URL, [("fr", PRESS_URL)], "0.4"))

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

PRIVACY_SUMMARY = ("Personalized sessions are written on the phone or, only after the user "
                   "agrees, with Onira Cloud (encrypted, not stored); new installs are asked "
                   "the first time they start one, ready-made sessions send nothing. Ads (Google AdMob, unless removed), Play Billing purchases "
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
            "- [Dossier de presse (FR)](%s%s): press kit in French, with downloadable visuals" % (ORIGIN, PRESS_URL),
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
    pages = ["/privacy/", PRESS_URL]
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
    written.append(build_press())
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
