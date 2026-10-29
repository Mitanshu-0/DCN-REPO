import socket
# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Port number
port = 12345

# Bind the server to all available network interfaces
server.bind(('', port))

print("Socket successfully created")
print(f"Socket binded to {port}")

# Start listening
server.listen(5)

print("Socket is listening")

# Accept a client connection
client, addr = server.accept()

print("Got connection from", addr)

# Send message to client
client.send("Thank you for connecting".encode())

# Close connection
client.close()
server.close()





import socket

s = socket.socket()
s.bind(("0.0.0.0", 12345))
s.listen(1)

c, addr = s.accept()

with open("received.txt", "wb") as f:
    while True:
        data = c.recv(1024)
        if not data:
            break
        f.write(data)

print("File received successfully")
c.close()
s.close()
