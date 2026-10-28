import socket

HOST = "127.0.0.1"  # Replace with server's LAN IP when using two computers
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print(client.recv(1024).decode())
