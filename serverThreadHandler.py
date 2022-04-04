from http.server import HTTPServer
from threading import Thread
import httpController

class threadHandler(Thread):
    def __init__(self, port):
        Thread.__init__(self)
        self.PORT = port

    def run(self):
        HOST = "127.0.0.1"
        server = HTTPServer((HOST, self.PORT), httpController.Server)
        server.serve_forever()
        server.server_close()
