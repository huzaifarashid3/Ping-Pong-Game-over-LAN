import socket


class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "172.21.122.101"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)
        for i in range(10):
            print(self.send(str(i)))

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
        except:
            pass
        return self.client.recv(2048).decode()


n = Network()
