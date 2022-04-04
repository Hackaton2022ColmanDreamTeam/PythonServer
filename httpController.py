import cgi
import logging
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.client
from io import BytesIO

import requests

# class Conteller:
#     def __init__(self,view,model):
#         self.View = view
#         self.Model = model
#         # self.commands = []
#         # for i in range(6):
#         #     self.commands[i] = i



class Server(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>HELLO WORLD</h1><body><html>", "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
        print(response.getvalue())

