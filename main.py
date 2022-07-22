from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def hello():
    return {"This is a heroku deployment text app"}