# B. Fast Divisibility & Modulo Filters

The analysis layer applies a sequence of modulo checks (e.g., n mod p where p is a small prime) to evaluate remainder patterns. Candidates that return zero remainders for any known small primes are immediately discarded. Others with highly suspicious residue signatures (e.g., non-uniform modulo distributions or patterns known to occur in composites) are deprioritized.

