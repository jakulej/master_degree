import grpc
import time

from proto import data_pb2_grpc, data_pb2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = data_pb2_grpc.UserServiceStub(channel)
        user = data_pb2.User(
            _id="683de5db39e1693e2430bbb8",
            index=0,
            guid="b6f29743-ebe8-4229-aeaf-8281d05f7538",
            isActive=False,
            balance="$2,182.65",
            age=27,
            eyeColor="brown",
            name="Mays Rowe",
            gender="male",
            company="ZIORE",
            email="maysrowe@ziore.com",
            phone="+1 (976) 525-3112",
            address="519 Garden Place, Vale, Marshall Islands, 106",
            about="Sunt magna tempor labore est proident deserunt non proident pariatur esse labore voluptate.",
            registered="2023-05-19T08:42:19 -02:00",
            latitude=39.975429,
            longitude=140.989848
        )
        for n in range(10):
            start = time.perf_counter()
            response = stub.SendUser(user)
            end = time.perf_counter()
            print("Server response:", response.message, " Time: ", (end-start)*1000,"ms")

if __name__ == '__main__':
    run()
