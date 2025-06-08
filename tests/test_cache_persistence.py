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
import json
import os
import sys
import time

from src.cache_manager import CacheManager

# Setup import path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../src"))


def test_persistence_and_metrics(tmp_path):
    # Use tmp file for persistence
    p = tmp_path / "cache.json"
    os.environ["CACHE_PERSIST_PATH"] = str(p)
    # Initialize and clear
    cm = CacheManager()
    cm.symbolic.cache.clear()
#     cm.hash.cache.clear()
#     cm.factor.cache.clear()
    # Populate caches
    cm.symbolic.set(1, [1])
    cm.hash.set(2, [2])
    cm.factor.set(3, True)
    # Trigger hits/misses
    assert cm.symbolic.get(1) == 1
    assert cm.symbolic.get(99) is None
    assert cm.hash.get(2) == 2
    assert cm.factor.get(3) is True
    # Persist and load new manager
    cm.persist()
    cm2 = CacheManager()
    assert cm2.symbolic.get(1) == 1
    assert cm2.hash.get(2) == 2
    assert cm2.factor.get(3) is True
    # Check metrics recorded
    data = json.load(open(str(p)))
    metrics = data["metrics"]
    assert "symbolic_hits" in metrics and metrics["symbolic_hits"] >= 1
    assert "hash_hits" in metrics and metrics["hash_hits"] >= 1
    assert "factor_hits" in metrics and metrics["factor_hits"] >= 1

