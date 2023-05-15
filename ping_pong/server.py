import socket
from helper_functions import *


class Server():
    def __init__(self, ip="localhost", port=5555):
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.bind((self.ip, self.port))
        except:
            pass
        self.s.listen(1)

        print("waiting for connections...")

        self.conn, self.addr = self.s.accept()

        print("Connected to ", self.addr)

    def send(self, data=(0, 0, 0, 0, 0, 0, 0, 0)):
        try:
            self.conn.sendall(str.encode(make_pos(data)))
            print("sending " + make_pos(data))
        except:
            pass

    def rcv(self):
        try:
            data = read_pos(self.conn.recv(2048).decode())
            print("recieved " + make_pos(data))
            return data
        except:
            print("rcv failed")
            return (0, 0, 0, 0, 0, 0, 0, 0)
