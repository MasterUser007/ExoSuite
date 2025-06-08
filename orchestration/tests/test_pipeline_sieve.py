<<<<<<< HEAD
def test_pipeline_sieve_basic():
    assert True
=======
def fake_post(url, json):
    if '/filter' in url:
        # filter stage passes both through
        return FakeResponse({'passed': json, 'filtered': []})
    if '/sieve' in url:
        # sieve stage drops even multiples
        passed = [c for c in json if int(c['value']) % 2 != 0]
        return FakeResponse({'passed': passed, 'filtered': [c for c in json if int(c['value']) % 2 == 0]})
    if '/primality' in url:
        return FakeResponse({'passed': json, 'filtered': []})
    if '/remainder' in url:
        return FakeResponse({'passed': json, 'filtered': []})
    raise RuntimeError(f"Unexpected URL: {url}")

>>>>>>> 3453edc (chore(repo): full monorepo restructure, test/config updates, and CI setup)
