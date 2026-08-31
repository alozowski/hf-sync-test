---
title: HF Sync Test
emoji: 🔄
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 6.5.1
app_file: app.py
pinned: false
---

# HF Sync Test

A simple test Space to verify GitHub → Hugging Face synchronization workflow.

## What it does

This Space contains a basic Gradio interface that greets users by name. It's used to test automated syncing from GitHub.

## Usage

Simply enter your name and receive a friendly greeting!

## Tech Stack

- **Framework**: Gradio
- **Sync**: Automated via GitHub Actions

## Pattern filtering test case

The sync workflow runs with these inputs:

```yaml
exclude: |
  notes/
  assets/*
include: |
  *.md
  *.py
  *.txt
```

Each fixture below is a witness for exactly one filtering rule, so a wrong
outcome points at a single cause. The Hub file list should be exactly the four
`UPLOAD` rows.

| File | Expected | Witness for |
|---|---|---|
| `README.md` | UPLOAD | include `*.md` |
| `app.py` | UPLOAD | include `*.py` |
| `requirements.txt` | UPLOAD | include `*.txt` |
| `keep/keepme.txt` | UPLOAD | include `*.txt` matching below the root |
| `.gitnotes.md` | skip | base `.git*`, despite include `*.md` |
| `docs/.gitnotes.md` | skip | base `*/.git*`, despite include `*.md` |
| `docs/.gitkeep` | skip | base `*/.git*` |
| `docs/.gitattributes` | skip | base `*/.git*` |
| `sub/.github/workflows/noop.yml` | skip | base `*/.git*` |
| `.gitignore` | skip | base `.git*` |
| `.github/workflows/sync-hf-space.yml` | skip | base `.git*` |
| `notes/scratch.md` | skip | user exclude `notes/` (trailing slash) |
| `notes/todo.md` | skip | user exclude `notes/` |
| `assets/top.txt` | skip | user exclude `assets/*` |
| `assets/nested/deep.txt` | skip | user exclude `assets/*` crossing a `/` |
| `tmpfiles/artifact.tmp` | skip | no include pattern matches it |
