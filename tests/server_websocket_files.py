#!/usr/bin/env python

import asyncio
import json
from websockets.asyncio.server import serve
import io

async def client_handler(websocket):
    buffer = io.BytesIO()
    async for message in websocket:
        if message == b"--end--":
            full_data = buffer.getvalue()
            #print(full_data)
            print(f"Odebrano plik ({len(full_data)} bajtów)")
            await websocket.send("OK")
            buffer = io.BytesIO()
        else:
            #print(message)
            buffer.write(message)

async def main():
    async with serve(client_handler, "localhost", 8765) as server:
        await server.serve_forever()

asyncio.run(main())