from typing import List, Dict, Tuple

# Apply an additional mod‑3 and mod‑7 filter:
SMALL_PRIMES = [3, 7]


def remainder_batch(candidates: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    passed, filtered = [], []
    for item in candidates:
        n = int(item["value"])
        # If divisible by 3 or 7 (and not equal), filter out
        if any(n % p == 0 and n != p for p in SMALL_PRIMES):
            filtered.append(item)
        else:
            passed.append(item)
    return passed, filtered
