import socket
from helper_functions import *


class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "172.21.122.101"
        self.port = 5555
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
        except socket.error as e:
            print(e)
        return read_pos(self.client.recv(2048).decode())
