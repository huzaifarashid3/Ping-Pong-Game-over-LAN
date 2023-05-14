import socket
import sys
from _thread import *

server = "172.21.122.101"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)

print("waiting for connections...")


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("disconnected...")
                break
            else:
                print("recieved", reply)
                print("sending", reply)

            conn.sendall(str.encode(reply))
        except:
            break
    print("lost connection...")
    conn.close()


while True:
    conn, addr = s.accept()

    print("Connected to ", addr)
    start_new_thread(threaded_client, (conn,))