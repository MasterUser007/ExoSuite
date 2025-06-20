<<<<<<< HEAD
﻿from fastapi import FastAPI
from typing import List, Dict
from symbolic_filter import symbolic_filter

app = FastAPI(title="PrimeEngineAI")


@app.post("/filter")
def filter_endpoint(batch: List[Dict]):
    passed, filtered = symbolic_filter(batch)
    return {"passed": passed, "filtered": filtered}
=======
def main():
    print("PrimeEngineAI main")


if __name__ == "__main__":
    main()
>>>>>>> 68f649f10b9a89a6adbe875b4fef357adef21fe4
