import socket ; 


# create a server_socket object
server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# create a host and port for the server 
server_host = "127.0.0.1"
server_port = 9090


# bind the server_sock object to host and port
server_sock.bind((server_host,server_port))
print("binding has been done and waiting for the req")

#serve start listing to the req
server_sock.listen()

# accet the req from client 
connection , address = server_sock.accept()
print("recieved the req from client ")

# reciev the data from the client 
recieve_data = connection.recv(1024)
print("Data received from client " + str(recieve_data))


#send the response to the  client 
connection.sendall(bytes("Hello from the server side ".encode("utf-8")))
print("res send to client closing connection")


#close the server socket
server_sock.close()




