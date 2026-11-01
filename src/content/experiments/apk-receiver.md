---
title: "apk-receiver"
slug: "apk-receiver"
group: "mobile-platform"
language: "Kotlin"
description: "Send APK download URLs from an iPhone to an Android TV box over the local network. Local-first, no cloud, no Play Services."
updatedAt: "2026-10-10T00:00:00.000Z"
stars: 0
status: "active"
private: false
github: "https://github.com/feliperezende/apk-receiver"
tags: ["android", "kotlin", "lan", "apk"]
---

<!-- DRAFT: 'hypothesis' and 'retrospective' sections were drafted by Hermes from repo
     evidence (README, metadata) and are marked (draft). Rewrite them in your own voice. -->

# apk-receiver

## Hypothesis (draft)

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
