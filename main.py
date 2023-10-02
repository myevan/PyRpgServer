from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def welcome():
    return {"Msg": "Hello"}