#!/usr/bin/env python

from websockets.sync.client import connect
import time
import json

def hello():
    with open("data/small_data.json", "r") as f:
        data_small = json.load(f)


    start = time.perf_counter()
    with connect("ws://localhost:8765") as websocket:
        websocket.send(json.dumps(data_small))
        message = websocket.recv()
        end = time.perf_counter()
        print(f"Received: {message},Time: {(end-start)*1000}ms")


hello()