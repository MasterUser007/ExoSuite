# D. GMP Miller-Rabin Testing – Deterministic Validation Backbone

For high-confidence primality decisions, PrimeEngineAI uses GMP-backed Miller-Rabin testing. This step offers:
• Probabilistic validation with configurable rounds (e.g., 10, 25, 50)
• Deterministic fallback using ECPP for 200+ digit candidates
• Logging of all outcome metrics and latency percentiles for auditability

The integration with GMP ensures compatibility with standard cryptographic verification workflows.

