---
title: "kikis-sky-adventure"
slug: "kikis-sky-adventure"
group: "games"
language: "Luau"
description: "Arcade flying game for kids on Roblox, written entirely in code (Luau + Rojo, no Studio): procedural airport, 37 missions, economy, NPC world life. Published through the Open Cloud API."
updatedAt: "2026-11-06T23:20:32.000Z"
stars: 0
status: "active"
private: true
github: "https://github.com/feliperezende/kikis-sky-adventure"
demo: "https://www.roblox.com/games/128759582737786"
tags: ["roblox", "luau", "rojo", "gamedev", "lune"]
---

<!-- DRAFT: 'hypothesis' and 'retrospective' sections were drafted by Hermes from repo
     evidence (README, commit log) and are marked (draft). Rewrite them in your own voice. -->

# kikis-sky-adventure

## Hypothesis (draft)

What does a Roblox game look like when it is written **entirely in code** — Luau + Rojo, no Studio editing at all — and aimed at kids rather than at Roblox veterans?

## Stack & constraints

- **Luau + Rojo** (`default.project.json`): `src/shared` → ReplicatedStorage, `src/server` → ServerScriptService, `src/client` → StarterPlayerScripts.
- **Pure modules, tested outside Roblox**: `ArcadeFlight`, `Rings`, `AirportLayout`, `AircraftDesign`, `Economy`, `Missions` have no Roblox APIs and are unit-tested in **Lune**.
- Every tunable lives in `src/shared/Config.luau` (flight feel, controls, rings, camera, validation, map).
- **Publishing is a script, not a click**: `scripts/publish.sh` lints, tests, builds and uploads `flight-sim.rbxl` through the **Open Cloud Place Publishing API** (universe `10772740718`, place `128759582737786`), key passed via a private temp header file.
- Deliberately **arcade, not a simulator**: no stalls, no flaps, no throttle, nothing scary.

## What shipped

- Per-player high-wing plane parked on the apron of a **procedurally built airport**; walk up, get in, hold UP to take off, fly through golden rings, land anywhere.
- **37 adventure missions** — take off, rings, boost, land, fly to a place, delivery, balloons, boss races, passengers, timed deliveries, fire squad scoops and fires, photo safari, rescues — with progress detection and server-side checks.
- Economy: coins, rewards, shop catalog (planes, paints, smoke trails), places, saved profile.
- World life: NPCs (airport and hub crowds, field farmer and animals, island villagers, bird flocks, far sky traffic, boats), roads between towns, traffic (cars, bus, truck, ice-cream van, tractor, ferry), map life (windmills, smoke, kites, park, ducks, lighthouse beam).
- Vehicles: planes and helicopters with a heli flight mode, hangar badges; optional **Robux unlocks** (Developer Products, idempotent `ProcessReceipt` saved before grant — coins unchanged).
- Renamed from "Plane Avião" to **Kiki's Sky Adventure** in v30, keeping the old DataStore (`PlaneAviaoProgress_v1`) and web save keys (`planeAviao.*`) **on purpose** so nobody loses progress.
- Public on Roblox: narrated by Captain Kiki in English or Portuguese, 37 golden balloons (one per mission), animal passenger flights, Fire Squad, Photo Safari, mountain rescues.
- 44 commits so far, currently at v36.

## Retrospective (draft)

- Keeping the pure logic outside Roblox's API surface is what makes the test suite possible; the flip side is that the *feel* (turn rate, pitch/bank response, crash thresholds, touch joystick placement) can only be tuned in a real session.
- The rename is the interesting constraint: identity changed, but the storage keys deliberately did not — compatibility over tidiness.
- Known gaps: no engine sound or music yet (Kiki's voice is the only audio), control-surface animation visible only to the pilot, and server validation is basic (speed, altitude, NaN) — a determined exploiter could still teleport within the limits.