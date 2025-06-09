from src.cache_manager import CacheManager
from primality_test.src.primality import is_prime

class ExoSuiteCore:
    def __init__(self):
        self.cache = CacheManager()
    def test_and_cache(self, n):
        cached = self.cache.symbolic.get(n)
        if cached is not None:
            return cached
        result = is_prime(n)
        self.cache.symbolic.set(n, result)
        return result

def main():
    engine = ExoSuiteCore()
    nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = [engine.test_and_cache(n) for n in nums]
    print(list(zip(nums, results)))

if __name__ == "__main__":
    main()
