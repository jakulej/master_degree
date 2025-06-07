import grpc
import time
import sys

from proto import data_pb2, data_pb2_grpc
OUTPUT_FILE = "output/grpc_file.csv"
URL = '192.168.88.2:50051'
def file_chunk_generator():
    with open("data/big_file", "rb") as f:
        while chunk := f.read(64 * 1024):
            yield data_pb2.FileChunk(content=chunk)

def run():
    start = time.perf_counter()
    with grpc.insecure_channel(URL) as channel:
        stub = data_pb2_grpc.FileServiceStub(channel)
        response = stub.Upload(file_chunk_generator())
        end = time.perf_counter()
        with open(OUTPUT_FILE, "a") as f:
            f.write(f"{int(sys.argv[1])},{(end-start)*1000}\n")


if __name__ == "__main__":
    run()
