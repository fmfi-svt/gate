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
    server.MessageHandler.set_db(config.DB)
    srv = ThreadingUDPServer((config.HOST, config.PORT), server.MessageHandler)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye')

if __name__ == '__main__':
    sys.exit(main())
