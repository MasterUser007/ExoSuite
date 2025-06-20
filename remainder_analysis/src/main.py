from fastapi import FastAPI
from typing import List, Dict
from remainder import remainder_batch

app = FastAPI(title="Remainder Analysis")


@app.post("/remainder")
def remainder_endpoint(batch: List[Dict]):
    passed, filtered = remainder_batch(batch)
    return {"passed": passed, "filtered": filtered}
