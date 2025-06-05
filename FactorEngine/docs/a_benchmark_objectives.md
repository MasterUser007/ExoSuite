# A. Benchmark Objectives

The study will be structured around the following measurable performance metrics:
• Filtering throughput (candidates processed per second)
• False positive rate (composites incorrectly passed)
• False negative rate (primes incorrectly excluded)
• Candidate rejection efficiency (early vs. late stage exclusion)
• Latency distribution per stage (symbolic, sieve, probabilistic, deterministic)

B. Comparative Tools

PrimeEngineAI will be benchmarked against a cross-section of established peer tools, including:
• GIMPS – The distributed Great Internet Mersenne Prime Search, optimized for Mersenne primes using Lucas-Lehmer testing
• OpenPFGW – A general-purpose probabilistic prime tester using Fermat, Lucas, and LLR logic
• msieve – A factorization and sieving tool used for pre-screening composite ranges

These tools are selected based on popularity, legacy use, and representativeness of traditional CPU-bound and deterministic pipelines.

