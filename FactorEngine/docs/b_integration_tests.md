# B. Integration Tests

Integration tests confirm that subsystems function correctly together. These include:
• test_pipeline.py – Validates end-to-end candidate processing from input to final validation.
• test_gpu_sieve.py – Ensures sieve outputs feed correctly into symbolic and remainder layers.
• test_cache.py – Confirms that symbolic cache operations remain consistent across batch contexts and node boundaries.

