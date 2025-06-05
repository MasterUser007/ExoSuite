# C. Infinitesimal Remainder Analysis – Probabilistic Lightweight Rejection

This layer provides low-cost, fast rejection by analyzing modularity signatures and statistical residue traits. It acts as a secondary filter between symbolic and deterministic layers, helping:
• Reduce false positives from ambiguous symbolic matches
• Lower overall GMP/Miller-Rabin test load
• Tune confidence thresholds to digit class, throughput goals, or error tolerance

