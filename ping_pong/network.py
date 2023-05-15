import socket
from helper_functions import *


class Network():
    def __init__(self, ip="localhost", port=5555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip
        self.port = port
        self.addr = (self.server, self.port)
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            print("failed")

    def send(self, data):
        try:
            self.client.send(str.encode(make_pos(data)))
            print("sending ", make_pos(data))
        except:
            pass

    def rcv(self):
        try:
            data = read_pos(self.client.recv(2048).decode())
            print("recieved ", make_pos(data))
            return data
        except:
            print("rcv failed")
            return (0, 0, 0, 0, 0, 0, 0, 0)

    def threaded_client(self):
        pass
