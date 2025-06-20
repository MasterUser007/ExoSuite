<<<<<<< HEAD
﻿from fastapi import FastAPI
from typing import List, Dict
from primality import primality_batch

app = FastAPI(title="Primality Test")


@app.post("/primality")
def primality_endpoint(batch: List[Dict]):
    passed, filtered = primality_batch(batch)
    return {"passed": passed, "filtered": filtered}
=======
def primality_main():
    print("Primality test")


if __name__ == "__main__":
    primality_main()
>>>>>>> 68f649f10b9a89a6adbe875b4fef357adef21fe4
