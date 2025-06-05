# B. Modular AI Integration Points

• training_data/: Labeled Training Dataset Repository

Contains structured metadata for each candidate, including digit traits, cache outcomes, symbolic hits, and final verdicts. Used to train ML models to recognize difficult-to-filter compositeness traits.

• inference/: ML Prediction Scripts

Includes scripts that load trained models to score candidates in real time. Model outputs are used to prioritize or bypass certain filters based on prediction confidence.

• retrain.py: Periodic Model Update Utility

This script supports scheduled retraining of ML models using new pipeline output data. It enables continuous improvement and adaptation of ML classifiers to evolving candidate behavior.

