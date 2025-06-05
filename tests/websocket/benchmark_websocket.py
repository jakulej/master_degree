import subprocess

def single(request_number):
    output_file = "output/websocket_single.csv"
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(request_number):
        result = subprocess.run(["python3", "tests/websocket/single_request.py", str(request_number)], capture_output=True, text=True)
        print(result)

def n_times(request_number):
    result = subprocess.run(["python3", "tests/websocket/n_requests.py", str(request_number)], capture_output=True, text=True)
    print(result)

def file(request_number):
    output_file = "output/websocket_big.csv"
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")
    for n in range(request_number):
        result = subprocess.run(["python3", "tests/websocket/file_request.py", str(request_number)], capture_output=True, text=True)
        print(result)


#single(100)
#n_times(22)
file(20)