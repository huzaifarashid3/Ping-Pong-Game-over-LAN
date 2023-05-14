import socket
from _thread import *
from helper_functions import *


server = "172.21.122.101"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)

print("waiting for connections...")


pos = [(20, 20), (100, 20)]


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("disconnected Player ", player)
                break
            else:
                print("recieved", reply)
                print("sending", reply)

            conn.sendall(str.encode(reply))
        except:
            break
    print("lost connection...")
    conn.close()


currentPlayer = 0


while True:
    conn, addr = s.accept()

    print("Connected to ", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
