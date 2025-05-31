import requests
from .config import SERVICE_URLS

def run_pipeline(batch):
    passed = batch
    filtered = []
    for stage in ["filter", "sieve", "remainder", "primality"]:
        try:
            resp = requests.post(f"{SERVICE_URLS[stage]}/{stage}", json=passed)
            data = resp.json()
        except Exception:
            break
        passed = data["passed"]
        filtered.extend(data.get("filtered", []))
    return {"passed": passed, "filtered": filtered}
