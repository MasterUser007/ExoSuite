# symbolic_factoring.py


def basic_symbolic_filters(n: int) -> bool:
    """
    Apply symbolic rules to exclude obvious non-candidates early.
    Return True if the candidate should be excluded.
    """
    if n < 2:
        return True
    if n % 2 == 0 and n != 2:
        return True
    if n % 5 == 0 and n != 5:
        return True
    if str(n)[-1] in ["0", "4", "6", "8"]:  # fast digit screen
        return True
    return False
