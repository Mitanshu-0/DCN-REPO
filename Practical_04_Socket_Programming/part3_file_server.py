import socket
from pathlib import Path

HOST = "0.0.0.0"
PORT = 40674
OUTPUT_DIR = Path("received_files")
OUTPUT_DIR.mkdir(exist_ok=True)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Server listening on {HOST}:{PORT}...")
    conn, addr = server.accept()
    with conn:
        print(f"Connection established with {addr}")
        with conn.makefile("rb") as stream:
            filename = Path(stream.readline().decode().strip()).name
            if not filename:
                raise ValueError("Missing filename")
            target = OUTPUT_DIR / ("received_" + filename)
            with target.open("wb") as output:
                while chunk := stream.read(65536):
                    output.write(chunk)
            print(f"File received successfully: {target}")
