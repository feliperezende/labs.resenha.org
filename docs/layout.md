# labs.resenha.org — Layout & Information Architecture

## Site Concept
**Living lab notebook** — curated technical experiments across systems, mobile, web. No marketing, no portfolio vibe. Written for future self and peers.

---

## Global Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  HEADER (sticky, minimal)                                       │
│  ┌──────────────────┐                    ┌──────────────────┐  │
│  │ labs.resenha.org │                    │ [GitHub] [RSS]   │  │
│  │  monospace logo  │                    │  theme toggle    │  │
│  └──────────────────┘                    └──────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│  MAIN (max-w-5xl mx-auto px-6 py-12)                            │
│                                                                 │
│  {{page content}}                                               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  FOOTER (minimal)                                               │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Felipe Rezende · Engineering Manager @ Nubank · São Paulo │  │
│  │ GitHub · LinkedIn · Email · RSS · Source on GitHub        │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Page Layouts

### 1. Home (`/`)
```
┌─────────────────────────────────────────────────────────────────┐
│  HERO (above fold)                                              │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                                                           │  │
│  │   labs.resenha.org                                        │  │
│  │   technical experiments · systems · mobile · web          │  │
│  │                                                           │  │
│  │   [Live Demo: rotating iframe of latest experiment]       │  │
│  │   ▲ amber badge: "LIVE"                                   │  │
│  │                                                           │  │
│  └───────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│  LATEST EXPERIMENTS (3 cards)                                   │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
│  │ futmanager-  │ │ apk-receiver │ │ clj-telebot  │            │
│  │ wasm         │ │              │ │              │            │
│  │ [Rust]       │ │ [Kotlin]     │ │ [Clojure]    │            │
│  │ Systems      │ │ Mobile       │ │ Tooling      │            │
│  │ 2026-10-13   │ │ 2026-10-10   │ │ 2026-09-29   │            │
│  │ [Read]       │ │ [Read]       │ │ [Read]       │            │
│  └──────────────┘ └──────────────┘ └──────────────┘            │
├─────────────────────────────────────────────────────────────────┤
│  NOW (current focus)                                            │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  🔬 Building WASM-based football manager simulation       │  │
│  │  📱 Shipping Android→TV APK bridge                        │  │
│  │  📖 Reading: "Crafting Interpreters" · Tinkering: Luau   │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Experiments Index (`/experiments`)
```
┌─────────────────────────────────────────────────────────────────┐
│  PAGE HEADER                                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Experiments                                    [Filters] │  │
│  │  10 public experiments across 4 groups                     │  │
│  └───────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│  FILTER BAR (sticky on scroll)                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Groups: [All] [Systems] [Mobile] [Web] [Foundational]    │  │
│  │  Languages: [All] [Rust] [Kotlin] [Clojure] [JS] [HTML]   │  │
│  │  Status: [All] [Active] [Archived] [Learning]             │  │
│  │  Sort: [Recent] [Stars] [Alphabetical]                    │  │
│  └───────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│  EXPERIMENTS GRID (responsive: 1col mobile, 2col tablet,       │
│  3col desktop)                                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────┐  │  │
│  │  │ Card 1  │ │ Card 2  │ │ Card 3  │ │ Card 4  │ │...  │  │  │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────┘  │  │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────┐  │  │
│  │  │ Card 5  │ │ Card 6  │ │ Card 7  │ │ Card 8  │ │...  │  │  │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│  EMPTY STATE (if filters yield nothing)                         │
│  "No experiments match. Try clearing filters."                  │
└─────────────────────────────────────────────────────────────────┘
```

### 3. Experiment Detail (`/experiments/[slug]`)
```
┌─────────────────────────────────────────────────────────────────┐
│  BREADCRUMB                                                     │
│  Home / Experiments / futmanager-wasm                           │
├─────────────────────────────────────────────────────────────────┤
│  EXPERIMENT HEADER                                              │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  futmanager-wasm              [GitHub] [Live Demo?]       │  │
│  │  Systems & WASM Tooling  ·  Rust  ·  Updated 2026-10-13  │  │
│  │  ★ 0  ·  Private: No  ·  Status: Active                   │  │
│  └───────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│  CONTENT (MDX, prose + code blocks + diagrams)                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  ## Context                                                │  │
│  │  Why this exists. Problem statement. Constraints.         │  │
│  │                                                            │  │
│  │  ## Architecture                                           │  │
│  │  Mermaid diagrams, component breakdown, data flow.        │  │
│  │  ```mermaid                                                │  │
│  │  graph LR ...                                              │  │
│  │  ```                                                       │  │
│  │                                                            │  │
│  │  ## Key Decisions                                          │  │
│  │  - WASM over JS for deterministic simulation              │  │
│  │  - ECS pattern for entity management                      │  │
│  │                                                            │  │
│  │  ## What Worked / What Didn't                              │  │
│  │  ✅ WASM performance met 60fps target                     │  │
│  │  ❌ Memory leaks in long-running matches                  │  │
│  │                                                            │  │
│  │  ## Artifacts                                              │  │
│  │  - [GitHub Repo] [Live Demo] [WASM Bundle Analyzer]       │  │
│  │                                                            │  │
│  │  ## Reflection                                             │  │
│  │  "Would I revisit? Yes — the ECS core is reusable..."     │  │
│  └───────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│  RELATED EXPERIMENTS (sidebar or bottom)                        │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Related: clj-telebot · clj-tasks · augdrive              │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 4. Lab Reports (`/lab-reports`)
```
┌─────────────────────────────────────────────────────────────────┐
│  PAGE HEADER                                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Lab Reports · Quarterly synthesis posts                  │  │
│  └───────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│  POST LIST (newest first)                                       │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │ Q4 2026: WASM in Production                       │  │  │
│  │  │ What I learned shipping Rust→WASM for games...    │  │  │
│  │  │ 2026-10-15  ·  8 min read  ·  [Read]              │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │ Q3 2026: Android→TV Networking                     │  │  │
│  │  │ Building a local-first file bridge without cloud  │  │  │
│  │  │ 2026-07-10  ·  12 min read  ·  [Read]             │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 5. Now Page (`/now`)
```
┌─────────────────────────────────────────────────────────────────┐
│  NOW (updated manually, timestamped)                            │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Last updated: 2026-10-31                                 │  │
│  │                                                           │  │
│  │  ## Building                                              │  │
│  │  - futmanager-wasm: ECS + deterministic simulation        │  │
│  │  - apk-receiver: local network file bridge                │  │
│  │                                                           │  │
│  │  ## Reading                                               │  │
│  │  - "Crafting Interpreters" (Bob Nystrom)                 │  │
│  │  - "Designing Data-Intensive Applications" (Kleppmann)   │  │
│  │                                                           │  │
│  │  ## Tinkering                                             │  │
│  │  - Luau/Roblox prototypes (private)                       │  │
│  │  - Swift concurrency patterns                             │  │
│  │                                                           │  │
│  │  ## Speaking / Writing                                    │  │
│  │  - None scheduled                                         │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 6. About (`/about`)
```
┌─────────────────────────────────────────────────────────────────┐
│  ABOUT                                                          │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Felipe Rezende                                           │  │
│  │  Engineering Manager @ Nubank · São Paulo, BR             │  │
│  │                                                           │  │
│  │  This is my technical lab notebook. I build experiments   │  │
│  │  in systems programming, mobile, and web — mostly for     │  │
│  │  learning, sometimes for utility.                         │  │
│  │                                                           │  │
│  │  ## Contact                                               │  │
│  │  GitHub: github.com/feliperezende                         │  │
│  │  LinkedIn: in/felipe-rezende-em                           │  │
│  │                                                           │  │
│  │  ## Speaking / Writing                                    │  │
│  │  - [links to talks, posts, podcasts]                      │  │
│  │                                                           │  │
│  │  ## This Site                                             │  │
│  │  Built with Astro + Tailwind + Cloudflare Pages           │  │
│  │  Source: github.com/feliperezende/labs.resenha.org        │  │
│  │  Analytics: Plausible (privacy-first, no cookies)         │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Experiment Card Component

```
┌─────────────────────────────────────────────────────────────────┐
│  CARD (group accent color top border: 3px)                      │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │ futmanager-wasm                          [Rust]    │  │  │
│  │  │ Systems & WASM Tooling                              │  │  │
│  │  │                                                     │  │  │
│  │  │ Football manager simulation with deterministic      │  │  │
│  │  │ match engine compiled to WebAssembly...             │  │  │
│  │  │                                                     │  │  │
│  │  │ Updated 2026-10-13  ·  ★0  ·  Active                │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

