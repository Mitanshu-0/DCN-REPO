import socket

HOST = "0.0.0.0"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Chat server listening on {HOST}:{PORT}")
    conn, address = server.accept()
    with conn:
        print("Connected:", address)
        while True:
            message = conn.recv(4096).decode()
            if not message or message.strip().lower() == "bye":
                break
            print("Client:", message)
            reply = input("You: ")
            conn.sendall(reply.encode())
            if reply.strip().lower() == "bye":
                break
