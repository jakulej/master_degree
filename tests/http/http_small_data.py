import httpx
import time
import json


URL = 'http://127.0.0.1:5000'
OUTPUT_FILE = "http_small.csv"

with open(OUTPUT_FILE, "w") as f:
    f.write("request_number,time_ms\n")

with open('data/small_data.json') as file:
    small_data = json.load(file)

def test(i):
    for n in range(i):
        #client = httpx.Client(http1=True, timeout=5)
        start = time.perf_counter()
        response = httpx.post('http://127.0.0.1:5000',headers={"Connection": "close"},json=small_data)

        #response = client.post(URL, json=small_data)


        end = time.perf_counter()
        print(response)
        print((end-start)*1000,"ms")

        with open(OUTPUT_FILE, "a") as f:
            f.write(f"{n},{(end-start)*1000}\n")

test(100)