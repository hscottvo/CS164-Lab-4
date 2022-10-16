import socket
import sys
from _thread import *
from datetime import datetime

HOST = ''
PORT = 9822

i = 0
connection_dict = {}

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


def clientthread(conn, num: int):
    conn.send(b"Welcome to the server. Type something and hit enter\n")

    while True:
        data = conn.recv(1024)

        if data.startswith(b"!q"):
            del connection_dict[num]
            break
        elif data.startswith(b'!sendall '):
            now = datetime.now()
            reply = now.strftime("%H:%M:%S").encode('utf-8') + b': ' + data.lstrip(b'!sendall ')
            for connection in connection_dict.values():
                connection.sendall(reply)
        else:
            now = datetime.now()
            reply = now.strftime("%H:%M:%S").encode('utf-8') + b": OK..." + data
            if not data:
                break

            conn.sendall(reply)
    conn.close()
while True:
    conn, addr = s.accept()
    connection_dict[i] = conn
    print(f"Connected with {addr[0]}: {str(addr[1])}")

    start_new_thread(clientthread, (conn, i,))
    i += 1

s.close()