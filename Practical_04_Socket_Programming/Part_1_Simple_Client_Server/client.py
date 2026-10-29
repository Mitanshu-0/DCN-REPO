import socket

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server port
port = 12345

# Connect to the server running on this computer
client.connect(('127.0.0.1', port))

# Receive message from server
print(client.recv(1024).decode())

# Close connection


import socket

s = socket.socket()
s.connect(("127.0.0.1", 12345))

with open("sample.txt", "rb") as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        s.sendall(data)

print("File sent successfully")
s.close()
