# C. Training Data Composition

Training data is generated from historical candidate evaluations and filtering logs. Each record is labeled based on the final validation outcome (prime or composite) and includes:
• Symbolic pass/fail history
• ML prediction confidence (if previously scored)
• False positive and false negative annotations from GMP/ECPP stage

The training process emphasizes balance across digit classes, filtering depth, and known edge cases to ensure generalizability. The v1 symbolic filtering model provides a foundation for data-driven symbolic exclusion enhancement in PrimeEngineAI. Its lightweight architecture and transparent design make it ideal for early-stage integration, rapid retraining, and side-by-side evaluation with legacy rule-based systems. Future iterations will introduce reinforcement mechanisms and ensemble modeling for increased filtering power.

