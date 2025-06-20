import sys, os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))
import pytest
from src.engine_core import main_factoring_engine


@pytest.mark.parametrize(
    "input_number, expected_factors", [(15, [3, 5]), (77, [7, 11]), (221, [13, 17])]
)
def test_black_box_factoring(input_number, expected_factors):
    result = main_factoring_engine(input_number=input_number)
    result_str = result if isinstance(result, str) else ",".join(str(x) for x in result)
    for factor in expected_factors:
        assert (
            str(factor) in result_str
        ), f"Expected factor {factor} not in result {result}"
