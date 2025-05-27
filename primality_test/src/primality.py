from typing import List, Dict, Tuple
import random


def is_probable_prime(n: int, k: int = 5) -> bool:
    if n < 2:
        return False
    # small primes quick check
    for p in (2, 3, 5, 7, 11):
        if n == p:
            return True
        if n % p == 0:
            return False
    # write n-1 as d*2^r
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    # witness loop
    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def primality_batch(candidates: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    passed, filtered = [], []
    for item in candidates:
        n = int(item["value"])
        if is_probable_prime(n):
            passed.append(item)
        else:
            filtered.append(item)
    return passed, filtered
