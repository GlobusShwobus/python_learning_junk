
from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import sys

HOST = input("Enter IP: ")
PORT = int(input("Enter port num: "))

class NHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers();

        self.wfile.write(bytes("<html><body><h1>I AM THEREFOR I THINK</h1></body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "'+date+'"}',"utf-8"))


try:
    server = HTTPServer((HOST, PORT), NHTTP)
except Exception as e:
    print(f"\nFailed to start server on {HOST}:{PORT}")
    print(f"error: {e}")
    sys.exit(1)

print(f"server on {HOST}:{PORT}...")

try:
    server.serve_forever()

except KeyboardInterrupt:
    print("\nShitting down server")
    server.server_close()