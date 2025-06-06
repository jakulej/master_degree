import grpc
from concurrent import futures
import time


from proto import data_pb2, data_pb2_grpc

class UserServiceServicer(data_pb2_grpc.UserServiceServicer):
    def SendUser(self, request, context):
        print("Received user data:")
        print(request)
        return data_pb2.Response(message="OK")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
