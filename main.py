import socket
import sys

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("Failed to create socket. Error code: " + str(msg[0]) + 
          ", Error message: " + msg[1])

print("Socket created")

host = 'www.google.com'
port = 80

try: 
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("Hostname could not resolve. Exiting")
    sys.exit()
print(f'Ip address of {host} is {remote_ip}')

s.connect((remote_ip, port))

print(f'Socket connected to {host} on ip {remote_ip}')

message = b'GET / HTTP/1.1\r\n\r\n'

try:
    s.sendall(message)
except socket.error:
    print('Send failed')
    sys.exit()

print('Message send successfully')