**Group accent colors:**
- Systems & WASM: `cyan` (#06B6D4)
- Mobile & Platform: `emerald` (#10B981)
- Web & Infra: `violet` (#8B5CF6)
- Foundational: `slate` (#64748B)

---

## Responsive Breakpoints

| Breakpoint | Grid Columns | Notes |
|------------|--------------|-------|
| `< 640px` | 1 | Stack cards, full-width filters |
| `640-1024px` | 2 | Side-by-side cards |
| `> 1024px` | 3 | Three-column grid |

---

## Technical Components Needed

| Component | Purpose |
|-----------|---------|
| `Layout.astro` | Global wrapper (header, main, footer) |
| `Header.astro` | Logo, theme toggle, nav links |
| `Footer.astro` | Minimal contact + source link |
| `ExperimentCard.astro` | Grid card with group accent |
| `ExperimentDetail.astro` | MDX layout with frontmatter |
| `FilterBar.astro` | Client-side filter (vanilla JS or Alpine) |
| `LiveDemo.astro` | Rotating iframe for home hero |
| `Breadcrumb.astro` | Navigation context |
| `RelatedExperiments.astro` | Cross-linking by group/tags |

---

## Content Schema (Astro Content Collections)

```typescript
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const experiments = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    group: z.enum(['systems-wasm', 'mobile-platform', 'web-infra', 'foundational']),
    language: z.string(),
    description: z.string(),
    updatedAt: z.string().datetime(),
    stars: z.number().default(0),
    status: z.enum(['active', 'archived', 'learning']).default('active'),
    private: z.boolean().default(false),
    github: z.string().url().optional(),
    demo: z.string().url().optional(),
    tags: z.array(z.string()).default([]),
  }),
});

const labReports = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    date: z.string().date(),
    description: z.string(),
    readTime: z.string(),
    tags: z.array(z.string()).default([]),
  }),
});

export const collections = { experiments, labReports };
```