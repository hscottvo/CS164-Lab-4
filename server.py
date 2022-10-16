import socket
import sys
from _thread import *

HOST = ''
PORT = 9822

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print(f'Bind failed. Error code: {str(msg[0])} Message: {msg[1]}')
    sys.exit()

print("Socket bind complete")

s.listen(10)
print('Socket now listening')


def clientthread(conn):
    conn.send(b"Welcome to the server. Type something and hit enter\n")

    while True:
        data = conn.recv(1024)
        reply = b"OK..." + data
        if not data:
            break

        conn.sendall(reply)
    conn.close()

while True:
    conn, addr = s.accept()

    print(f"Connected with {addr[0]}: {str(addr[1])}")

    start_new_thread(clientthread, (conn,))

s.close()