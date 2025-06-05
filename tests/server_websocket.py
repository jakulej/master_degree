#!/usr/bin/env python

import asyncio
import json
from websockets.asyncio.server import serve

async def client_handler(websocket):
    async for message in websocket:
        data = json.loads(message)
        await websocket.send("OK")
        print("Message Recive")

async def main():
    async with serve(client_handler, "localhost", 8765) as server:
        await server.serve_forever()

asyncio.run(main())