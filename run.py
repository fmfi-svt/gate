#!/usr/bin/env python
"""
Gate server runner -- https://github.com/fmfi-svt/gate/wiki/Architecture#server
"""

import server
import config

import sys
from socketserver import ThreadingMixIn, UDPServer

class ThreadingUDPServer(ThreadingMixIn, UDPServer): pass

def main():
    srv = ThreadingUDPServer((config.HOST, config.PORT), server.MessageHandler)
    srv.serve_forever()

if __name__ == '__main__':
    sys.exit(main())
