import socket

HOST = "0.0.0.0"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    print("Socket successfully created")
    print(f"Socket binded to {PORT}")
    server.listen(1)
    print("Socket is listening")
    client, addr = server.accept()
    with client:
        print("Got connection from", addr)
        client.sendall(b"Thank you for connecting")
