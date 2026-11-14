---
title: "+1 Speed Rainbow Escape"
slug: "speed-rainbow-escape"
group: "games"
language: "Luau"
description: "All-ages Roblox speed-incremental escape game built without Studio (Luau + Rojo): procedural world, +1 speed per second, and level design checked by balance bots in a web simulator."
updatedAt: "2026-10-31T10:30:14.000Z"
stars: 0
status: "active"
private: true
github: "https://github.com/feliperezende/speed-rainbow-escape"
demo: "https://www.roblox.com/games/1601833037"
robloxUniverse: 619746601
tags: ["roblox", "luau", "rojo", "gamedev", "procedural", "playtesting"]
---

<!-- DRAFT: 'hypothesis' and 'retrospective' sections were drafted by Hermes from repo
     evidence (README, commit log) and are marked (draft). Rewrite them in your own voice. -->

# +1 Speed Rainbow Escape

## Hypothesis (draft)

What if level design for a speed-incremental runner could be **verified by bots** instead of by feel — a track exported to the browser, played by automated lanes, and adjusted from the numbers?

## Stack & constraints

- **Luau + Rojo**, again with **no Roblox Studio**: the world is procedurally generated from primitive parts at server start and the place is uploaded through the Open Cloud API.
- **Rating target: Minimal** — no violence, no blood, no horror, no gambling, no paid random items, no chat-centric features, no free-form drawing, no personal data collection. The constraint shapes the design more than the code.
- Toolchain pinned in `rokit.toml`: `stylua`, `selene`, `lune` — **72 tests** over the pure modules.
- **`web-sim/`**: the track and config are exported from Luau to a playable HTML simulator, the JS port is verified against the Luau original, and balance bots run the levels (`web-sim/bot-report.json`).
- Assets are all **CC0 1.0** (Kenney, Quaternius), catalogued in `assets-manifest.json` with pack, source URL, license and Roblox asset ID for every model.

## What shipped

- Core loop: run to gain **+1 Speed per second**; Speed is what makes the jumps — gaps get wider zone by zone and the track climbs.
- Hazards: walls, sliding blocks, lava, spinners. A fall or a hit sends you back to the start — **you keep your Speed**.
- Reach the golden finish for **Wins**, then **rebirth** for a multiplier.
- v11 introduced the speed-gated climbing track; the project is at **v48**, published live as place version 46.

## Retrospective (draft)

- The interesting habit here is the version discipline: every README update records which version is *live* (v47 → place version 45, v48 → 46) versus the one written but **not published** — the repo always says what players actually have.
- Bots found the level problems that screenshots alone wouldn't: roominess, clear lanes, one hazard per row, kill floors per level.
- Last touched 2026-10-31 — alive, but parked while the focus moved to the other Roblox games.