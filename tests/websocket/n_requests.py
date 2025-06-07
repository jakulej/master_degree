from websockets.sync.client import connect
import time
import json
import sys

OUTPUT_FILE = "output/websocket_n_times.csv"
URL = 'ws://192.168.88.2:8765'

with open(OUTPUT_FILE, "w") as f:
    f.write("request_number,time_ms\n")

with open("data/small_data.json", "r") as f:
    data_small = json.load(f)

start = time.perf_counter()
with connect(URL) as websocket:
    websocket.send(json.dumps(data_small))
    message = websocket.recv()
    end = time.perf_counter()

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"{0},{(end-start)*1000}\n")

    for n in range(int(sys.argv[1])-1):
        start = time.perf_counter()
        websocket.send(json.dumps(data_small))
        message = websocket.recv()
        end = time.perf_counter()
        with open(OUTPUT_FILE, "a") as f:
            f.write(f"{n+1},{(end-start)*1000}\n")




