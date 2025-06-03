import httpx
import time
import json
import sys 

OUTPUT_FILE = "output/http_client_big.csv"
URL = 'http://127.0.0.1:5000/file'

with open('data/big_file','rb') as big_data:
    start = time.perf_counter()
    response = httpx.post(URL,files={"file":big_data})
    end = time.perf_counter()


with open(OUTPUT_FILE, "a") as f:
    f.write(f"{sys.argv[1]},{(end-start)*1000}\n")