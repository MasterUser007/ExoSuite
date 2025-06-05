
from .symbolic_cache import SymbolicCache
from .miller_rabin import is_probable_prime

def prime_discovery_pipeline(start, end):
    cache = SymbolicCache()
    primes = []

    for number in range(start, end):
        if number % 2 == 0 or number % 5 == 0:
            cache.add(number, "Trivial modulo exclusion")
            continue
        if not is_probable_prime(number):
            cache.add(number, "Failed Miller-Rabin")
            continue
        primes.append(number)

    return primes
