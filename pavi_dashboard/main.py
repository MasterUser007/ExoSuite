from fastapi import FastAPI, Request
from pydantic import BaseModel
import logging, datetime

app = FastAPI()
logging.basicConfig(filename='dashboard.log', level=logging.INFO)

class Event(BaseModel):
    department: str
    status: str
    message: str

@app.post('/event')
async def receive_event(event: Event):
    timestamp = datetime.datetime.now().isoformat()
    logging.info(f"{timestamp} [{event.department}] {event.status}: {event.message}")
    return {"ok": True, "received": event}

@app.get('/')
async def index():
    with open('dashboard.log') as f:
        logs = f.readlines()
    return {'events': logs[-100:]}