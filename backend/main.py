from fastapi import FastAPI
from database import engine

app = FastAPI(title="Autonomous Freelance Agent")

@app.get("/")
def root():
    return {"message": "AI Freelance Agent Running"}

@app.get("/db-test")
def db_test():
    return {"database": "connected"}