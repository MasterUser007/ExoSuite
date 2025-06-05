
class SymbolicCache:
    def __init__(self):
        self.cache = {}

    def add(self, number, reason):
        self.cache[number] = reason

    def is_composite(self, number):
        return number in self.cache

    def get_reason(self, number):
        return self.cache.get(number, "Unknown")


def apply_symbolic_filters(n: int) -> bool:
    try:
        num = int(n)
    except:
        return False
    if num < 2:
        return False
    if num % 2 == 0 and num != 2:
        return False
    if num % 5 == 0 and num != 5:
        return False
    return True
