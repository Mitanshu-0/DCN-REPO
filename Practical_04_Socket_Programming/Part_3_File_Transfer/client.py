import socket
import os

# Server IP address and port
host = '10.158.235.151'
port = 40674

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect((host, port))

print("Connected to server.")

# File to send
filename = "sample.txt"

# Send file name
client.send(filename.encode())

# Open file in binary mode
with open(filename, "rb") as file:

    while True:
        data = file.read(1024)

        if not data:
            break

        client.send(data)

print("File sent successfully.")

# Close connection
client.close()
