import grpc
import time
from concurrent import futures
import os
import sys

# from example import data_pb2_grpc, data_pb2
from example import data_pb2_grpc, data_pb2

current_fonder_path = os.path.split(os.path.realpath(__file__))[0]
print(current_fonder_path)
protocal_path = os.path.join(current_fonder_path, "..", "example")
print(protocal_path)
sys.path.append(protocal_path)


_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '8080'


class FormatData(data_pb2_grpc.FormatDataServicer):
    def DoFormat(self, request, context):
        str = request.text
        return data_pb2.actionresponse(text=str.upper(), value=1.0)


def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    data_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == '__main__':
    serve()
