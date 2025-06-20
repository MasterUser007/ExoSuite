from fastapi import FastAPI
from typing import List, Dict
from primality import primality_batch

app = FastAPI(title="Primality Test")


@app.post("/primality")
def primality_endpoint(batch: List[Dict]):
    passed, filtered = primality_batch(batch)
    return {"passed": passed, "filtered": filtered}
