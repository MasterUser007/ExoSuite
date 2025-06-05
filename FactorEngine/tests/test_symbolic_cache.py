from src.symbolic_cache import apply_symbolic_filters

def test_basic_exclusion():
    assert not apply_symbolic_filters('222')  # trivially composite
