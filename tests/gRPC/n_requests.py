import grpc
import time
import json
import sys

from proto import data_pb2_grpc, data_pb2

OUTPUT_FILE = "output/grpc_n_times.csv"
with open(OUTPUT_FILE, "w") as f:
    f.write("request_number,time_ms\n")

def run(times):
    with open("data/small_data.json", "r") as f:
        user_data = json.load(f)


    start = time.perf_counter()
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = data_pb2_grpc.UserServiceStub(channel)
        user = data_pb2.User(**user_data)
        response = stub.SendUser(user)
        end = time.perf_counter()
        with open(OUTPUT_FILE, "a") as f:
            f.write(f"{0},{(end-start)*1000}\n")


        for n in range(int(sys.argv[1])-1):
            start = time.perf_counter()
            response = stub.SendUser(user)
            end = time.perf_counter()
            print("Server response:", response.message, " Time: ", (end-start)*1000,"ms")
            with open(OUTPUT_FILE, "a") as f:
                f.write(f"{n+1},{(end-start)*1000}\n")

if __name__ == '__main__':
    run(100)
