import pytest
from engine_core import main_factoring_engine

@pytest.mark.parametrize("input_number, expected_factors", [
    (15, [3, 5]),
    (77, [7, 11]),
    (221, [13, 17])
])
def test_black_box_factoring(input_number, expected_factors):
    result = main_factoring_engine(input_number=input_number)
    for factor in expected_factors:
        assert factor in result, f"Expected factor {factor} not in result {result}"