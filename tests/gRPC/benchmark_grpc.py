import subprocess

def n_times(request_number):
    result = subprocess.run(["python3", "tests/gRPC/n_requests.py", str(request_number)], capture_output=True, text=True)

def single(request_number):
    output_file = "output/grpc_single.csv"
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(request_number):
        result = subprocess.run(["python3", "tests/gRPC/single_request.py", str(n)], capture_output=True, text=True)


def file(request_number):
    output_file = "output/grpc_file.csv"
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(request_number):
        result = subprocess.run(["python3", "tests/gRPC/file_request.py", str(n)], capture_output=True, text=True)

def stream(request_number):
    result = subprocess.run(["python3", "tests/gRPC/stream_requests.py", str(request_number)], capture_output=True, text=True)


stream(100)
file(100)
single(100)
n_times(100)