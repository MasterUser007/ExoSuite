import sys, os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))
# Updated pipeline tests for list return
from src.engine_core import main_factoring_engine


def test_known_composite():
    result = main_factoring_engine(100)
    assert isinstance(result, list) and len(result) >= 1


def test_known_prime():
    result = main_factoring_engine(7)
    assert result == [7]
