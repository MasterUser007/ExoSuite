from src.prime_pipeline import prime_discovery_pipeline

if __name__ == "__main__":
    start, end = 100000, 100100
    primes = prime_discovery_pipeline(start, end)
    print(f"Discovered primes: {primes}")
