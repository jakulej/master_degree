import subprocess
import sys

def n_times(request_number):
    result = subprocess.run([sys.executable, "tests/gRPC/n_requests.py", str(request_number)], capture_output=True, text=True)

def single(request_number):
    output_file = "output/grpc_single.csv"
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(request_number):
        result = subprocess.run([sys.executable, "tests/gRPC/single_request.py", str(n)], capture_output=True, text=True)
        print(n)


def file(request_number):
    output_file = "output/grpc_file.csv"
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(request_number):
        result = subprocess.run([sys.executable, "tests/gRPC/file_request.py", str(n)], capture_output=True, text=True)
        print(n)

def stream(request_number):
    result = subprocess.run([sys.executable, "tests/gRPC/stream_requests.py", str(request_number)], capture_output=True, text=True)


#stream(10000)
file(1000)
#single(1000)
#n_times(10000)