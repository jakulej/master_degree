import grpc

from proto import data_pb2, data_pb2_grpc

import json
import time
import sys



def run():
    output_file = "output/grpc_stream_small.csv"
    with open(output_file, "w") as f:
        f.write("request_number,time_ms\n")

    with open("data/small_data.json") as f:
        user_data = json.load(f)


    start = time.perf_counter()
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = data_pb2_grpc.UserServiceStub(channel)
        start = time.perf_counter()
        user = data_pb2.User(**user_data)
        response_iterator = stub.StreamUsers(iter([user]))
        for response in response_iterator:
            end = time.perf_counter()
            with open(output_file, "a") as f:
                f.write(f"{0},{(end-start)*1000}\n")

        for n in range(int(sys.argv[1])-1):
            start = time.perf_counter()
            user = data_pb2.User(**user_data)
            response_iterator = stub.StreamUsers(iter([user]))
            for response in response_iterator:
                end = time.perf_counter()
                with open(output_file, "a") as f:
                    f.write(f"{n+1},{(end-start)*1000}\n")


if __name__ == "__main__":
    run()