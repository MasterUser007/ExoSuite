# ml_plugins/base.py


class BaseMLPlugin:
    def __init__(self):
        self.name = "BasePlugin"

    def score(self, candidate_number: int) -> float:
        """
        Return a float score from 0.0 (low likelihood of being prime) to 1.0 (high).
        """
        raise NotImplementedError("Plugin must implement score() method")
