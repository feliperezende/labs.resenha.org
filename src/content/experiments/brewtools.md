---
title: "brewtools"
slug: "brewtools"
group: "web-infra"
language: "JavaScript"
description: "Tools for home brewing: ABV calculator, bottle calculator, hydrometer temperature correction and unit converter. React Native, runs on iOS, Android and web."
updatedAt: "2023-05-12T00:00:00.000Z"
stars: 3
status: "active"
private: false
github: "https://github.com/feliperezende/brewtools"
tags: ["react-native", "brew", "tools"]
---

<!-- DRAFT: 'hypothesis' and 'retrospective' sections were drafted by Hermes from repo
     evidence (README, metadata) and are marked (draft). Rewrite them in your own voice. -->

# brewtools

## Hypothesis (draft)

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
