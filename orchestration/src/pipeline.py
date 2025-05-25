import requests
from typing import List, Dict

SERVICE_URLS = {
    'primeengineai': 'http://primeengineai:8000',
    'gpu_sieve':      'http://gpu_sieve:8000',
    'remainder_analysis': 'http://remainder_analysis:8000',
    'primality_test': 'http://primality_test:8000',
    'pavi':           'http://pavi:8080',
}

def run_pipeline(batch: List[Dict]):
    # Stage 1: Symbolic Filter
    resp1 = requests.post(f\"{SERVICE_URLS['primeengineai']}/filter\", json=batch)
    resp1.raise_for_status()
    data1 = resp1.json()
    passed, filtered = data1['passed'], data1['filtered']

    # Stage 2: GPU Sieve
    resp2 = requests.post(f\"{SERVICE_URLS['gpu_sieve']}/sieve\", json=passed)
    resp2.raise_for_status()
    data2 = resp2.json()
    passed_after_sieve, filtered2 = data2['passed'], data2['filtered']

    # Combine filtered lists
    filtered.extend(filtered2)
    final_batch = passed_after_sieve

    # (Subsequent stages would follow...)

    return {
        'passed': final_batch,
        'filtered': filtered
    }
