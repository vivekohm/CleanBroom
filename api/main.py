from fastapi import FastAPI
from app.pipeline import query_system

app = FastAPI()

@app.get("/ask")
def ask(q: str):
    answer = query_system(q)
    return {"answer": answer}