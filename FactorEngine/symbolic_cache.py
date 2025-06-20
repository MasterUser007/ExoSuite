# symbolic_cache.py


class SymbolicCache:
    def __init__(self):
        self.tier1 = set()  # fast rejection
        self.tier2 = set()  # reusable exclusion patterns
        self.history = []

    def check(self, number):
        if number in self.tier1:
            return True, "Tier 1"
        if number in self.tier2:
            return True, "Tier 2"
        return False, None

    def update(self, number, tier="tier1"):
        if tier == "tier1":
            self.tier1.add(number)
        elif tier == "tier2":
            self.tier2.add(number)
        self.history.append((number, tier))
