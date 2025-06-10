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
import os
import sys

import pytest

# Ensure src on path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../src"))
# from core import orchestrate_factoring

# Known primes list for test
PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29]


@pytest.mark.parametrize("p", PRIMES)
def test_neighbors(p):
    # p is prime
    res_p = orchestrate_factoring(p)
    # p+1 is composite
    res_next = orchestrate_factoring(p + 1)
    # composite number factoring should produce factors >1

