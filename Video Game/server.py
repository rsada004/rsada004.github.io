import os
import http.server
import socketserver

ip = '0.0.0.0'
port = 8080

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer((ip, int(port)), Handler)

print(f"serving at port {port}")
httpd.serve_forever()