#!/usr/bin/python3

import socket
from subprocess import PIPE, Popen

HOST = ''    # Symbolic name meaning all available interfaces
PORT = 2016  # Arbitrary non-privileged port

def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return output

def main():
    s6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
    scope_id = socket.if_nametoindex('lowpan0')
    s6.bind((HOST, PORT, 0, scope_id))
    s6.listen(1)

    while True:
        conn, addr = s6.accept()
        conn.send(get_cpu_temperature())
        conn.close()

if __name__ == '__main__':
    main()
    