#!/usr/bin/env python
# encoding: utf-8

import socket
import sys
#import os
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#clientSocket.setbocking(0)
serverAddress = ('', 51423)
clientSocket.connect(serverAddress)

while True:
    """
    简单的socket 应答测试

    """
    #date = sys.argv[1]
    print "输入要发送的内容，按回车键："
    date = sys.stdin.readline()
    if not len(date):
        break
    clientSocket.send(date)
    print 'send date:',date,
    dateReci = clientSocket.recv(1024)
    print 'received date:', dateReci,

