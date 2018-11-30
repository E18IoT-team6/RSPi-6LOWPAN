#!/usr/bin/python3

import socket
from subprocess import PIPE, Popen
import pyshark

HOST = ''    # Symbolic name meaning all available interfaces
PORT = 1500  # Arbitrary port


def get_cpu_temperature():
    """Function to get the temperature of the CPU"""
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return output


def main():
    # specify the IPv6 "scope id"
    scope_id = socket.if_nametoindex('lowpan0')
    # Create the socket with a INET6 network
    s6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
    # Bind the socket to address
    s6.bind((HOST, PORT, 0, scope_id))
    # Enable the server to accept connections.
    s6.listen(1)

    cap = pyshark.LiveCapture(interface='lowpan0')

    cap.sniff(packet_count=5)

    print("Tamano cap:", len(cap))

    while True:
        # Accept a connection.
        # Return (conn, address)
        # conn is a new socket object usable to send and receive data on the connection,
        # address is the address bound to the socket on the other end of the connection.
        conn, addr = s6.accept()
        # Send data to the socket
        conn.send(get_cpu_temperature())
        # Mark the socket closed
        print("Tamano cap:", len(cap))
        conn.close()



if __name__ == '__main__':
    main()
