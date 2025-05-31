import requests

from orchestration.src.pipeline import run_pipeline


class FakeResponse:
    def __init__(self, data):
        self._data = data

    def raise_for_status(self):
        pass

    def json(self):
        return self._data


def test_filter_and_sieve(monkeypatch):
    batch = [{"id": 1, "value": "14"}, {"id": 2, "value": "17"}]

    def fake_post(url, json):
        if "/filter" in url:
            # filter stage passes both through
            return FakeResponse({"passed": json, "filtered": []})
        if "/sieve" in url:
            # sieve stage drops even multiples
            passed = [c for c in json if int(c["value"]) % 2 != 0]
            return FakeResponse(
                {
                    "passed": passed,
                    "filtered": [c for c in json if int(c["value"]) % 2 == 0],
                }
            )
        raise RuntimeError(f"Unexpected URL: {url}")

    monkeypatch.setattr(requests, "post", fake_post)

    result = run_pipeline(batch)
    # Only ID=2 (value 17) should remain passed
    assert result["passed"] == [{"id": 2, "value": "17"}]
    assert result["filtered"] == [{"id": 1, "value": "14"}]
