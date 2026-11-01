#!/usr/bin/env python
# Generates src/content/experiments/*.md from REAL GitHub metadata (pulled 2026-10-31)
# plus prose grounded in each repo's README. Draft sections are marked.
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "src" / "content" / "experiments"
OUT.mkdir(parents=True, exist_ok=True)

HEADER = "<!-- DRAFT: 'hypothesis' and 'retrospective' sections were drafted by Hermes from repo\n     evidence (README, metadata) and are marked (draft). Rewrite them in your own voice. -->\n\n"

E = [
dict(slug="futmanager-wasm", title="futmanager-wasm", group="systems-wasm", language="Rust",
     date="2026-10-13", stars=0, status="active", tags=["wasm","simulation","rust","retro"],
     desc="Browser football manager (FutManager 98) with the match engine written in Rust and compiled to WebAssembly, behind a retro Windows 98 interface.",
     body="""## Hypothesis (draft)

Can a manager game of the 90s school run **entirely in the browser** if the engine is Rust compiled to WebAssembly, instead of shipping a desktop binary per platform?

## Stack & constraints

- **Rust → WebAssembly** via `wasm-bindgen` (`src/lib.rs`).
- **UI**: plain HTML/CSS/JS in `www/`, styled as a Windows 98 pastiche, in **pt-BR**.
- **Clean-room**: no code, data, names or files from other games — every club and player is fictional and generated procedurally.

## What shipped

- 4 divisions, 16 fictional clubs each.
- Squads of 18 players plus a free-agent market.
- Players carry position (GK/DEF/MID/ATT), ability and attributes (finishing, passing, marking, goalkeeping).

## Retrospective (draft)

- The clean-room constraint shaped the whole data model — everything had to be generated, so the generator became a first-class part of the game rather than a seed script.
"""

),
dict(slug="apk-receiver", title="apk-receiver", group="mobile-platform", language="Kotlin",
     date="2026-10-10", stars=0, status="active", tags=["android","kotlin","lan","apk"],
     desc="Send APK download URLs from an iPhone to an Android TV box over the local network. Local-first, no cloud, no Play Services.",
     body="""## Hypothesis (draft)

Getting an install artifact from an iPhone to an Android TV box shouldn't require a cloud hop, a USB stick or Play Services — the two devices are already on the same LAN.

## Stack & constraints

- **Kotlin** app on the box, running a tiny local HTTP server.
- Downloads handled by Android's `DownloadManager`, then handed to the package installer (silent install when the box is rooted).
- The iPhone needs nothing but a browser.
- CI builds the APK through GitHub Actions; releases are published per build.

## What shipped

- The box shows a **QR code**; scanning it from the phone opens the send page.
- URLs sent from the iPhone arrive on the box, download, and open the installer.
- Works on plain **AOSP** boxes — no Play Services required.

## Retrospective (draft)

- The "no cloud" constraint turned the QR code into the whole pairing story — less code than any account-based flow would have needed.
"""

),
dict(slug="treino-gallant", title="treino-gallant", group="web-infra", language="HTML",
     date="2026-10-04", stars=0, status="active", tags=["html","timer","fitness"],
     desc="Timer for the spinning workouts at Gallant X. Single page, no install, works offline.",
     body="""## Hypothesis (draft)

A class timer should be one page you can open from a phone with no install and no network.

## Stack & constraints

- Single **HTML** page. No build step, no dependencies, no README in the repo.

## What shipped

- A timer for the spinning workouts at Gallant X (`Timer dos treinos de spinning na Gallant X`).

## Retrospective (draft)

- Entry needs a proper write-up: there is no README in the repository, so this card is metadata only.
"""

),
dict(slug="clj-telebot", title="clj-telebot", group="systems-wasm", language="Clojure",
     date="2026-09-28", stars=1, status="active", tags=["clojure","telegram","bot","yt-dlp"],
     desc="Small Clojure Telegram bot client using the Telegram HTTP API (long polling). Minimal, functional, composable.",
     body="""## Hypothesis (draft)

How small can a Telegram bot be in Clojure with no framework — just the HTTP API and a loop?

## Stack & constraints

- **Clojure** + **Hato** (HTTP) + **Cheshire** (JSON), long-polling the Bot API.
- **Leiningen** for build; Java 8+ (CI on Temurin 21).
- `yt-dlp` and `ffmpeg` on `PATH` for video downloads.
- Fails fast: a missing `TELEGRAM_BOT_TOKEN` throws on the first API call rather than starting half-configured.

## What shipped

- Echoes text, reports uptime.
- Downloads videos through `yt-dlp` with **per-chat rate limiting**.
- Ships as a standalone jar.

## Retrospective (draft)

- The interesting part was not the bot but the boundary: rate limiting and external binaries (`yt-dlp`/`ffmpeg`) are where a "tiny" bot stops being tiny.
"""

),
dict(slug="dom-cleaner", title="dom-cleaner", group="web-infra", language="JavaScript",
     date="2026-09-20", stars=0, status="active", tags=["chrome-extension","mv3","ads","ai"],
     desc="Chrome extension (Manifest V3) that removes ad iframes, autoplay players and cookie consent modals with a 0ms heuristic fast path plus zero-shot AI classification.",
     body="""## Hypothesis (draft)

Most intrusive page junk is unambiguously identifiable from the DOM alone. A 0ms heuristic can clear that tier, and an AI classifier should only ever see the ambiguous remainder.

## Stack & constraints

- **Chrome extension, Manifest V3**.
- **Tier 1 (0ms fast path)**: unambiguous ad iframes (`doubleclick.net`, `googlesyndication.com`, `taboola.com`, ...) and standard CMP banners (`#onetrust-consent-sdk`, Cookiebot, Didomi, LGPD/GDPR dialogs).
- **Tier 2**: zero-shot AI classification via classifier.dev for everything the heuristic can't decide.

## What shipped

- Ad iframes, autoplay video players and cookie consent modals removed without network delay and without layout shift (CLS) — because tier 1 never waits on the network.

## Retrospective (draft)

- Splitting the problem into "free decisions" and "paid decisions" is what makes the extension feel instant; the classifier is the fallback, not the product.
"""

),
dict(slug="augdrive", title="augdrive", group="mobile-platform", language="Kotlin",
     date="2026-06-08", stars=0, status="active", tags=["android","mediapipe","audio","poc"],
     desc="AuditoryGuard — on-device road hazard detection that alerts the driver with distinct audio tones instead of visuals.",
     body="""## Hypothesis (draft)

A driving assistant that speaks only through **sound** could warn a driver without taking their eyes off the road.

## Stack & constraints

- **Android**, on-device **MediaPipe + EfficientDet** for object detection.
- **Rule-based** temporal and spatial risk analysis (no learned risk model).
- Alerts through `ToneGenerator` — deliberately non-visual.
- Explicitly a **proof of concept**: the README states it does not replace safe driving practices.

## What shipped

- Detects **person**, **car** and **red traffic light**.
- Three scenarios, each with its own tone: pedestrian in path (high-pitch emergency ringback), vehicle closing (medium-pitch alert call guard), red light ahead (low-pitch autoredial lite).
- Runs in the background and alerts the driver as hazards appear.

## Retrospective (draft)

- Encoding urgency as pitch rather than as another screen element is the design decision worth keeping; everything else in this POC is replaceable.
"""

),
dict(slug="clj-tasks", title="clj-tasks", group="systems-wasm", language="Clojure",
     date="2026-04-30", stars=0, status="learning", tags=["clojure","ring","reitit","sqlite"],
     desc="Simple CRUD in Clojure. Server-rendered task list built on Ring, Reitit, Hiccup and SQLite — a learning project about functional patterns.",
     body="""## Hypothesis (draft)

What does server-rendered CRUD look like with no ORM and no JS framework — just Ring, Reitit, Hiccup and SQLite?

## Stack & constraints

- **Clojure** via the `clj` CLI; **Ring** (server), **Reitit** (routing), **Hiccup** (HTML), **SQLite** (storage).
- Schema created by an explicit migration step (`app.db/migrate!`), then `clj -M:run` on `http://localhost:3000`.

## What shipped

- Full CRUD surface: `GET /`, `GET /tasks`, `GET /tasks/new`, `POST /tasks`, `GET /tasks/:id`, `GET /tasks/:id/edit`, `POST /tasks/:id`, `POST /tasks/:id/delete`.

## Retrospective (draft)

- Marked as *learning*: the value here is the data flow (request → route → handler → Hiccup → SQLite), not the feature set.
"""

),
dict(slug="feliperezende-github-io", title="feliperezende.github.io", group="foundational", language="Ruby",
     date="2026-03-16", stars=0, status="active", tags=["jekyll","blog","ruby"],
     desc="Personal blog built with Jekyll. Technical posts, reading notes and occasional thoughts.",
     body="""## Hypothesis (draft)

Writing has to live somewhere I control, in a format I can still build in ten years — static files and a `git push`.

## Stack & constraints

- **Jekyll** (Ruby), published to GitHub Pages at `feliperezende.github.io`.

## What shipped

- Technical posts, reading notes, and the occasional personal piece.

## Retrospective (draft)

- Superseded by this site for labs-style entries: the blog carries long-form writing, `labs.resenha.org` carries experiments.
"""

),
dict(slug="brewtools", title="brewtools", group="web-infra", language="JavaScript",
     date="2023-05-12", stars=3, status="active", tags=["react-native","brew","tools"],
     desc="Tools for home brewing: ABV calculator, bottle calculator, hydrometer temperature correction and unit converter. React Native, runs on iOS, Android and web.",
     body="""## Hypothesis (draft)

Brew-day arithmetic (ABV, priming, hydrometer correction) belongs in a phone app, not in a spreadsheet you have to trust blindly.

## Stack & constraints

- **React Native + React**, so one codebase covers iOS, Android and web.
- Last active in 2023 — the calculators work, nothing here chases platform churn.

## What shipped

- ABV calculator.
- Bottle calculator.
- Hydrometer temperature correction.
- Unit converter.

## Retrospective (draft)

- Still the most-starred thing here (3★), which says more about homebrewers finding tools than about the tooling.
"""

),
dict(slug="python-cookbook", title="python-cookbook", group="foundational", language="Python",
     date="2021-07-01", stars=0, status="archived", tags=["python","snippets"],
     desc="Simple Python recipes. Patterns, snippets and utilities collected over years of Python work. Archived.",
     body="""## Hypothesis (draft)

Snippets you actually reuse deserve a repo, not a notes app.

## Stack & constraints

- Plain **Python** scripts, no packaging, no tests. Archived since 2021.

## What shipped

- A collection of recipes, patterns and small utilities from years of Python work.

## Retrospective (draft)

- Archived because the working style changed: snippets now live next to the projects that use them instead of in one shared drawer.
"""

),
]

for e in E:
    fm = f"""---
title: "{e['title']}"
slug: "{e['slug']}"
group: "{e['group']}"
language: "{e['language']}"
description: "{e['desc']}"
updatedAt: "{e['date']}T00:00:00.000Z"
stars: {e['stars']}
status: "{e['status']}"
private: false
github: "https://github.com/feliperezende/{e['slug'] == 'feliperezende-github-io' and 'feliperezende.github.io' or e['slug']}"
tags: [{', '.join('"%s"' % t for t in e['tags'])}]
---

{HEADER}# {e['title']}

{e['body'].strip()}
"""
    (OUT / f"{e['slug']}.md").write_text(fm, encoding="utf-8")
    print("wrote", e["slug"])