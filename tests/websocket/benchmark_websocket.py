import subprocess
import sys

def single(request_number):
    output_file = "output/websocket_single.csv"
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(request_number):
        result = subprocess.run([sys.executable, "tests/websocket/single_request.py", str(n)], capture_output=True, text=True)
        print(n)

def n_times(request_number):
    result = subprocess.run([sys.executable, "tests/websocket/n_requests.py", str(request_number)], capture_output=True, text=True)

def file(request_number):
    output_file = "output/websocket_big.csv"
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(request_number):
        result = subprocess.run([sys.executable, "tests/websocket/file_request.py", str(n)], capture_output=True, text=True)
        print(n)



single(1000)

#n_times(10000)
#file(1000)