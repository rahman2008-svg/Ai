from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI App Running 🚀"}

@app.get("/ask")
def ask(q: str):
    return {"response": f"You asked: {q}"}
