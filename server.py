import socketserver
import psycopg2


class MessageHandler(socketserver.BaseRequestHandler):
    """Handles a message from the controller.
    
    Behaves according to
    https://github.com/fmfi-svt/gate/wiki/Controller-%E2%86%94-Server-Protocol .
    """

    _db_conn = None

    @classmethod
    def set_db(cls, db_conf):
        """Connects to the database. All instances will share the connection."""
        cls._db_conn   = psycopg2.connect(db_conf)

    def handle(self):
        data, socket = self.request
        print("Received data from {}:".format(self.client_address))
        print(data)

        cur = self._db_conn.cursor()
        cur.execute("SELECT * FROM controllers;")
        print(cur.fetchall())
        cur.close()

        socket.sendto(data, self.client_address)
