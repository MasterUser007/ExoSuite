import requests

from orchestration.src.pipeline import run_pipeline


class FakeResponse:
    def __init__(self, data):
        self._data = data

    def raise_for_status(self):
        pass

    def json(self):
        return self._data


def test_filter_stage(monkeypatch):
    batch = [{"id": 1, "value": "10"}, {"id": 2, "value": "17"}]

    def fake_post(url, json):
        # Simulate dropping any even-ending numbers
        passed = [c for c in json if c["value"][-1] not in "024568"]
        return FakeResponse({"passed": passed, "filtered": []})

    monkeypatch.setattr(requests, "post", fake_post)

    result = run_pipeline(batch)
    assert any(r["id"] == 2 for r in result["passed"])
    assert all(r["id"] != 1 for r in result["passed"])
