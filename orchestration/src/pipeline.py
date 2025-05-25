import requests
from typing import List, Dict

SERVICE_URLS = {
    'primeengineai':       'http://primeengineai:8000',
    'gpu_sieve':           'http://gpu_sieve:8000',
    'remainder_analysis':  'http://remainder_analysis:8000',
    'primality_test':      'http://primality_test:8000',
    'pavi':                'http://pavi:8080',
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
    filtered.extend(filtered2)
    batch2 = passed_after_sieve

    # Stage 3: Remainder Analysis
    resp3 = requests.post(f\"{SERVICE_URLS['remainder_analysis']}/remainder\", json=batch2)
    resp3.raise_for_status()
    data3 = resp3.json()
    passed_after_rem, filtered3 = data3['passed'], data3['filtered']
    filtered.extend(filtered3)
    final_passed = passed_after_rem

    return {
        'passed': final_passed,
        'filtered': filtered
    }
