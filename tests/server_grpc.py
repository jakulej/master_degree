import grpc
from concurrent import futures
import json_struct_pb2
import json_struct_pb2_grpc

class JsonService(json_struct_pb2_grpc.JsonServiceServicer):
    def SendJson(self, request, context):
        for item in request.items:
            print(f"Name: {item.name}, Age: {item.age}, Active: {item.isActive}")
        return json_struct_pb2.JsonResponse(status="Received")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    json_struct_pb2_grpc.add_JsonServiceServicer_to_server(JsonService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Server running on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
