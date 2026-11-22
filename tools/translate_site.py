"""Draft translation of the English site copy (content.EN) into another language with the local teacher LLM (mindease#57).

Writes tools/drafts/<lang>.json: the EN dict with every copy string translated, unit by unit (ui, home, each theme, each
guide). Slugs and codes are left in English: they are chosen by hand (natural search phrasing), as is every fact that
differs per language (narration voice, helplines). This is a draft for review, never published as is.
Resumable: units already in the output are kept.

Usage: python3 tools/translate_site.py pt|de [--url http://127.0.0.1:8080] [--model qwen36-35b]
"""
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import content  # noqa: E402

LANG = sys.argv[1]
URL = sys.argv[sys.argv.index("--url") + 1] if "--url" in sys.argv else "http://127.0.0.1:8080"
MODEL = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "qwen36-35b"
TARGET = {
    "pt": "Brazilian Portuguese (address the reader as \"você\", natural Brazilian wording)",
    "de": "German (address the reader informally as \"du\", natural German wording)",
}[LANG]
KEEP = {"slug", "code", "base", "label", "name", "theme_dir", "guide_dir", "privacy_slug"}
OUT = ROOT / "tools" / "drafts" / f"{LANG}.json"


def plain(v):
    if isinstance(v, dict):
        return {k: plain(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [plain(x) for x in v]
    return v


def strip(v, key=None):
    """The translatable part: drop the kept keys (put back after)."""
    if isinstance(v, dict):
        return {k: strip(x, k) for k, x in v.items() if k not in KEEP}
    if isinstance(v, list):
        return [strip(x) for x in v]
    return v


def merge(orig, tr):
    if isinstance(orig, dict):
        return {k: (orig[k] if k in KEEP else merge(orig[k], tr.get(k) if isinstance(tr, dict) else None)) for k in orig}
    if isinstance(orig, list):
        tr = tr if isinstance(tr, list) and len(tr) == len(orig) else [None] * len(orig)
        return [merge(o, t) for o, t in zip(orig, tr)]
    return tr if isinstance(tr, type(orig)) and tr else orig


def count_untranslated(orig, tr):
    if isinstance(orig, dict):
        return sum(count_untranslated(orig[k], tr[k]) for k in orig if k not in KEEP)
    if isinstance(orig, list):
        return sum(count_untranslated(o, t) for o, t in zip(orig, tr))
    return int(isinstance(orig, str) and len(orig) > 12 and orig == tr)


def ask(unit_json: str) -> str:
    prompt = (
        f"Translate the string values of this JSON object from English into {TARGET}. It is the copy of the website of "
        "Onira, a self-hypnosis app (Android). Rules:\n"
        "- Return ONLY the JSON object, same keys, same structure, same number of list items; translate values, never keys.\n"
        "- Keep markdown (**bold**), HTML tags, line breaks (\\n), placeholders like %s or {name}, and URLs exactly as they are.\n"
        "- Keep the names Onira, Onira Cloud, Google Play, Android unchanged.\n"
        "- Write like a native copywriter for a search-friendly health and wellbeing site: clear, warm, accurate; no literal"
        " calques. Keep every factual claim exactly as strong as in English (do not add or remove promises).\n"
        "- Titles and descriptions should use the words people in that country actually search for (e.g. the usual term"
        " for self-hypnosis, insomnia, anxiety, quitting smoking).\n\n" + unit_json
    )
    body = {"model": MODEL, "messages": [{"role": "user", "content": prompt}], "temperature": 0.3, "top_p": 0.9,
            "max_tokens": 16000, "chat_template_kwargs": {"enable_thinking": False}}
    r = urllib.request.Request(URL + "/v1/chat/completions", json.dumps(body).encode(), {"Content-Type": "application/json"})
    with urllib.request.urlopen(r, timeout=3600) as resp:
        return json.load(resp)["choices"][0]["message"]["content"]


def parse(text: str):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    return json.loads(text[text.index("{"): text.rindex("}") + 1])


def main():
    en = plain(content.EN)
    units = [("ui", en["ui"]), ("home", en["home"])]
    units += [(f"themes.{k}", v) for k, v in en["themes"].items()]
    units += [(f"guides.{k}", v) for k, v in en["guides"].items()]
    OUT.parent.mkdir(exist_ok=True)
    done = json.loads(OUT.read_text()) if OUT.exists() else {}
    for name, unit in units:
        if name in done:
            continue
        merged = None
        for attempt in range(3):
            try:
                tr = parse(ask(json.dumps(strip(unit), ensure_ascii=False, indent=1)))
                merged = merge(unit, tr)
                left = count_untranslated(unit, merged)
                if left <= 1:
                    break
                print(f"{name}: {left} strings left in English, retry", flush=True)
            except (ValueError, KeyError) as e:
                print(f"{name}: {type(e).__name__}, retry", flush=True)
        else:
            # Long units sometimes come back as broken JSON (an unescaped quote): translate them one field at a time.
            print(f"{name}: whole unit failed, field by field", flush=True)
            tr = {}
            for k, v in strip(unit).items():
                for attempt in range(3):
                    try:
                        tr[k] = parse(ask(json.dumps({k: v}, ensure_ascii=False, indent=1)))[k]
                        break
                    except (ValueError, KeyError) as e:
                        print(f"{name}.{k}: {type(e).__name__}, retry", flush=True)
            merged = merge(unit, tr)
            print(f"{name}: {count_untranslated(unit, merged)} strings left in English", flush=True)
        done[name] = merged
        OUT.write_text(json.dumps(done, ensure_ascii=False, indent=1))
        print(f"{name} ok ({len(done)}/{len(units)})", flush=True)
    print("done", len(done), "/", len(units))


if __name__ == "__main__":
    main()
