from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def getWallet():
    return {"message": "Hello World"}