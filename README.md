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

Base exclusions are `.git*` at the root plus `*/.git/` and `*/.github/` at any
depth. Each fixture below is a witness for exactly one rule, so a wrong outcome
points at a single cause. The Hub file list should be exactly the five `UPLOAD`
rows, plus the Hub's own `.gitattributes`, which `huggingface_hub` refuses to
delete.

| File | Expected | Witness for |
|---|---|---|
| `README.md` | UPLOAD | include `*.md` |
| `app.py` | UPLOAD | include `*.py` |
| `requirements.txt` | UPLOAD | include `*.txt` |
| `keep/keepme.txt` | UPLOAD | include `*.txt` matching below the root |
| `docs/.gitnotes.md` | UPLOAD | a nested `.git`-prefixed **file** is content, not metadata, so it must survive |
| `.gitnotes.md` | skip | base `.git*` at the root, despite include `*.md` |
| `sub/.github/notes.md` | skip | base `*/.github/`, despite include `*.md` |
| `sub/.github/workflows/noop.yml` | skip | base `*/.github/` |
| `.gitignore` | skip | base `.git*` |
| `.github/workflows/sync-hf-space.yml` | skip | base `.git*` |
| `notes/scratch.md` | skip | user exclude `notes/` (trailing slash) |
| `notes/todo.md` | skip | user exclude `notes/` |
| `assets/top.txt` | skip | user exclude `assets/*` |
| `assets/nested/deep.txt` | skip | user exclude `assets/*` crossing a `/` |
| `tmpfiles/artifact.tmp` | skip | no include pattern matches it |
| `docs/.gitkeep` | skip | no include pattern matches it |
| `docs/.gitattributes` | skip | no include pattern matches it |

`docs/.gitnotes.md` is the regression guard: it would be filtered out by a base
pattern of `*/.git*`, and must stay on the Hub under `*/.git/` + `*/.github/`.

The `*/.git/` pattern has no fixture here. Git silently refuses to stage any
path containing a `.git` component, so that rule only fires on a real submodule
checked out by `actions/checkout` with `submodules: true`.
