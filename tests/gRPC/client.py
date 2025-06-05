import grpc
import json_struct_pb2
import json_struct_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = json_struct_pb2_grpc.JsonServiceStub(channel)

    # Wypełniamy dane zgodnie ze strukturą
    item = json_struct_pb2.JsonData(
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
        about="Sunt magna tempor labore est...",
        registered="2023-05-19T08:42:19 -02:00",
        latitude=39.975429,
        longitude=140.989848
    )

    request = json_struct_pb2.JsonDataList(items=[item])
    response = stub.SendJson(request)
    print("Odpowiedź:", response.status)

if __name__ == "__main__":
    run()
