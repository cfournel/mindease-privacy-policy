#!/usr/bin/env python3
"""Search Console report for onirahypno.com: traffic trend, top pages/queries, indexation.

Needs Application Default Credentials with the webmasters.readonly scope:
    gcloud auth application-default login \
        --scopes=https://www.googleapis.com/auth/webmasters.readonly,https://www.googleapis.com/auth/cloud-platform
and a project with the Search Console API enabled (GSC_QUOTA_PROJECT, default below).

Usage: python3 gsc_report.py [--days 28] [--no-inspect] [--email ADDRESS]
--email sends it through Gmail SMTP; credentials in ~/.config/gsc-report.env, see
send_mail(). The report is saved to
~/gsc-reports/YYYY-MM-DD.md either way.
Check monthly: nothing on this site moves in days (see marketing/BACKLINKS.md).
"""
import argparse
import collections
import contextlib
import datetime
import email.message
import io
import json
import os
import re
import smtplib
import subprocess
import urllib.request

SITE = "sc-domain:onirahypno.com"
QUOTA_PROJECT = os.environ.get("GSC_QUOTA_PROJECT", "arcane-bit-505212-f8")
HERE = os.path.dirname(os.path.abspath(__file__))


def token():
    return subprocess.check_output(
        ["gcloud", "auth", "application-default", "print-access-token"]).decode().strip()


def call(url, body):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + token(),
                 "x-goog-user-project": QUOTA_PROJECT,
                 "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req))


def query(start, end, dims=None, limit=25):
    body = {"startDate": str(start), "endDate": str(end), "rowLimit": limit}
    if dims:
        body["dimensions"] = dims
    url = "https://www.googleapis.com/webmasters/v3/sites/%s/searchAnalytics/query" % \
        SITE.replace(":", "%3A")
    return call(url, body).get("rows", [])


def totals(start, end):
    rows = query(start, end)
    return rows[0] if rows else {"clicks": 0, "impressions": 0, "ctr": 0, "position": 0}


def indexation():
    urls = sorted(set(re.findall(r"<loc>([^<]+)", open(os.path.join(HERE, "sitemap.xml")).read())))
    states = collections.Counter()
    missing = []
    for u in urls:
        r = call("https://searchconsole.googleapis.com/v1/urlInspection/index:inspect",
                 {"inspectionUrl": u, "siteUrl": SITE})
        state = r["inspectionResult"]["indexStatusResult"].get("coverageState", "?")
        states[state] += 1
        if not state.startswith("Submitted and indexed"):
            missing.append((u, state))
    return len(urls), states, missing


def send_mail(to, subject, body):
    """Gmail SMTP with an app password: gcloud's OAuth client is blocked for gmail.send.

    Credentials live outside the repo, in ~/.config/gsc-report.env (chmod 600):
        GMAIL_USER=you@gmail.com
        GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
    """
    env = {}
    with open(os.path.expanduser("~/.config/gsc-report.env")) as f:
        for line in f:
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.strip().split("=", 1)
                env[k] = v.strip().strip("\"'")
    msg = email.message.EmailMessage()
    msg["From"], msg["To"], msg["Subject"] = env["GMAIL_USER"], to, subject
    msg.set_content(body)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(env["GMAIL_USER"], env["GMAIL_APP_PASSWORD"].replace(" ", ""))
        smtp.send_message(msg)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", help="send the report to this address")
    ap.add_argument("--days", type=int, default=28)
    ap.add_argument("--no-inspect", action="store_true")
    a = ap.parse_args()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report(a)
    text = buf.getvalue()
    print(text)
    outdir = os.path.expanduser("~/gsc-reports")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "%s.md" % datetime.date.today()), "w") as f:
        f.write(text)
    if a.email:
        send_mail(a.email, "onirahypno.com Search Console, %s" % datetime.date.today(), text)


def report(a):
    # Search Console data lags ~2 days.
    end = datetime.date.today() - datetime.timedelta(days=2)
    start = end - datetime.timedelta(days=a.days - 1)
    p_end = start - datetime.timedelta(days=1)
    p_start = p_end - datetime.timedelta(days=a.days - 1)

    cur, prev = totals(start, end), totals(p_start, p_end)
    print("# onirahypno.com — %s to %s (vs %s to %s)\n" % (start, end, p_start, p_end))
    for k in ("clicks", "impressions"):
        print("- %s: %d (previous %d)" % (k, cur[k], prev[k]))
    print("- avg position: %.1f (previous %.1f)\n" % (cur["position"], prev["position"]))

    for dim, title in (("page", "Pages"), ("query", "Queries"), ("country", "Countries")):
        print("## %s\n" % title)
        for r in query(start, end, [dim], 10):
            print("- %s — %d imp, %d clicks, pos %.1f" % (
                r["keys"][0].replace("https://onirahypno.com", ""),
                r["impressions"], r["clicks"], r["position"]))
        print()

    if not a.no_inspect:
        n, states, missing = indexation()
        print("## Indexation (%d sitemap URLs)\n" % n)
        for s, c in states.most_common():
            print("- %s: %d" % (s, c))
        for u, s in missing:
            print("  - %s — %s" % (u.replace("https://onirahypno.com", ""), s))


if __name__ == "__main__":
    main()
