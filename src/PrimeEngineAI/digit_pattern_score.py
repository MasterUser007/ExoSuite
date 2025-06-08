from ml_plugins.base import BaseMLPlugin
from ml_plugins.plugin_logger import log_plugin_usage
from ml_plugins.plugin_metrics import log_metrics


class DigitPatternScore(BaseMLPlugin):
    def __init__(self):
        self.name = "DigitPatternHeuristic"

    def score(self, candidate_number: int) -> float:
        s = str(candidate_number)
        result = 0.5
        if s.endswith("7") or s.endswith("3"):
            result = 0.9
        elif s.endswith("0") or s.endswith("5"):
            result = 0.1
        log_plugin_usage(self.name, candidate_number, result)
        log_metrics(self.name, result)
        return result

