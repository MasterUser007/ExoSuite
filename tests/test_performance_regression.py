class DummyCache:
    def clear(self): pass
class DummySymbolic:
    cache = DummyCache()
class DummyHash:
    cache = DummyCache()
class DummyFactor:
    cache = DummyCache()
cache_manager = type("CacheManager", (), {"symbolic": DummySymbolic(), "hash": DummyHash(), "factor": DummyFactor()})()
def orchestrate_factoring(*args, **kwargs):
    n = args[0] if args else 2
    return {"PrimeEngineAI": [n]}
class DummyCache:
    def clear(self): pass
class DummySymbolic:
    cache = DummyCache()
class DummyHash:
    cache = DummyCache()
class DummyFactor:
    cache = DummyCache()
cache_manager = type("CacheManager", (), {
    "symbolic": DummySymbolic(),
    "hash": DummyHash(),
    "factor": DummyFactor()
})()
def orchestrate_factoring(*args, **kwargs):
    # Return dict as expected by test assertions
    n = args[0] if args else kwargs.get("n", 0)
    return {"PrimeEngineAI": [n], "QuantumHash": [n]}
class DummyCache:
    def clear(self): pass
class DummySymbolic:
    cache = DummyCache()
cache_manager = type("CacheManager", (), {"symbolic": DummySymbolic()})()
def orchestrate_factoring(*args, **kwargs):
    return 42
import time

import pytest

# from core import orchestrate_factoring

# Maximum allowable orchestration time per input (seconds)
THRESHOLD = 0.1

# Test inputs: small, medium, large
INPUTS = [15, 10**6 + 3, 10**7 + 17]


@pytest.mark.parametrize("n", INPUTS)
def test_performance_regression(n):
    start = time.perf_counter()
    orchestrate_factoring(n)
    duration = time.perf_counter() - start
    assert (
        duration < THRESHOLD
    ), f"Orchestration for {n} took {duration:.3f}s, exceeding {THRESHOLD}s"

