from FactorEngine.src.miller_rabin import is_probably_prime


def test_small_prime():
    assert is_probably_prime(17, 5)


def test_small_composite():
    assert not is_probably_prime(15, 5)
