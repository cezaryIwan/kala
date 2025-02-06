from fastapi import FastAPI
from database.database import engine
from database import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def getWallet():
    return {"message": "Hello World"}