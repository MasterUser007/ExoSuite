def main_factoring_engine(input_number: int):
    """Trial-division factoring stub for FactorEngine tests."""
    n = input_number
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        factors.append(n)
    return factors
