import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 8080))

client_socket.send("im client".encode("utf-8"))

recv_data = client_socket.recv(1024)

print("recv_data--->", recv_data.decode(encoding="utf-8"))

client_socket.close()