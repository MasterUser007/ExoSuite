from primality import is_probable_prime, primality_batch


def test_small_primes_and_composites():
    assert is_probable_prime(2)
    assert is_probable_prime(17)
    assert not is_probable_prime(15)
    # batch test
    batch = [{"id": 1, "value": "8"}, {"id": 2, "value": "13"}]
    passed, filtered = primality_batch(batch)
    assert passed == [{"id": 2, "value": "13"}]
    assert filtered == [{"id": 1, "value": "8"}]
