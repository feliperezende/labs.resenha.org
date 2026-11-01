// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// ── GitHub Pages ─────────────────────────────────────────────────────────────
// Serving on the custom domain: labs.resenha.org (CNAME → feliperezende.github.io).
// The project-pages URL is a redirect now, so the custom domain is the default.
//
// Building for a subpath (pre-DNS testing) still works:
//   SITE=https://feliperezende.github.io BASE=/labs.resenha.org npm run build
// See docs/DEPLOY.md.
const site = process.env.SITE ?? 'https://labs.resenha.org';
const base = process.env.BASE ?? '/';

export default defineConfig({
  site,
  base,
  trailingSlash: 'ignore',
  vite: {
    plugins: [tailwindcss()],
  },
});