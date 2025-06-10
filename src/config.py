import os

SERVICE_URLS = {
    "filter":    os.getenv("FILTER_SERVICE_URL",    "http://localhost:5001"),
    "sieve":     os.getenv("SIEVE_SERVICE_URL",     "http://localhost:5002"),
    "remainder": os.getenv("REMAINDER_SERVICE_URL", "http://localhost:5004"),
    "primality": os.getenv("PRIMALITY_SERVICE_URL", "http://localhost:5003"),
}
