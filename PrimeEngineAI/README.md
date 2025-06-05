# 🚀 FactorEngine

![Build Status](https://img.shields.io/github/workflow/status/your-org/factorengine/CI)
![License](https://img.shields.io/github/license/your-org/factorengine)
![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

FactorEngine is a high-performance, symbolic-accelerated number factoring engine with modular design, GPU sieving, and infinitesimal remainder pruning. Built to integrate directly with PrimeEngineAI and QuantumHash via the ExoSuite orchestration layer.

---

## 🔧 Features

| Feature | Description |
|--------|-------------|
| 🧠 Symbolic Factoring | Uses exclusion rules to bypass composite patterns |
| ⚙️ Modular Filters | Layered exclusion and reduction logic |
| ⚡ GPU-Accelerated | Leverages CUDA kernels for batch sieving |
| 🔁 Tiered Cache | Efficient storage of rejected candidates |
| 📉 Infinitesimal Analysis | Lightweight scoring of near-zero remainders |
| 🔍 Miller-Rabin GPU Tests | Probabilistic primality test at scale |
| 🔒 Closed Gap Filters | Removes already-verified prime gaps |
| 🧪 Full Test Suite | Includes ExoSuite black-box automation |

---

## 🚀 Quickstart

```bash
# Install dependencies
pip install -r requirements.txt

# Run the engine on a demo number
python examples/demo_run.py
```

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 🔄 Environment Configuration

Copy `.env.example` to `.env` and modify as needed:

```bash
cp configs/.env.example .env
```

---

## 🧱 Folder Structure

```
factoring_engine/
├── engine_core.py
├── symbolic_factoring.py
├── gpu_miller_rabin.py
├── ...
├── tests/
├── docs/
├── examples/
├── configs/
├── Glossary.md
├── Dockerfile
├── .github/
```

---

## 📚 Documentation

Documentation is available under the `docs/` folder or can be auto-published with MkDocs.

---

## 🔗 Part of ExoSuite

This tool works standalone or as part of the full ExoSuite symbolic math engine.

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