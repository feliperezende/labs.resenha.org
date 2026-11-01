---
title: "futmanager-wasm"
slug: "futmanager-wasm"
group: "systems-wasm"
language: "Rust"
description: "Browser football manager (FutManager 98) with the match engine written in Rust and compiled to WebAssembly, behind a retro Windows 98 interface."
updatedAt: "2026-10-13T00:00:00.000Z"
stars: 0
status: "active"
private: false
github: "https://github.com/feliperezende/futmanager-wasm"
tags: ["wasm", "simulation", "rust", "retro"]
---

<!-- DRAFT: 'hypothesis' and 'retrospective' sections were drafted by Hermes from repo
     evidence (README, metadata) and are marked (draft). Rewrite them in your own voice. -->

# futmanager-wasm

## Hypothesis (draft)

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
