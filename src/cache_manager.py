import threading


class _EngineCache:
    def __init__(self):
        self.cache = {}
        self._lock = threading.Lock()

    def get(self, key):
        with self._lock:
            return self.cache.get(key)

    def set(self, key, value):
        with self._lock:
            self.cache[key] = value

    def clear(self):
        with self._lock:
            self.cache.clear()


class CacheManager:
    def __init__(self):
        self.symbolic = _EngineCache()
        self.hash = _EngineCache()
        self.factor = _EngineCache()

    def persist(self, path="cache.json"):
        import json

        with open(path, "w", encoding="utf-8") as f:
            data = {
                "symbolic": self.symbolic.cache,
                "hash": self.hash.cache,
                "factor": self.factor.cache,
            }
            json.dump(data, f)

    def load(self, path="cache.json"):
        import json

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.symbolic.cache = data.get("symbolic", {})
        self.hash.cache = data.get("hash", {})
        self.factor.cache = data.get("factor", {})
