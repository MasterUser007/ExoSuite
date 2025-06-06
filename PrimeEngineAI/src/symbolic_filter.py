from typing import Dict, List, Tuple


def symbolic_filter(batch: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    """
    Filters out composite candidates based on simple digit rules:
      - Exclude any number ending in 0,2,4,5,6,8
      - Exclude any number with a digit repeated 4+ times in a row
    Returns (passed, filtered).
    """
    passed, filtered = [], []
    for item in batch:
        val = item["value"]
        # Rule: last digit exclusion
        if val[-1] in {"0", "2", "4", "5", "6", "8"}:
            filtered.append(item)
            continue
        # Rule: 4+ repeating digits
        if any(d * 4 in val for d in "0123456789"):
            filtered.append(item)
            continue
        passed.append(item)
    return passed, filtered
