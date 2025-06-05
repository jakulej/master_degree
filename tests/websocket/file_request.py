from websockets.sync.client import connect
import time
import json
import sys

OUTPUT_FILE = "output/websocket_big.csv"


with open("data/small_data.json", "r") as f:
    data_small = json.load(f)

start = time.perf_counter()
with connect("ws://localhost:8765") as websocket:
    with open("data/big_file", "rb") as f:
        while chunk := f.read(4096):
            websocket.send(chunk)
    websocket.send(b"--end--")
    message = websocket.recv()
    end = time.perf_counter()

    print(message)
    with open(OUTPUT_FILE, "a") as f:
        f.write(f"{sys.argv[1]},{(end-start)*1000}\n")

