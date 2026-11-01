---
title: "augdrive"
slug: "augdrive"
group: "mobile-platform"
language: "Kotlin"
description: "AuditoryGuard — on-device road hazard detection that alerts the driver with distinct audio tones instead of visuals."
updatedAt: "2026-06-08T00:00:00.000Z"
stars: 0
status: "active"
private: false
github: "https://github.com/feliperezende/augdrive"
tags: ["android", "mediapipe", "audio", "poc"]
---

<!-- DRAFT: 'hypothesis' and 'retrospective' sections were drafted by Hermes from repo
     evidence (README, metadata) and are marked (draft). Rewrite them in your own voice. -->

# augdrive

## Hypothesis (draft)

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
