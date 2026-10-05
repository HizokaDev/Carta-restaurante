import http.server
import socketserver
import os

CARPETA = "/storage/emulated/0/carta-restaurante"

os.chdir(CARPETA)

PUERTO = 8000

servidor = socketserver.TCPServer(
    ("0.0.0.0", PUERTO),
    http.server.SimpleHTTPRequestHandler
)

print("Servidor iniciado")
print("Abre en Chrome:")
print("http://127.0.0.1:8000")

servidor.serve_forever()