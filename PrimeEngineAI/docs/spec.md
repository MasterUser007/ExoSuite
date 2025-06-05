# Formal API Specification for PrimeEngineAI

## Available APIs

- `main_factoring_engine(input_number: int) -> List[int]`: Factorizes input into prime factors.

### Preconditions
- `input_number` must be a non-negative integer.

### Postconditions
- Returns a list of integers whose product equals `input_number`.

---
## Updates
- **Black-Box API**: `main_factoring_engine` remains the sole entrypoint.
- **Symbolic Caching**: Tiered LRU cache (PrimeEngineAI) and lock-free cache (QuantumHash) abstracted in ExoSuite.
- **Formal Specifications**: Preconditions/postconditions for public API in spec.md.
