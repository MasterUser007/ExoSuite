# B. inference/ – ML Model Prediction Scripts

This module includes inference utilities that allow trained models to evaluate candidates in real time. Functions include:
• Scoring a candidate’s likelihood of being composite based on structural and symbolic metadata
• Producing a confidence score that determines whether to bypass, escalate, or deprioritize the candidate
• Outputting classification logs and prediction confidence to audit traceability

The inference layer is designed to run efficiently alongside symbolic filtering, using shared feature representations.

