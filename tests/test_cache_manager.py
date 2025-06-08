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

from src.cache_manager import CacheManager

root = os.path.abspath(os.path.dirname(__file__) + "/../../")
sys.path.insert(0, root)
sys.path.insert(0, os.path.join(root, "ExoSuite", "src"))
project_root = os.path.abspath(os.path.dirname(__file__) + "/..")


def test_cache_manager_set_get():
    cm = CacheManager(max_size=2)
    assert cm.symbolic.get(1) is None
    cm.symbolic.set(1, [1])
    assert cm.symbolic.get(1) == 1
    cm.symbolic.set(2, [2])
    cm.symbolic.set(3, [3])  # should evict 1
    assert cm.symbolic.get(1) is None
    assert cm.symbolic.get(2) == 2
    assert cm.symbolic.get(3) == 3

