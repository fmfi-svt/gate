#!/usr/bin/env python
"""
Gate server runner -- https://github.com/fmfi-svt/gate/wiki/Architecture#server
"""

import server
import os
from socketserver import ThreadingMixIn, UDPServer

class ThreadingUDPServer(ThreadingMixIn, UDPServer): pass

def main():
    server.MessageHandler.set_db(os.environ.get('DB_URL'))
    srv_addr = os.environ.get('HOST', 'localhost'), int(os.environ.get('PORT'))
    srv = ThreadingUDPServer(srv_addr, server.MessageHandler)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye')

if __name__ == '__main__':
    sys.exit(main())
