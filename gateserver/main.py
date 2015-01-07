"""
Gate server runner -- https://github.com/fmfi-svt/gate/wiki/Architecture#server
"""

from socketserver import ThreadingUDPServer
import os, sys
from .messagehandler import MessageHandler

def serve():
    MessageHandler.set_db(os.environ.get('DB_URL'))
    bind_addr = os.environ.get('HOST', 'localhost'), int(os.environ.get('PORT'))
    server = ThreadingUDPServer(bind_addr, MessageHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye')

if __name__ == '__main__':
    sys.exit(serve())
