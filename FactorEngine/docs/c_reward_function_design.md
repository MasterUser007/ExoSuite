# C. Reward Function Design

The RL system uses a carefully structured reward function to encourage:
• Early exclusion of confirmed composites (+ reward for shallow filtering success)
• Efficient use of symbolic and ML resources (avoiding unnecessary escalation)
• High overall throughput (reward tied to batch completion speed)
• Reduced false positive risk (penalty for misclassifying composites as probable primes)

Rewards are accumulated across batches and candidate classes, allowing generalization beyond specific numeric traits.

