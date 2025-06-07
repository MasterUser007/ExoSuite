import os

import pytest

pytest.importorskip("hypothesis")


import sys

from hypothesis import given
from hypothesis import strategies as st

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../src"))
from exosuite_core import orchestrate_factoring
from FactorEngine.src.miller_rabin import is_probably_prime
from PrimeEngineAI.src.engine_core import main_factoring_engine as pef
from QuantumHash.src.engine_core import main_factoring_engine as qhf


@given(st.integers(min_value=2, max_value=5000))
def test_orch_fuzz(n):
    result = orchestrate_factoring(n)
    # Compare against direct engine calls
    assert result["PrimeEngineAI"] == pef(input_number=n)
    assert result["QuantumHash"] == qhf(input_number=n)
    assert result["FactorEngine"] == is_probably_prime(n)
