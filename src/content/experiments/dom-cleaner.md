---
title: "dom-cleaner"
slug: "dom-cleaner"
group: "web-infra"
language: "JavaScript"
description: "Chrome extension (Manifest V3) that removes ad iframes, autoplay players and cookie consent modals with a 0ms heuristic fast path plus zero-shot AI classification."
updatedAt: "2026-09-20T00:00:00.000Z"
stars: 0
status: "active"
private: false
github: "https://github.com/feliperezende/dom-cleaner"
tags: ["chrome-extension", "mv3", "ads", "ai"]
---

<!-- DRAFT: 'hypothesis' and 'retrospective' sections were drafted by Hermes from repo
     evidence (README, metadata) and are marked (draft). Rewrite them in your own voice. -->

# dom-cleaner

## Hypothesis (draft)

Most intrusive page junk is unambiguously identifiable from the DOM alone. A 0ms heuristic can clear that tier, and an AI classifier should only ever see the ambiguous remainder.

## Stack & constraints

- **Chrome extension, Manifest V3**.
- **Tier 1 (0ms fast path)**: unambiguous ad iframes (`doubleclick.net`, `googlesyndication.com`, `taboola.com`, ...) and standard CMP banners (`#onetrust-consent-sdk`, Cookiebot, Didomi, LGPD/GDPR dialogs).
- **Tier 2**: zero-shot AI classification via classifier.dev for everything the heuristic can't decide.

## What shipped

- Ad iframes, autoplay video players and cookie consent modals removed without network delay and without layout shift (CLS) — because tier 1 never waits on the network.

## Retrospective (draft)

- Splitting the problem into "free decisions" and "paid decisions" is what makes the extension feel instant; the classifier is the fallback, not the product.
