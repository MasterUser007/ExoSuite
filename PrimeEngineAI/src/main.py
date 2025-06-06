from typing import Dict, List

from fastapi import FastAPI
from symbolic_filter import symbolic_filter

app = FastAPI(title="PrimeEngineAI")


@app.post("/filter")
def filter_endpoint(batch: List[Dict]):
    passed, filtered = symbolic_filter(batch)
    return {"passed": passed, "filtered": filtered}
