def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def test_sieve_and_primality():
    sieve_limit = 20
    is_prime_list = [is_prime(n) for n in range(2, sieve_limit + 1)]
    expected = [True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False]
    assert is_prime_list == expected
