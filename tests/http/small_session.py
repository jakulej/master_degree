import time
import json
import sys
import requests

OUTPUT_FILE = "output/http_small_session.csv"
URL = 'http://127.0.0.1:8000'

with open('data/small_data.json') as file:
    small_data = json.load(file)

with open(OUTPUT_FILE, "w") as f:
    f.write("request_number,time_ms\n")

start = time.perf_counter()
session = requests.Session()
response = session.post(URL,json=small_data)
end = time.perf_counter()

with open(OUTPUT_FILE, "a") as f:
    f.write(f"{0},{(end-start)*1000}\n")


for n in range(int(sys.argv[1])-1):
    start = time.perf_counter()
    response = session.post(URL,json=small_data)
    end = time.perf_counter()

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"{n+1},{(end-start)*1000}\n")
session.close()