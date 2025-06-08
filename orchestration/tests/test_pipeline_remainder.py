def fake_post(url, json):
    if '/filter' in url:
        return FakeResponse({'passed': json, 'filtered': []})
    if '/sieve' in url:
        passed = [c for c in json if int(c['value']) % 2 != 0]
        return FakeResponse({'passed': passed, 'filtered': [c for c in json if int(c['value']) % 2 == 0]})
    if '/remainder' in url:
        passed = [c for c in json if not (int(c['value']) % 3 == 0 and int(c['value']) != 3)]
        return FakeResponse({'passed': passed, 'filtered': [c for c in json if c not in passed]})
    if '/primality' in url:
        return FakeResponse({'passed': json, 'filtered': []})
    raise RuntimeError(f"Unexpected URL: {url}")

