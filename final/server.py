import socket
from _thread import *
from helper_functions import *


class Server():
    def __init__(self, ip="172.21.122.101", port=5555):
        self.ip = ip
        self.port = port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
            self.s.bind((self.ip, self.port))
            self.s.listen(1)

        print("waiting for connections...")

        self.conn, self.addr = self.s.accept()
        with self.conn:
            print("Connected to ", self.addr)

    def send_n_rcv(self, data):
        with self.conn:
            self.conn.sendall(str.encode(make_pos(data)))
            return read_pos(self.conn.recv(2048).decode())
