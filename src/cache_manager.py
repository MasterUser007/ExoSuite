import os, json
from pathlib import Path

class _EngineCache:
    def __init__(self, max_size=None):
        self.max_size = max_size
        self.cache = {}
    def set(self, key, value):
        if self.max_size and len(self.cache) >= self.max_size:
            del self.cache[next(iter(self.cache))]
        self.cache[key] = value
    def get(self, key):
        return self.cache.get(key)
    def metrics(self):
        return {"hits": len(self.cache), "size": len(self.cache)}

class CacheManager:
    symbolic = _EngineCache()
    hash     = _EngineCache()
    factor   = _EngineCache()

    def __init__(self, max_size=None):
        self.symbolic = _EngineCache(max_size)
        self.hash     = _EngineCache(max_size)
        self.factor   = _EngineCache(max_size)
        p = os.getenv("CACHE_PERSIST_PATH")
        if p and Path(p).is_file():
            data = json.loads(Path(p).read_text())
            for name, cache in [("symbolic", self.symbolic), ("hash", self.hash), ("factor", self.factor)]:
                for k, v in data.get(name, {}).items():
                    cache.cache[int(k)] = v

    def persist(self):
        p = os.getenv("CACHE_PERSIST_PATH")
        if not p: return
        Path(p).parent.mkdir(parents=True, exist_ok=True)
        out = {
            "symbolic": {str(k): v for k, v in self.symbolic.cache.items()},
            "hash":     {str(k): v for k, v in self.hash.cache.items()},
            "factor":   {str(k): v for k, v in self.factor.cache.items()},
            "metrics": {
                "symbolic_hits": len(self.symbolic.cache),
                "hash_hits":     len(self.hash.cache),
                "factor_hits":   len(self.factor.cache),
            },
        }
        Path(p).write_text(json.dumps(out, indent=2))

    def metrics(self):
        return {
            "symbolic": self.symbolic.metrics(),
            "hash":     self.hash.metrics(),
            "factor":   self.factor.metrics(),
        }
