# Formal API Specification for FactorEngine

## Available APIs

- `is_probably_prime(n: int) -> bool`: Returns probabilistic primality result.

### Preconditions
- `n` must be a non-negative integer.

### Postconditions
- Returns `True` if `n` passes Miller-Rabin tests, else `False`.

---
## Updates
- **Black-Box API**: `is_probably_prime` remains the sole entrypoint.
- **Symbolic Caching**: Tiered LRU cache (PrimeEngineAI) and lock-free cache (QuantumHash) abstracted in ExoSuite.
- **Formal Specifications**: Preconditions/postconditions for public API in spec.md.
