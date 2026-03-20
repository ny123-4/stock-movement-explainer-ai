from fastapi import FastAPI

app = FastAPI()
red = "I am a color"


@app.get("/")
def read_root():
    return {"Hello World!"}



