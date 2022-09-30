import grpc
import os
import sys

current_fonder_path = os.path.split(os.path.realpath(__file__))[0]
print (current_fonder_path)
protocal_path = os.path.join(current_fonder_path,"..","example")
print (protocal_path)
sys.path.append(protocal_path)
import data_pb2, data_pb2_grpc

_HOST = 'localhost'
_PORT = '8080'


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # Монитор канала
    print(conn)
    client = data_pb2_grpc.FormatDataStub(channel=conn)   # Клиент использует класс Stub для отправки запроса, параметр - канал, чтобы связать ссылку
    print(client)
    response = client.DoFormat(data_pb2.actionrequest(text='hello,world!'))   # Возвращенный результат - класс, определенный в прото
    print("received: " + response.text + str(response.value))


if __name__ == '__main__':
    run()