import time
import json
import sys
import requests

OUTPUT_FILE = "output/http_big.csv"
URL = 'http://192.168.88.2:8000'

with open('data/big_file','rb') as big_data:
    start = time.perf_counter()
    response = requests.post(URL+"/file",files={"file":big_data})
    end = time.perf_counter()


with open(OUTPUT_FILE, "a") as f:
    f.write(f"{sys.argv[1]},{(end-start)*1000}\n")