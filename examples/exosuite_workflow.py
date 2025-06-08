<<<<<<< HEAD
def run_workflow():
    print("ExoSuite workflow")


if __name__ == "__main__":
    run_workflow()
=======
# Example: Prime -> Factor -> Hash Pipeline

This example demonstrates how ExoSuite engines interact in sequence.

```python
from PrimeEngineAI.engine_core import main_factoring_engine as discover_prime
from FactorEngine.engine_core import main_factoring_engine as factor_number
from QuantumHash.engine_core import main_factoring_engine as quantum_hash_transform

# Step 1: Discover a prime number (simulate)
candidate = 1299827  # Substitute with output of discover_prime() if available

# Step 2: Factor (should be prime, so returns [candidate])
factors = factor_number(candidate)
print("Factors:", factors)

# Step 3: Transform via QuantumHash
hash_output = quantum_hash_transform(candidate)
print("QuantumHash Result:", hash_output)
```
>>>>>>> 3453edc (chore(repo): full monorepo restructure, test/config updates, and CI setup)
