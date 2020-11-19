import socket
import sys

#TODO
server_ip = '169.254.163.34'

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except err:
    print('err', err)
    
server_address = (server_ip, 8080)

print('starting up on %s port %s' % server_address)

sock.bind(server_address)

while True:
    data, addr = sock.recvfrom(1024)
    print('received message: ', data)
    