# Stage 3: Symbolic/GPU Sieve

This stage performs high-throughput sieving by combining traditional symbolic rules with GPU-powered sieving arrays. The GPU executes massively parallel trial divisions to exclude multiples of known small primes and cached non-prime structures. At the same time, symbolic rule sets apply bitmask-based filters and structural recognizers for layered exclusion. This hybrid approach leverages symbolic logic for fine-grained pattern exclusion and GPU acceleration for rapid numerical checks, allowing millions of candidates to be processed concurrently.

