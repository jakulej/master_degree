from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/")
async def handle_post(request: Request):
    data = await request.body()
    return PlainTextResponse("OK")

