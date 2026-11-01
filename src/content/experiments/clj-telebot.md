---
title: "clj-telebot"
slug: "clj-telebot"
group: "systems-wasm"
language: "Clojure"
description: "Small Clojure Telegram bot client using the Telegram HTTP API (long polling). Minimal, functional, composable."
updatedAt: "2026-09-28T00:00:00.000Z"
stars: 1
status: "active"
private: false
github: "https://github.com/feliperezende/clj-telebot"
tags: ["clojure", "telegram", "bot", "yt-dlp"]
---

<!-- DRAFT: 'hypothesis' and 'retrospective' sections were drafted by Hermes from repo
     evidence (README, metadata) and are marked (draft). Rewrite them in your own voice. -->

# clj-telebot

## Hypothesis (draft)

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
