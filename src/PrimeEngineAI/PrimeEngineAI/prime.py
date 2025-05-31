def pef(input_number):
    n = input_number
    factors = []
    f = 2
    while f * f <= n:
        while n % f == 0:
            factors.append(f)
            n //= f
        f += 1
    if n > 1:
        factors.append(n)
    return factors
