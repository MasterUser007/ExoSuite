<<<<<<< HEAD
class CacheManager:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value

    def clear(self):
        self.cache.clear()
=======
import os, json
from src._EngineCache import _EngineCache

class CacheManager:
    def __init__(self):
        self.persist_path = os.environ.get( CACHE_PERSIST_PATH,cache.json)
        self.symbolic = _EngineCache(symbolic,self)
        self.hash     = _EngineCache(hash,    self)
        self.factor   = _EngineCache(factor,  self)
        try:
            with open(self.persist_path,r,encoding=utf-8) as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
        for n in (symbolic,hash,factor):
            getattr(self,n).cache = data.get(n,{})
    def persist(self):
        out={symbolic:self.symbolic.cache,hash:self.hash.cache,factor:self.factor.cache}
        with open(self.persist_path,w,encoding=utf-8) as f:
            json.dump(out,f,indent=2)
>>>>>>> 3453edc (chore(repo): full monorepo restructure, test/config updates, and CI setup)
