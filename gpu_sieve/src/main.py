<<<<<<< HEAD
﻿from fastapi import FastAPI
from typing import List, Dict
from sieve import sieve_batch

app = FastAPI(title="GPU Sieve")


@app.post("/sieve")
def sieve_endpoint(batch: List[Dict]):
    passed, filtered = sieve_batch(batch)
    return {"passed": passed, "filtered": filtered}
=======
def gpu_sieve_main():
    print("GPU sieve main")


if __name__ == "__main__":
    gpu_sieve_main()
>>>>>>> 68f649f10b9a89a6adbe875b4fef357adef21fe4
