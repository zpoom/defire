import socket
import smbus
import time

#TODO
server_ip = '169.254.163.34'

address = 0x48
A0 = 0x40

THRESHOLD = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bus = smbus.SMBus(1)

server_address = (server_ip, 8080)

print('connecting to %s port %s' % server_address)

while True:
    bus.write_byte(address, A0)
    value = bus.read_byte(address)
    print(value)
    if value >= THRESHOLD:
        print('Warning', value)
        message = str.encode(str(value))
        sock.sendto(message, server_address)
    time.sleep(0.1)