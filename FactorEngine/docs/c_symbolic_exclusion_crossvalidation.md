# C. Symbolic Exclusion Cross-Validation

All symbolic exclusion decisions are benchmarked against deterministic rule sets and tracked for:
• False positive rate (target < 0.1%)
• False negative rate (target < 0.01%)
• Compatibility with ML model predictions

Discrepancies between deterministic, ML-driven, and symbolic verdicts are flagged for review and used to calibrate thresholds and weights.

