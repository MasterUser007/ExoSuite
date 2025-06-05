
class SymbolicCache:
    def __init__(self):
        self.cache = {}

    def add(self, number, reason):
        self.cache[number] = reason

    def is_composite(self, number):
        return number in self.cache

    def get_reason(self, number):
        return self.cache.get(number, "Unknown")
