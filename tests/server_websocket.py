#!/usr/bin/env python

import asyncio
import json
from websockets.asyncio.server import serve

async def client_handler(websocket):
    async for message in websocket:
        data = json.loads(message)
        print(data)
        await websocket.send("OK")

async def main():
    async with serve(client_handler, "localhost", 8765) as server:
        await server.serve_forever()

asyncio.run(main())