import httpx
import time
import json
import subprocess

URL = 'http://127.0.0.1:5000'

def simple_reqest(i,output_file,url):
    with open('data/small_data.json') as file:
        small_data = json.load(file)

    output_file = "output/http_simple_small.csv"
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")

    for n in range(i):
        start = time.perf_counter()
        response = httpx.post(url,json=small_data)
        end = time.perf_counter()

        with open(output_file, "a") as f:
            f.write(f"{n},{(end-start)*1000}\n")

def client_request(i,output_file,url):
    with open('data/small_data.json') as file:
        small_data = json.load(file)

    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")

    client = httpx.Client()

    for n in range(i):
        start = time.perf_counter()
        response = client.post(url,json=small_data)
        end = time.perf_counter()

        with open(output_file, "a") as f:
            f.write(f"{n},{(end-start)*1000}\n")
    client.close()

def test_independent_call(i,output_file):
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(i):
        result = subprocess.run(["python3", "tests/http/single_request_small.py", str(n)], capture_output=True, text=True)

def test_big_file(i, output_file,url,big_data):

    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")

    for n in range(i):
        for n in range(i):
            result = subprocess.run(["python3", "tests/http/single_request_small.py", str(n)], capture_output=True, text=True)


#test_independent_call(100,"output/http_simple_small_independent.csv")
#simple_reqest(100,"output/http_simple_small.csv",URL)
#client_request(100,"output/http_client_small.csv",URL)
test_big_file(100,"output/http_client_big.csv",URL+"/file","data/big_file")