# A. Unit Tests

Unit tests validate the functionality of individual modules in isolation. These include:
• cache.py – Ensures symbolic filtering rules are correctly matched and cached.
• sieve.py – Verifies GPU and CPU sieving logic for small prime division.
• miller_rabin.py – Confirms probabilistic test returns expected outcomes across known prime/composite samples.
• remainder_analysis.py – Checks that remainder-based exclusions behave statistically as intended.
• config.py – Validates system configuration parameters, default values, and override logic.

