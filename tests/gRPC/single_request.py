import grpc
import time
import json
import sys

from proto import data_pb2_grpc, data_pb2
OUTPUT_FILE = "output/grpc_single.csv"

def run():
    with open("data/small_data.json", "r") as f:
        user_data = json.load(f)

    start = time.perf_counter()
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = data_pb2_grpc.UserServiceStub(channel)
        user = data_pb2.User(**user_data)
        response = stub.SendUser(user)
        end = time.perf_counter()
        with open(OUTPUT_FILE, "a") as f:
            f.write(f"{int(sys.argv[1])},{(end-start)*1000}\n")

if __name__ == '__main__':
    run()
