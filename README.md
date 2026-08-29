# Onira Privacy Policy

Static privacy policy page for the Onira Android app, published via GitHub Pages
for use as the Play Console privacy policy URL.

Live at <https://cfournel.github.io/mindease-privacy-policy/> until the custom
domain `onirahypno.com` is pointed here — see "Custom domain" below.

Source content also lives in `docs/PRIVACY_POLICY.md` in the main
[mindease](https://github.com/cfournel/mindease) repo — keep both in sync when the
policy changes.

## Naming

The app was renamed from MindEase to Onira at versionCode 31. This repo, and the
main one, keep their original names on purpose: the Play `applicationId` is frozen
at `com.oytaub.mindease` for the lifetime of the listing, so `mindease` remains the
technical identifier everywhere. Only user-visible text says Onira.

## Custom domain

Not enabled yet. Adding a `CNAME` file here makes GitHub Pages serve the site
**only** from that domain — so the DNS records must resolve *first*, or the policy
URL goes dark and Play Console's link breaks.

Order of operations:

1. At the registrar, point `onirahypno.com` at GitHub Pages — four `A` records to
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`, and
   a `CNAME` for `www` to `cfournel.github.io`.
2. Wait for the records to resolve.
3. Only then add a `CNAME` file containing `onirahypno.com` and enable HTTPS in the
   repo's Pages settings.
