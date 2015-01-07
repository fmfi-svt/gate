#!/usr/bin/env python

import socket, sys

BUF_SZ = 1024

def message(addr, data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host, port = addr.split(':')
    sock.sendto(data, (host, int(port)))
    reply = sock.recv(BUF_SZ)
    return reply

if __name__ == '__main__':
    print(message(sys.argv[1], bytes(sys.argv[2], 'utf-8')))
