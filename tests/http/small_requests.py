import time
import json
import sys
import requests

OUTPUT_FILE = "output/http_small.csv"
URL = 'http://192.168.88.2:8000'

with open('data/small_data.json') as file:
    small_data = json.load(file)

with open(OUTPUT_FILE, "w") as f:
    f.write("request_number,time_ms\n")

for n in range(int(sys.argv[1])):
    start = time.perf_counter()
    response = requests.post(URL,json=small_data)
    end = time.perf_counter()

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"{n},{(end-start)*1000}\n")