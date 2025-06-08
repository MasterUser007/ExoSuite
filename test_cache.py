import os, json
from src.cache_manager import CacheManager

print('CACHE_PERSIST_PATH=', os.environ.get('CACHE_PERSIST_PATH'))
cm = CacheManager()
cm.symbolic.cache.clear()
cm.hash.cache.clear()
cm.factor.cache.clear()
cm.symbolic.set(1, [1])
cm.persist()

print('After persist, file exists?', os.path.exists(os.environ['CACHE_PERSIST_PATH']))
print(open(os.environ['CACHE_PERSIST_PATH'], 'r', encoding='utf-8').read())

cm2 = CacheManager()
val = cm2.symbolic.get(1)
assert val == 1, f"LOADED WRONG: got {val}"
print('✔ Persistence OK')
