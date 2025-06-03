import httpx
import time
import json
import sys 

OUTPUT_FILE = "output/http_simple_small_independent.csv"
URL = 'http://127.0.0.1:5000'

with open('data/small_data.json') as file:
    small_data = json.load(file)

start = time.perf_counter()
response = httpx.post(URL,json=small_data)
end = time.perf_counter()


with open(OUTPUT_FILE, "a") as f:
    f.write(f"{sys.argv[1]},{(end-start)*1000}\n")