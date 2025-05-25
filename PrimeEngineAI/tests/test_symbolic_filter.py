import pytest
from symbolic_filter import symbolic_filter

def test_filter_excludes_even_end():
    batch = [{'id':1,'value':'1234'},{'id':2,'value':'1237'}]
    passed, filtered = symbolic_filter(batch)
    assert filtered == [{'id':1,'value':'1234'}]
    assert passed   == [{'id':2,'value':'1237'}]

def test_filter_repeating_digits():
    batch = [{'id':3,'value':'11112'}]
    passed, filtered = symbolic_filter(batch)
    assert filtered == batch
    assert passed   == []
