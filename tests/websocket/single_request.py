from websockets.sync.client import connect
import time
import json
import sys

OUTPUT_FILE = "output/websocket_single.csv"
URL = 'ws://192.168.88.2:8765'

with open("data/small_data.json", "r") as f:
    data_small = json.load(f)

start = time.perf_counter()
with connect(URL) as websocket:
    websocket.send(json.dumps(data_small))
    message = websocket.recv()
    end = time.perf_counter()

    print(message)
    with open(OUTPUT_FILE, "a") as f:
        f.write(f"{sys.argv[1]},{(end-start)*1000}\n")

