import time
import json
import subprocess
import requests
import sys

URL = 'http://192.168.88.2:8000'

def simple_reqest(request_number):
    result = subprocess.run([sys.executable, "tests/http/small_requests.py", str(request_number)], capture_output=True, text=True)
    print(result)

def session_requests(request_number):
    result = subprocess.run([ sys.executable , "tests/http/small_session.py", str(request_number)], capture_output=True, text=True)


def test_independent_call(i,output_file):
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(i):
        result = subprocess.run([sys.executable, "tests/http/single_request_small.py", str(n)], capture_output=True, text=True)
        print("Test: ",n)

def test_big_file(i, output_file):
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(i):
        result = subprocess.run([sys.executable, "tests/http/single_request_big.py", str(n)], capture_output=True, text=True)
        print("Test: ",n)


#test_independent_call(10000,"output/http_simple_small_independent.csv")
#simple_reqest(100)

#session_requests(10000)

test_big_file(1000,"output/http_big.csv") 