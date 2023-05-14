import socket


class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "172.21.122.101"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        self.pos = "10,11"

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            print("failed")
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
        except socket.error as e:
            print(e)
        return self.client.recv(2048).decode()

    def getPos(self):
        return self.pos
