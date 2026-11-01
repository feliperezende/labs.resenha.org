# labs.resenha.org

A living lab notebook — curated technical experiments across systems, mobile and web.
Astro + Tailwind v4, static, deployed to GitHub Pages by GitHub Actions.

## Commands

```
npm install
npm run dev -- --port 4322     # http://localhost:4322
npm run build                  # → dist/
npm run preview
```

## Content

Experiments are markdown files in `src/content/experiments/<slug>.md`; the frontmatter
schema lives in `src/content.config.ts`. Pages read the collection — never hardcode
cards in a template.

Adding an entry:

```
npm run new:entry -- my-project   # scaffold (optional helper, see scripts/)
```

The prose sections (`Hypothesis`, `Retrospective`) are written by hand, in Felipe's
voice. Entries generated from repo evidence carry a `DRAFT` comment at the top.

## Deploy

Pushes to `master` build and publish through `.github/workflows/deploy.yml`.
Details, including the custom-domain switch, are in `docs/DEPLOY.md`.

## Stack

- Astro 7 (static output) + content collections (glob loader, Zod schema)
- Tailwind CSS v4 (CSS-first `@theme` in `src/styles/global.css`)
- No client-side JS beyond CSS animations; no framework islands