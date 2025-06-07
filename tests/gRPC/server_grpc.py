import grpc
from concurrent import futures
import time


from proto import data_pb2, data_pb2_grpc

class UserServiceServicer(data_pb2_grpc.UserServiceServicer):
    def SendUser(self, request, context):
        data = request
        return data_pb2.Response(message="OK")
    def StreamUsers(self, request_iterator, context):
        for user in request_iterator:
            yield data_pb2.Response(message="OK")

class FileServiceServicer(data_pb2_grpc.FileServiceServicer):
    def Upload(self, request_iterator, context):
        file_bytes = b""
        for chunk in request_iterator:
            file_bytes += chunk.content
        return data_pb2.UploadStatus(message="Ok")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    data_pb2_grpc.add_FileServiceServicer_to_server(FileServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
