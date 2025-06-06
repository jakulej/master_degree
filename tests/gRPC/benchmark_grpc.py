import subprocess

def n_times(request_number):
    result = subprocess.run(["python3", "tests/gRPC/n_requests.py", str(request_number)], capture_output=True, text=True)
    print(result)

def single(request_number):
    output_file = "output/grpc_single.csv"
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(request_number):
        result = subprocess.run(["python3", "tests/gRPC/single_request.py", str(request_number)], capture_output=True, text=True)
        print(result)


def file(request_number):
    output_file = "output/grpc_file.csv"
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(request_number):
        result = subprocess.run(["python3", "tests/gRPC/file_request.py", str(request_number)], capture_output=True, text=True)
        print(result)

def stream(request_number):
    result = subprocess.run(["python3", "tests/gRPC/stream_requests.py", str(request_number)], capture_output=True, text=True)
    print(result)


stream(100)
#file(10)
#single(10)
#n_times(100)