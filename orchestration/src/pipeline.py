from typing import Dict, List
import requests

SERVICE_URLS = {
    "primeengineai": "http://primeengineai:8000",
    "gpu_sieve": "http://gpu_sieve:8000",
    "remainder_analysis": "http://remainder_analysis:8000",
    "primality_test": "http://primality_test:8000",
    "pavi": "http://pavi:8080",
}


def run_pipeline(batch: List[Dict]):
    filtered = []

    # Stage 1: Symbolic Filter
    r1 = requests.post(f"{SERVICE_URLS['primeengineai']}/filter", json=batch)
    r1.raise_for_status()
    d1 = r1.json()
    passed, filtered_stage = d1["passed"], d1["filtered"]
    filtered.extend(filtered_stage)

    # Stage 2: GPU Sieve
    r2 = requests.post(f"{SERVICE_URLS['gpu_sieve']}/sieve", json=passed)
    r2.raise_for_status()
    d2 = r2.json()
    p2, f2 = d2["passed"], d2["filtered"]
    filtered.extend(f2)
    batch2 = p2

    # Stage 3: Remainder Analysis
    r3 = requests.post(f"{SERVICE_URLS['remainder_analysis']}/remainder", json=batch2)
    r3.raise_for_status()
    d3 = r3.json()
    p3, f3 = d3["passed"], d3["filtered"]
    filtered.extend(f3)
    batch3 = p3

    # Stage 4: Primality Test
    r4 = requests.post(f"{SERVICE_URLS['primality_test']}/primality", json=batch3)
    r4.raise_for_status()
    d4 = r4.json()
    p4, f4 = d4["passed"], d4["filtered"]
    filtered.extend(f4)
    final_passed = p4

    return {"passed": final_passed, "filtered": filtered}
