import socket

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server IP address and port
host = '10.158.235.151'
port = 40674

# Bind server
server.bind((host, port))

# Listen for client
server.listen(1)

print(f"Server listening on {host}:{port}...")

# Accept client connection
client, addr = server.accept()

print(f"Connection established with {addr}")

# Receive file name
filename = client.recv(1024).decode()

print(f"Receiving file: {filename}")

# Open file to write received data
with open("received_" + filename, "wb") as file:

    while True:
        data = client.recv(1024)

        if not data:
            break

        file.write(data)

print("File received successfully.")

# Close connection
client.close()
server.close()
