#!/usr/bin/env node
// Scaffold a new experiment entry: npm run new:entry -- <slug> "<title>"
import { mkdirSync, writeFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const [, , slugArg, titleArg] = process.argv;

if (!slugArg) {
  console.error('usage: npm run new:entry -- <slug> "<title>"\n       npm run new:entry -- my-project "my project"');
  process.exit(1);
}

const slug = slugArg
  .toLowerCase()
  .replace(/\.github\.io$/, '-github-io')
  .replace(/[^a-z0-9]+/g, '-')
  .replace(/^-|-$/g, '');

const dir = join(root, 'src', 'content', 'experiments');
mkdirSync(dir, { recursive: true });
const file = join(dir, `${slug}.md`);

if (existsSync(file)) {
  console.error(`${slug}.md already exists`);
  process.exit(1);
}

const today = new Date().toISOString().slice(0, 10);

writeFileSync(
  file,
  `---
title: "${titleArg ?? slug}"
slug: "${slug}"
group: "systems-wasm"        # systems-wasm | mobile-platform | web-infra | foundational
language: ""                 # rust | kotlin | clojure | javascript | python | ruby | html
description: ""              # one line, no marketing
updatedAt: "${today}T00:00:00.000Z"
stars: 0
status: "active"             # active | archived | learning
private: false
github: "https://github.com/feliperezende/${slugArg}"
tags: []
---

<!-- Write the prose by hand, in your own voice. Sections published from this file
     render in order: Hypothesis → Stack & constraints → What shipped → Retrospective. -->

# ${titleArg ?? slug}

## Hypothesis

What question drove this? One paragraph.

## Stack & constraints

- Language / platform:
- Self-imposed limits:

## What shipped

- ...

## Retrospective

- what worked
- what surprised me
- what I'd do differently
`,
  'utf8',
);

console.log(`created src/content/experiments/${slug}.md`);
console.log('reminder: unset entries fail the build — description and language are required.');