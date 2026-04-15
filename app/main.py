from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import run_agent

app = FastAPI()


class RequestModel(BaseModel):
    text: str


@app.get("/")
def root():
    return {"status": "Agent API running"}


@app.post("/ask")
def ask(req: RequestModel):
    return {"answer": run_agent(req.text)}