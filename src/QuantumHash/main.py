from fastapi import FastAPI
from pydantic import BaseModel
from engine_core import main_factoring_engine

app = FastAPI(title="FactorEngine API", version="1.0")


class FactorRequest(BaseModel):
    input_number: int


@app.post("/factor/")
def factor_number(req: FactorRequest):
    result = main_factoring_engine(input_number=req.input_number)
    return {"input": req.input_number, "factors": result}


# Prometheus metrics
from prometheus_client import Counter, start_http_server

requests_total = Counter("api_requests_total", "Total API requests")


@app.on_event("startup")
def start_metrics():
    start_http_server(9000)


@app.middleware("http")
async def count_requests(request, call_next):
    requests_total.inc()
    return await call_next(request)

