import httpx
import time
import json
import subprocess

URL = 'http://127.0.0.1:8000'

def simple_reqest(request_number):
    result = subprocess.run(["python3", "tests/http/small_requests.py", str(request_number)], capture_output=True, text=True)

def session_requests(request_number):
    result = subprocess.run(["python3", "tests/http/small_session.py", str(request_number)], capture_output=True, text=True)


def test_independent_call(i,output_file):
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(i):
        result = subprocess.run(["python3", "tests/http/single_request_small.py", str(n)], capture_output=True, text=True)

def test_big_file(i, output_file,url):

    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")

    for n in range(i):
        result = subprocess.run(["python3", "tests/http/single_request_big.py", str(1)], capture_output=True, text=True)


#test_independent_call(100,"output/http_simple_small_independent.csv")
simple_reqest(100)
session_requests(100)
