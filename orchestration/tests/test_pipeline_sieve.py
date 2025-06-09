import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.cache_manager import CacheManager
from primality_test.src.primality import is_prime


def test_sieve_and_primality():
    sieve_limit = 20
    is_prime_list = [is_prime(n) for n in range(2, sieve_limit + 1)]
    expected = [
        True,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        False,
        True,
        False,
        True,
        False,
        False,
        False,
        True,
        False,
        True,
        False,
    ]
    assert is_prime_list == expected


def test_cache_manager():
    cm = CacheManager()
    cm.symbolic.set("foo", 42)
    assert cm.symbolic.get("foo") == 42
    cm.hash.set(100, "bar")
    assert cm.hash.get(100) == "bar"
    cm.factor.set(17, True)
    assert cm.factor.get(17) is True
