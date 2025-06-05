#!/bin/bash
echo "Running PrimeEngineAI Validation Suite..."
pytest tests/
python benchmarks/performance_tests.py
echo "Validation complete."
