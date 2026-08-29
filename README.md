# onirahypno.com

Static site for the Onira Android app, published via GitHub Pages at
<https://onirahypno.com/>. It is both the app's public site and its SEO surface:
one page per session theme, per language, plus the privacy policy used as the
Play Console policy URL.

## ⚠️ The privacy policy moved to `/privacy/`

The root URL used to serve the policy. It now serves the English home page, and the
policy lives at <https://onirahypno.com/privacy/>. **Play Console's privacy policy
URL must be updated to `https://onirahypno.com/privacy/`** (Play Console → Policy →
App content → Privacy policy). Until that is done, Play points at a page that is no
longer the policy.

## Layout

```
index.html                     English home
hypnosis/<slug>/               English theme pages (anxiety, sleep, …)
fr/  fr/hypnose/<slug>/        French
es/  es/hipnosis/<slug>/       Spanish
privacy/                       Privacy policy (English, shared by all languages)
assets/site.css                The only stylesheet
sitemap.xml  robots.txt  404.html
```

Every page is generated. Do not hand-edit the HTML — edit `content.py` and rebuild.

## Building

```bash
python3 build.py
```

No dependencies beyond the standard library. `build.py` owns the template,
canonical URLs, reciprocal `hreflang` alternates, breadcrumbs, JSON-LD and the
sitemap; `content.py` owns every word of copy, keyed by language. Regenerated files
are committed — GitHub Pages serves them directly, there is no build on the Pages
side, so **a change to `content.py` is not live until you rerun `build.py` and
commit the result.**

## Adding a language

1. Copy an existing language block in `content.py` (`EN`, `FR`, `ES`), translate it,
   and set `code` / `base` / `theme_dir` / slugs.
2. Append it to `LANGS`.
3. `python3 build.py`, commit, push.

The `THEMES` keys must stay identical across languages — `hreflang` alternates are
matched on those keys, not on slugs, so a missing key breaks the alternate set for
that theme. The slugs themselves should be the natural search phrasing in each
language, not transliterations of the English ones.

Keep the language list in step with the app's `SupportedLanguage`
(`data/LocaleManager.kt` in the [mindease](https://github.com/cfournel/mindease)
repo): a landing page in a language the app cannot narrate is a bad first impression.

## SEO notes

- Each theme page targets one intent in one language ("self-hypnosis for anxiety",
  "auto-hypnose pour le sommeil", …), with an FAQ block marked up as `FAQPage`.
- Every page declares a canonical URL and a full reciprocal `hreflang` set including
  `x-default` (English). The sitemap repeats the alternates per URL.
- After a content change, resubmit `sitemap.xml` in Google Search Console.
- No analytics, no third-party scripts, no cookies — deliberately, so the site
  matches the privacy claim the app makes.

## Health and safety claims

Every theme page carries the same two non-negotiable blocks, emitted by
`build.py` (`privacy_and_safety`): Onira is a relaxation tool, not therapy or
medical advice, and a pointer to local crisis services. Copy that softens or
drops those, or that promises a clinical outcome ("cures anxiety", "guarantees you
quit"), is both untrue and a Play policy problem for a health-adjacent app. The
smoking and weight pages are the ones to watch — keep them descriptive.

## Naming

The app was renamed from MindEase to Onira at versionCode 31. This repo, and the
main one, keep their original names on purpose: the Play `applicationId` is frozen
at `com.oytaub.mindease` for the lifetime of the listing, so `mindease` remains the
technical identifier everywhere. Only user-visible text says Onira.

## Custom domain

Live: `onirahypno.com` resolves to GitHub Pages and the `CNAME` file in this repo
pins the domain. Removing or changing `CNAME` takes the site — and the Play policy
URL — offline.
