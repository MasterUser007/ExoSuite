# A. training_data/ – Repository for Symbolic Filtering ML Training Data

This directory houses the raw and pre-processed input datasets used to train symbolic exclusion classifiers. Each labeled record contains:
• Digit structure (e.g., terminal digits, repeating sequences, mirrored patterns)
• Symbolic rule outcomes and cache tier hits
• Stage-by-stage verdicts (filtered, passed, tested)
• Final primality result (prime or composite)

These structured samples are used to train supervised models that learn correlations between symbolic traits and final classification outcomes. The dataset supports feature engineering, batch segmentation, and class balancing for reproducible ML training.

