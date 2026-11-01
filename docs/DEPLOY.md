# Deploy — GitHub Pages

Static build published by `.github/workflows/deploy.yml` on every push to `master`.

## Current setup (custom domain)

- Repository: `github.com/feliperezende/labs.resenha.org`
- URL: **https://labs.resenha.org** (custom domain, `public/CNAME` committed)
- DNS: `CNAME labs → feliperezende.github.io` at the `resenha.org` provider
  (resolves to the Pages IPs `185.199.108-111.153`)
- Pages source: **GitHub Actions** (Settings → Pages → Source)
- `astro.config.mjs` defaults:
  - `site = https://labs.resenha.org`
  - `base = /`

Every internal link, the favicon and the RSS autodiscovery go through
`withBase()` in `src/config/site.ts`, so a subpath build still works if needed.

The old project-pages URL `https://feliperezende.github.io/labs.resenha.org/`
now redirects to the custom domain — GitHub serves Pages at one address only.

## Why the artifact, not a branch

The `deploy-pages` action publishes exactly what CI built, so `dist/` is never
committed and there is no `gh-pages` branch to keep in sync. `.gitignore` keeps
`dist/` out of history.

## Subpath build (rollback / pre-DNS)

```bash
SITE=https://feliperezende.github.io BASE=/labs.resenha.org npm run build
```

To go back to project pages for real: delete `public/CNAME`, drop the custom
domain in Settings → Pages, and set the defaults above back to the
`feliperezende.github.io` / `/labs.resenha.org` pair.

## Certificates

Settings → Pages → **Enforce HTTPS** must be ticked once GitHub provisions the
Let's Encrypt certificate for the custom domain (can take a few minutes after the
first deploy following the DNS change).

## Local checks before pushing

```bash
npm run build                     # project-pages mode
BASE=/ SITE=https://labs.resenha.org npm run build   # custom-domain mode
npm run preview                   # serve dist/ locally
```

`npm run preview` serves the build at the configured `base`, so click a few links
after changing URLs.