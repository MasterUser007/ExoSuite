# B. False Positive and False Negative Logs

All pipeline test outcomes include annotated logs capturing:
• False positives: composites incorrectly labeled as probable primes
• False negatives: primes incorrectly excluded before reaching final validation

These logs are crucial for supervised ML training, especially for refining classifiers that operate alongside symbolic filtering. Each record includes feature traces to enable error attribution and correction.

