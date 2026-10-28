import socket
from pathlib import Path

HOST = "127.0.0.1"  # Use server's LAN IP on a different computer
PORT = 40674
FILE_PATH = Path("sample.txt")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print("Connected to server")
    client.sendall((FILE_PATH.name + "\n").encode())
    with FILE_PATH.open("rb") as source:
        while chunk := source.read(65536):
            client.sendall(chunk)
    print("File sent successfully")
