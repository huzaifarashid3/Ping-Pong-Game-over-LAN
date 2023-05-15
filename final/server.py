import socket
from _thread import *
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

        # start_new_thread(self.threaded_client)

    def send(self, data=(30, 20, 100, 400, 0, 0)):
        try:
            self.conn.sendall(str.encode(make_pos(data)))
            print(make_pos(data))
        except:
            pass

    def rvc(self):
        try:
            return read_pos(self.conn.recv(2048).decode())
        except:
            print("rcv failed")
            return (300, 300, 400, 400, 0, 0)

    def threaded_client(self):

        while True:
            continue

        self.conn.close()
        pass
