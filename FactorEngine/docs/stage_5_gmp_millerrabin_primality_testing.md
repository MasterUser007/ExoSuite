# Stage 5: GMP Miller-Rabin Primality Testing

Candidates that survive all previous filters enter the final validation stage, where they undergo Miller–Rabin primality testing. This probabilistic test is implemented using the GNU MP (GMP) library to ensure high-speed and high-precision validation. Multiple configurable rounds of Miller–Rabin reduce the probability of false positives exponentially. For candidates exceeding 200 digits, the Elliptic Curve Primality Proving (ECPP) algorithm is used, which provides deterministic certification based on deep number theory. This final step guarantees that any number reported as prime has passed rigorous mathematical scrutiny.

