import socket

#create a socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(False)
#set option reused
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR  , 1)

server_address= ('',10001)
server.bind(server_address)

server.listen(10)
while True:
    connection, client_address = server.accept()
    print "    connection from ", client_address

