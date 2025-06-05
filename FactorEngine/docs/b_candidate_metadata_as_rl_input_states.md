# B. Candidate Metadata as RL Input States

Each candidate is represented as a vector of symbolic, structural, and heuristic features, such as:
• Digit pattern traits (e.g., mirrored, repeating, terminal digits)
• Symbolic cache tier hit ratios
• Historical filtering confidence scores
• Residue analysis patterns (modulo behaviors)
These feature vectors form the RL environment's state space, allowing the agent to learn which candidate profiles yield the best filtering outcomes.

