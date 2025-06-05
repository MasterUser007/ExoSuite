# ExoSuite Test Matrix Summary

| Engine         | Input | Symbolic Result | GPU Result | Final Verdict       |
|----------------|--------|------------------|-------------|---------------------|
| PrimeEngineAI  | 100    | Excluded (mod 2) | N/A         | Excluded            |
| PrimeEngineAI  | 7      | Passed           | Prime       | Probably Prime      |
| FactorEngine   | 100    | Excluded         | N/A         | Excluded            |
| FactorEngine   | 7      | Passed           | Prime       | Probably Prime      |
| QuantumHash    | 100    | Excluded         | N/A         | Excluded            |
| QuantumHash    | 7      | Passed           | Prime       | Probably Prime      |

Tests run through `main_factoring_engine` → symbolic → GPU → output.