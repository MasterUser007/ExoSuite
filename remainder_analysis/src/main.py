<<<<<<< HEAD
﻿from fastapi import FastAPI
from typing import List, Dict
from remainder import remainder_batch

app = FastAPI(title="Remainder Analysis")


@app.post("/remainder")
def remainder_endpoint(batch: List[Dict]):
    passed, filtered = remainder_batch(batch)
    return {"passed": passed, "filtered": filtered}
=======
def remainder_analysis_main():
    print("Remainder analysis")


if __name__ == "__main__":
    remainder_analysis_main()
>>>>>>> 68f649f10b9a89a6adbe875b4fef357adef21fe4
