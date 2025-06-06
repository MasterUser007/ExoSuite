name: Full Wash

on:
  pull_request:
  push:
    branches:
      - "release/**"
      - "dev/**"

jobs:
  wash:
    runs-on: windows-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: 3.11

      - name: Install Black
        run: pip install black

      - name: Run Full Wash Script
        shell: pwsh
        run: |
          Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
          ./scripts/full_wash.ps1
