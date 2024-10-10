#!/usr/bin/python3
"""Module task_03_http_server: Define
Develop a simple API using python with the http.server"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import http.server

PORT = 8000


class ApiRequestHandler(BaseHTTPRequestHandler):
    """Handle HTTP request"""

    def do_GET(self):
        """Handle GET request by checking the requested path and sending
        appropiate responses"""

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode('utf-8'))

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


if __name__ == "__main__":
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, ApiRequestHandler)
    print(f'Serving on port {PORT}...')
    httpd.serve_forever()
