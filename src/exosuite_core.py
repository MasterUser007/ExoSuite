<<<<<<< HEAD
def core_function():
    print("ExoSuite core function")
=======
from cache_manager import CacheManager
from PrimeEngineAI import pef
from QuantumHash.hasher import neighbors

cache_manager = CacheManager()

def orchestrate_factoring(n):
    cm = cache_manager

    symbolic_hit = cm.symbolic.get(n) is not None
    if symbolic_hit:
        factors = cm.symbolic.get(n)
    else:
        hash_hit = cm.hash.get(n) is not None
        if hash_hit:
            factors = cm.hash.get(n)
        else:
            factors = pef(input_number=n)
            cm.symbolic.set(n, factors)
            cm.hash.set(n, factors)

    factor_hit = cm.factor.get(n) is not None
    if not factor_hit:
        cm.factor.set(n, True)

    qh = neighbors(n)
    cm.persist()

    return {
        "PrimeEngineAI":      factors,
        "FactorEngine":       factor_hit,
        "QuantumHash":        qh,
        "symbolic_cache_hit": symbolic_hit,
        "hash_cache_hit":     cm.hash.get(n) is not None,
        "factor_cache_hit":   factor_hit,
    }
>>>>>>> 3453edc (chore(repo): full monorepo restructure, test/config updates, and CI setup)
