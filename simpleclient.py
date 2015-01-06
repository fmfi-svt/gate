#!/usr/bin/env python

import config

import socket, sys

BUF_SZ = 1024

def message(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data, (config.HOST, config.PORT))
    reply = sock.recv(BUF_SZ)
    return reply

if __name__ == '__main__':
    print(message(bytes('Hello World!', 'utf-8')))
