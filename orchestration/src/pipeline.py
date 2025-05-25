import requests
from typing import List, Dict

SERVICE_URLS = {
    'primeengineai': 'http://primeengineai:8000',
    'gpu_sieve': 'http://gpu_sieve:8000',
    'remainder_analysis': 'http://remainder_analysis:8000',
    'primality_test': 'http://primality_test:8000',
    'pavi': 'http://pavi:8080',
}

def run_pipeline(batch: List[Dict]):
    # Stage 1: Symbolic Filter via PrimeEngineAI
    resp = requests.post(
        f\"{SERVICE_URLS['primeengineai']}/filter\",
        json=batch
    )
    resp.raise_for_status()
    data = resp.json()
    passed, filtered = data['passed'], data['filtered']

    # (Subsequent stages go here…)

    return data
