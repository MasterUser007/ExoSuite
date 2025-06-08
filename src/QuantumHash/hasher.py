def neighbors(n):
    factors = []
    x = n
    f = 2
    while f * f <= x:
        while x % f == 0:
            factors.append(f)
            x //= f
        f += 1
    if x > 1:
        factors.append(x)
    return factors
