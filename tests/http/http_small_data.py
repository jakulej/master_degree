import httpx
import time
import json


with open('../../data/small_data.json') as file:
    small_data = json.load(file)

for n in range(100):
    start = time.perf_counter()
    request = httpx.post('http://127.0.0.1:5000',json=small_data)
    end = time.perf_counter()
    print(request)
    print((end-start)*1000,"ms")
