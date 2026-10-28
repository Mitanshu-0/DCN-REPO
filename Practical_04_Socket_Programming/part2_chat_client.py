import socket

HOST = "127.0.0.1"  # Use server's LAN IP to chat between computers
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    while True:
        message = input("You: ")
        client.sendall(message.encode())
        if message.strip().lower() == "bye":
            break
        reply = client.recv(4096).decode()
        if not reply:
            break
        print("Server:", reply)
        if reply.strip().lower() == "bye":
            break
