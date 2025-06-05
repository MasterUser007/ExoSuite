# D. False Positive Rejection Logs

When candidate numbers incorrectly pass early filters but are later invalidated, the system logs symbolic and ML features responsible for misclassification. These logs:
• Help improve ML model robustness and symbolic pattern weighting
• Identify numeric corner cases where traditional filters fail
• Provide statistical samples for anomaly detection and rule refinement
Each log entry is labeled with the candidate ID, misclassification reason, and symbolic path traversal.

