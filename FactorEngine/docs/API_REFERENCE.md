# API Reference – PrimeEngineAI

## Modules

### `symbolic_cache.py`
- `apply_symbolic_filters(candidate: str) -> bool`  
  Returns True if candidate passes symbolic exclusion.

### `prime_pipeline.py`
- `run_pipeline()`  
  Orchestrates all stages: symbolic filter → GPU sieve → Remainder → Miller-Rabin.

### `miller_rabin.py`
- `is_probably_prime(n: int, k: int) -> bool`  
  Performs Miller–Rabin primality test with `k` rounds.

## REST API (Planned)
See `api/server.py` for future REST API scaffolding via FastAPI.
