from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Working"}

@app.get("/test")
def test():
    return {"status": "ok"}
