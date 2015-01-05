import socketserver

class MessageHandler(socketserver.BaseRequestHandler):
    """
    Handles a message from the controller, according to
    https://github.com/fmfi-svt/gate/wiki/Controller-%E2%86%94-Server-Protocol .

    Note: the server is completely stateless.
    """

    def handle(self):
        data, socket = self.request
        print("Received data from {}:".format(self.client_address))
        print(data)
        socket.sendto(data, self.client_address)
