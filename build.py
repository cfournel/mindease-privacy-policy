#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator for onirahypno.com.

    python3 build.py

Writes the whole site (home + theme pages per language, privacy policy,
sitemap, robots.txt, 404) into the repo root from the copy in `content.py`.
Generated files are committed — GitHub Pages serves them as-is, there is no
build step on the Pages side.

Everything cross-cutting that SEO depends on — canonical URLs, reciprocal
hreflang alternates, breadcrumbs, JSON-LD — is derived here rather than typed
per page, so adding a language or a theme cannot silently produce a half-linked
page. Rerun after any edit to `content.py`; `git status` shows what changed.
"""

import html
import json
import os
import shutil

from content import SITE, THEMES, LANGS

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
<link rel="stylesheet" href="/assets/site.css">%(blocks)s
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
    return """<header class="site-head"><div class="wrap">
  <a class="mark" href="%s">%s<span>%s</span></a>
  <nav class="langs" aria-label="%s">%s</nav>
</div></header>
<main class="wrap">
""" % (home_url(lang), MARK, esc(title), esc(lang["ui"]["langs_label"]), langs)


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
  <p>%s</p>
</div></footer>
</body>
</html>
""" % (items, esc(lang["ui"]["foot_tag"]))


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
    for key in THEMES:
        if key == exclude:
            continue
        t = lang["themes"][key]
        lis.append('<li><a href="%s"><strong>%s</strong><span>%s</span></a></li>'
                   % (theme_url(lang, key), esc(t["nav"]), esc(t["card"])))
    return '<ul class="cards">%s</ul>\n' % "".join(lis)


def write(url, markup):
    path = out_path(url)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(markup)
    return path


# ------------------------------------------------------------------ pages ----

def alternates_home():
    return [(l["code"], home_url(l)) for l in LANGS]


def alternates_theme(key):
    return [(l["code"], theme_url(l, key)) for l in LANGS]


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

    markup = (head(lang, t["title"], t["desc"], url, alts, [crumbs_ld, faq_ld])
              + header(lang, alts, t["title"]) + "".join(body) + footer(lang))
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
        for lang in LANGS:
            entries.append((theme_url(lang, key), alternates_theme(key), "0.8"))
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
        out.append("    <lastmod>%s</lastmod>" % SITE["updated"])
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


def clean():
    """Drop generated language/theme trees so renamed slugs don't leave orphans."""
    for lang in LANGS:
        for d in filter(None, [lang["base"], os.path.join(lang["base"], lang["theme_dir"])
                               if lang["base"] else lang["theme_dir"]]):
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


def main():
    clean()
    written = [build_favicon_svg()]
    for lang in LANGS:
        written.append(build_home(lang))
        for key in THEMES:
            written.append(build_theme(lang, key))
    written.append(build_privacy())
    written.append(build_404())
    written.append(build_sitemap())
    written.append(build_robots())
    for path in written:
        print(os.path.relpath(path, ROOT))
    print("\n%d files written" % len(written))


if __name__ == "__main__":
    main()
