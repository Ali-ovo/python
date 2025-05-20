import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

tcp_socket.bind(("127.0.0.1", 8080))

print(f"listen: {8080}")
tcp_socket.listen()

conn_socket, client_addr = tcp_socket.accept()
print("client_addr", client_addr)

data = conn_socket.recv(1024)

print("data--->", data.decode(encoding="utf-8"))
conn_socket.send("hello".encode("utf-8"))

conn_socket.close()

tcp_socket.close()
