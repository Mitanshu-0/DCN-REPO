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
