from typing import Dict, List

from fastapi import FastAPI
from sieve import sieve_batch

app = FastAPI(title="GPU Sieve")


@app.post("/sieve")
def sieve_endpoint(batch: List[Dict]):
    passed, filtered = sieve_batch(batch)
    return {"passed": passed, "filtered": filtered}
