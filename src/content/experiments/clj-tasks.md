---
title: "clj-tasks"
slug: "clj-tasks"
group: "systems-wasm"
language: "Clojure"
description: "Simple CRUD in Clojure. Server-rendered task list built on Ring, Reitit, Hiccup and SQLite — a learning project about functional patterns."
updatedAt: "2026-04-30T00:00:00.000Z"
stars: 0
status: "learning"
private: false
github: "https://github.com/feliperezende/clj-tasks"
tags: ["clojure", "ring", "reitit", "sqlite"]
---

<!-- DRAFT: 'hypothesis' and 'retrospective' sections were drafted by Hermes from repo
     evidence (README, metadata) and are marked (draft). Rewrite them in your own voice. -->

# clj-tasks

## Hypothesis (draft)

What does server-rendered CRUD look like with no ORM and no JS framework — just Ring, Reitit, Hiccup and SQLite?

## Stack & constraints

- **Clojure** via the `clj` CLI; **Ring** (server), **Reitit** (routing), **Hiccup** (HTML), **SQLite** (storage).
- Schema created by an explicit migration step (`app.db/migrate!`), then `clj -M:run` on `http://localhost:3000`.

## What shipped

- Full CRUD surface: `GET /`, `GET /tasks`, `GET /tasks/new`, `POST /tasks`, `GET /tasks/:id`, `GET /tasks/:id/edit`, `POST /tasks/:id`, `POST /tasks/:id/delete`.

## Retrospective (draft)

- Marked as *learning*: the value here is the data flow (request → route → handler → Hiccup → SQLite), not the feature set.
