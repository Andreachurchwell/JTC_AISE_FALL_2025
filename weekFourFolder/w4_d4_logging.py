from fastapi import FastAPI, Request
import logging, json

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    log_data = {
        "method": request.method,
        "path": request.url.path,
        "client": request.client.host
    }
    logging.info(json.dumps(log_data))
    response = await call_next(request)
    return response

@app.get("/")
def root():
    return {"ok": True}

@app.get("/health")
def health():
    return {"status": "alive"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

