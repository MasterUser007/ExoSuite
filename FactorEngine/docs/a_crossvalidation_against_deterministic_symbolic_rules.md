# A. Cross-Validation Against Deterministic Symbolic Rules

Every exclusion made by an ML model is cross-validated with corresponding symbolic filtering outcomes. This two-layer verification process ensures that:
• ML predictions are consistent with human-verified symbolic patterns
• Symbolic overrides can flag and halt potential false negatives caused by overly aggressive ML exclusions
• Drift from originally validated rules is caught early through statistical discrepancy detection. This safeguard prevents critical dependency on non-transparent ML logic and maintains the interpretability of all exclusion actions.

