![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)

# FactorEngine

**FactorEngine** is a modular, high-performance prime number discovery engine featuring:

- 🚀 Symbolic filtering & rule-based truncation
- ⚡ GPU-accelerated sieving
- 🧮 GMP-backed Miller-Rabin primality testing
- 🤖 ML/RL integration for symbolic learning & candidate prioritization
- ☁️ Full cloud deployment support with Docker & Terraform
- 📊 Prometheus hooks for performance tracing
- 🧪 Full validation plan & benchmarking suite

## 🔧 Getting Started

```bash
# Clone & install dependencies
git clone https://github.com/yourorg/FactorEngine.git
cd FactorEngine
pip install -r requirements.txt

# Run the discovery pipeline
python main.py
```

## 📂 Repo Structure

| Folder | Purpose |
|--------|---------|
| `src/` | Core symbolic filtering, pipeline, primality checks |
| `scripts/` | Pipeline launcher & helpers |
| `tests/` | Unit & integration tests |
| `ml_hooks/` | ML training data, inference, retraining |
| `deployment/` | Docker, AWS Terraform deployment |
| `docs/` | Full modular documentation |
| `notebooks/` | Example pipeline walkthroughs |

## 📄 Documentation

See [`docs/`](./docs/) or the master documentation in `FactorEngine_Full_Documentation.docx`.

## 📜 License & Attribution

© Lee Bond, All Rights Reserved. Patent Pending. Unauthorized use or redistribution prohibited.

## ✅ Test & Coverage Instructions

Install dependencies:
```bash
pip install -r requirements.txt
```

Run tests:
```bash
make test
```

Generate terminal coverage report:
```bash
make coverage
```

Generate HTML coverage report:
```bash
make coverage-html
open htmlcov/index.html  # or manually browse to view
```