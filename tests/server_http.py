from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/")
async def handle_post(request: Request):
    data = await request.json()
    return PlainTextResponse("OK")

@app.post("/file")
async def upload_file(request: Request):
    form = await request.form()
    upload = form["file"]
    content = await upload.read()
    return PlainTextResponse("OK")