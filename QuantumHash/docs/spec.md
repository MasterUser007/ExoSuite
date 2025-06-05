# Formal API Specification for QuantumHash

## Available APIs

- `compute_hash(data: bytes, strength: int) -> bytes`: Computes hash of data.

### Preconditions
- `data` is bytes; `strength` one of [256, 512, 1024].

### Postconditions
- Returns a byte string of length corresponding to strength.

---
## Updates
- **Black-Box API**: `main_factoring_engine` remains the sole entrypoint.
- **Symbolic Caching**: Tiered LRU cache (PrimeEngineAI) and lock-free cache (QuantumHash) abstracted in ExoSuite.
- **Formal Specifications**: Preconditions/postconditions for public API in spec.md.
