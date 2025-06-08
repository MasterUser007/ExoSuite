# CLI Automation Routines

This page catalogs handy shell aliases and one‑liners for our ExoSuite docs workflow.

## Environment & Virtualenv
```bash
alias mkvenv='rm -rf .venv && python3 -m venv .venv && source .venv/bin/activate && pip install --upgrade pip mkdocs mkdocs-material'
alias mkup='source .venv/bin/activate && pip install --upgrade mkdocs mkdocs-material && deactivate'

