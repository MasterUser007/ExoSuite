from remainder import remainder_batch


def test_remainder_divisible_by_3_or_7():
    batch = [
        {"id": 1, "value": "21"},
        {"id": 2, "value": "25"},
        {"id": 3, "value": "7"},
    ]
    passed, filtered = remainder_batch(batch)
    # 21 (3*7) filtered, 7 (equals prime 7) should pass, 25 passes
    assert {"id": 1, "value": "21"} in filtered
    assert {"id": 2, "value": "25"} in passed
    assert {"id": 3, "value": "7"} in passed
