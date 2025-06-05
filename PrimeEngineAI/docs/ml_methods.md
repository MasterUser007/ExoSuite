# Machine Learning Methods in ExoSuite

This document explains the machine learning strategies embedded within the ExoSuite engines, including references, algorithms used, and future extensibility options.

---

## 🔍 1. Symbolic-Assisted ML Filtering

Symbolic rules (e.g., digit patterns, mod classes, known residues) are used as a prefilter to eliminate obvious non-primes or unworthy candidates before any ML layer engages.

ML augments this by:
- Scoring ambiguous candidates post-symbolic filtering
- Using pattern recognition to identify regions of statistical promise

---

## 🧠 2. Reinforcement Learning for Candidate Scoring

The `CandidateScoringEngine` module leverages RL methods to assign and adjust confidence scores to numerical inputs.

**Key Features:**
- Rewards based on confirmed prime discoveries
- Penalties based on false positives or misclassifications
- State is defined by feature vectors extracted from candidate number properties

**Suggested RL Frameworks:**
- Deep Q-Networks (DQN)
- Policy Gradient Methods
- Multi-armed Bandit Models (exploration vs exploitation)

---

## 🧮 3. Symbolic-to-Statistical Bridge

ExoSuite uses heuristic features extracted from symbolic logic to generate input vectors:
- Last-digit residue class
- Prime-adjacency likelihood score
- Symbolic cache history
- ML-driven feature extraction (e.g., digit entropy, distribution)

---

## 🔬 4. Example Heuristics

- **Truncation Likelihood**: Numbers ending in '27', '51' often fail Miller-Rabin
- **Frequency Bias**: Numbers near known prime clusters are weighted higher
- **Entropy Check**: Digit randomness may indicate prime-likeness

---

## 📚 5. References

- [1] R. Crandall & C. Pomerance, "Prime Numbers: A Computational Perspective"
- [2] Goodfellow, Bengio, Courville. "Deep Learning", MIT Press (2016)
- [3] S. S. Ravi, "Machine Learning for Integer Factorization", arXiv:1804.07245
- [4] Silver et al., "Mastering the game of Go with deep neural networks and tree search", Nature (2016)
- [5] Knuth, "The Art of Computer Programming", Vol. 2 (Seminumerical Algorithms)

---

## 🛠 6. Extending ML in ExoSuite

- Add feature vectors to `shared_data_exchange.py`
- Introduce reward tracking in `candidate_scoring_engine.py`
- Plug reinforcement model into batch selector for candidate zones

This layer remains modular and will be expanded in future ExoSuite ML modules.