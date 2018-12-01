#!/usr/bin/python3

import socket
import time
import pyshark

ADDR = '2001:db8::2'  # Sensor RPi
PORT = 1500


def main():
    # specify the IPv6 "scope id"
    # scope_id = socket.if_nametoindex('lowpan0')

    print("Waiting for packets")

    cap = pyshark.LiveCapture(interface='lowpan0')
        
    cap.sniff(packet_count=5)

    pac_1 = cap[0]

    print(pac_1.layers)

    # while True:

    #     print("Size cap:", len(cap))

        # cap.apply_on_packets(print_sources_data, timeout=100t)

        # for pkt in cap:
            # print('NO:', pkt.number)
        #     print('Frame Info', pkt.frame_info)
        #     print('\n')
            # print('Length', pkt.length)
            # print('Captured Length', pkt.captured_length)
            # print('sniff_time', pkt.sniff_time)
            # print('\n')


def print_sources_data(pkt):
    src_addr = pkt.ip.src
    dst_addr = pkt.ip.dst
    print('%s --> %s' % (src_addr, dst_addr))

    #     cap.sniff(packet_count=5)
    #     print("Tamano cap:", len(cap))
    # Create the socket with a INET6 network
    # s6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
    # Bind the socket to address
    # s6.connect((ADDR, PORT, 0, scope_id))
    # Receive data from the socket. The return value is a bytes object representing the data received.
    # data = s6.recv(1024)

    # Print the data
    # print(data.decode('utf-8'), end='')

    # get it again after 5 seconds


if __name__ == '__main__':
    main()
