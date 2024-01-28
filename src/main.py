from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wanker"}

@app.get('/insult')
def insult_man():
    return {"message": "Total Wanker"}