# A. GMP Library for High-Precision Arithmetic

The Miller–Rabin tests are performed using the GMP library, which supports arbitrary-precision integer operations. This ensures numerical correctness even for extremely large candidate numbers (100–1000+ digits). GMP's efficient handling of modular exponentiation and large integer comparisons makes it ideal for cryptographic-grade primality testing.

