import requests
from orchestration.src.pipeline import run_pipeline

class FakeResponse:
    def __init__(self, data): self._data = data
    def raise_for_status(self): pass
    def json(self): return self._data

def test_full_pipeline_primality(monkeypatch):
    batch = [
        {'id':1,'value':'30'},  # filter/sieve/remainder drop
        {'id':2,'value':'25'},  # passes 1–3, composite -> filtered stage 4
        {'id':3,'value':'13'}   # passes all stages
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
        if '/primality' in url:
            passed = [c for c in json if int(c['value']) in (2,3,5,7,11,13)]
            return FakeResponse({'passed': passed, 'filtered': [c for c in json if c not in passed]})
        raise RuntimeError(f\"Unexpected URL: {url}\")

    monkeypatch.setattr(requests, 'post', fake_post)

    result = run_pipeline(batch)
    assert result['passed'] == [{'id':3,'value':'13'}]
    assert any(f['id']==1 for f in result['filtered'])
    assert any(f['id']==2 for f in result['filtered'])

