import socket;


#creating a client socket object
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# defing host and port of server
server_host = "127.0.0.1"
server_port = 9090


# coonecting to the server 
client_sock.connect((server_host, server_port))
print("connection has been established")

# send the data to the server
client_sock.sendall(bytes("Hello from the Client side ".encode("utf-8")))

#recieve the data from the server side 
recieve_data = client_sock.recv(1024)
print("Data received from server"+str(recieve_data))

#close the client socket
client_sock.close()


