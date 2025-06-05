from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Odpowiedź 200 OK
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Witaj ze zwyklego serwera HTTP!")

# Konfiguracja serwera
def run():
    server_address = ("localhost", 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Serwer HTTP dziala na http://localhost:8000")
    httpd.serve_forever()

run()
