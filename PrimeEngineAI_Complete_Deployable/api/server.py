
from fastapi import FastAPI
from src.prime_pipeline import prime_discovery_pipeline

app = FastAPI()

@app.get("/discover/")
def discover_primes(start: int, end: int):
    primes = prime_discovery_pipeline(start, end)
    return {"primes": primes}
