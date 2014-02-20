#!/usr/bin/env python
# encoding: utf-8
import socket
serverAddress = ('', 51423)
serverSocket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#serverSocket.setblocking(0)
serverSocket.bind(serverAddress)
serverSocket.listen(1)
while True:
    clientSocket, clientAddress = serverSocket.accept()
    print 'Connected by :',clientSocket.getpeername()
    while True:
        date = clientSocket.recv(1024)
        if not len(date):
            break
        print 'server received data: ', date
        #date = 'xxx'
        #clientSocket.send(date,clientAddress)
        clientSocket.send(date)
        print 'server send date:',date
