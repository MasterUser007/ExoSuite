# GitHub Pages Deployment Guide for PrimeEngineAI

## 🚀 Step 1: Install MkDocs and Material Theme

```bash
pip install mkdocs mkdocs-material
```

## 🛠 Step 2: Preview Docs Locally

```bash
mkdocs serve
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

## 📦 Step 3: Build Static Site

```bash
mkdocs build
```

## 🌍 Step 4: Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

> Make sure your repo is connected to GitHub and `gh-pages` is an allowed branch.
