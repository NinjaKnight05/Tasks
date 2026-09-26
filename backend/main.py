from fastapi import FastAPI
from database import Base, engine
from models import User
from routes import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)

@app.get("/")
def root():
    return {"status": "ok"}