import requests
from orchestration.src.pipeline import run_pipeline

class FakeResponse:
    def __init__(self, data): self._data = data
    def raise_for_status(self): pass
    def json(self): return self._data

def test_full_filter_sieve_remainder(monkeypatch):
    batch = [
        {'id':1,'value':'30'},  # filtered by mod2 in sieve
        {'id':2,'value':'25'},  # passes sieve, mod-3/7 check passes
        {'id':3,'value':'21'},  # sieve passes, remainder filters (21 % 3==0)
    ]

    def fake_post(url, json):
        if '/filter' in url:
            return FakeResponse({'passed': json, 'filtered': []})
        if '/sieve' in url:
            passed = [c for c in json if int(c['value']) % 2 != 0]
            return FakeResponse({'passed': passed, 'filtered': [c for c in json if int(c['value']) % 2 == 0]})
        if '/remainder' in url:
            passed = [c for c in json if not (int(c['value']) % 3 == 0 and int(c['value']) != 3)]
            return FakeResponse({'passed': passed, 'filtered': [c for c in json if c not in passed]})
        raise RuntimeError(f"Unexpected URL: {url}")

    monkeypatch.setattr(requests, 'post', fake_post)

    result = run_pipeline(batch)
    # Only id=2 (25) should survive all three stages
    assert result['passed'] == [{'id':2,'value':'25'}]
    assert any(f['id']==1 for f in result['filtered']) and any(f['id']==3 for f in result['filtered'])
