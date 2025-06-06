from typing import Dict, List, Tuple

# A simple sieve removing multiples of small primes [2,3,5,7,11]
SMALL_PRIMES = [2, 3, 5, 7, 11]


def sieve_batch(candidates: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    passed, filtered = [], []
    for item in candidates:
        n = int(item["value"])
        if any(n % p == 0 and n != p for p in SMALL_PRIMES):
            filtered.append(item)
        else:
            passed.append(item)
    return passed, filtered
