import socket
from _thread import *
from helper_functions import *


class Server():
    def __init__(self, ip="172.21.122.101", port=5555):
        self.ip = ip
        self.port = port

    def initiate(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.bind((self.ip, self.port))
        except socket.error as e:
            print(e)
        self.s.listen(1)
        print("waiting for connections...")
        while True:
            self.conn, self.addr = self.s.accept()
            print("Connected to ", self.addr)
            start_new_thread(threaded_client, (self.conn))

    def send(self, data):
        try:
            self.conn.send(str.encode(make_pos(data)))
        except socket.error as e:
            print(e)
        return read_pos(self.conn.recv(2048).decode())


def threaded_client(conn):
    conn.send(str.encode(pos))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("disconnected Player")
                break
            else:
                print("recieved", reply)
                print("sending", reply)

            conn.sendall(str.encode(reply))
        except:
            break
    print("lost connection...")
    conn.close()
