from sieve import sieve_batch


def test_sieve_simple():
    batch = [{"id": 1, "value": "14"}, {"id": 2, "value": "17"}]
    passed, filtered = sieve_batch(batch)
    assert passed == [{"id": 2, "value": "17"}]
    assert filtered == [{"id": 1, "value": "14"}]
