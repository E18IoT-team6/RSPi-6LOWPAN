#!/usr/bin/python3

import socket
import time

ADDR = '2001:db8::1' # Server RPi
PORT = 1500

def main():
    # specify the IPv6 "scope id"
    scope_id = socket.if_nametoindex('lowpan0')
    while True:
        # Create the socket with a INET6 network
        s6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
        # Bind the socket to address
        s6.connect((ADDR, PORT, 0, scope_id))
        # Receive data from the socket. The return value is a bytes object representing the data received.
        data = s6.recv(1024)

        # Print the data
        print(data.decode('utf-8'), end='')

        # get it again after 5 seconds
        time.sleep(5)

if __name__ == '__main__':
    main()