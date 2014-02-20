#!/usr/bin/env python
# encoding: utf-8
import socket
import select
import Queue

serverAddress = ('', 51423)
serverSocket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#serverSocket.setblocking(0)
serverSocket.bind(serverAddress)
serverSocket.listen(1)

#sockets from which we except to read
inputs = [serverSocket]

#sockets from which we expect to write
outputs = []

#Outgoing message queues (socket:Queue)
message_queues = {}

#A optional parameter for select is TIMEOUT
timeout = 20

while inputs:
    print "waiting for next event:"
    readables, writables, exceptionals = select.select(inputs, outputs, inputs, timeout)
    if not (readables or writables or exceptionals):
        print "Time out"
    for readable in readables:
        if readable is serverSocket:
            #A "readable" socket is ready to accept a connection
            client_socket, client_address = readable.accept()
            print "     connection from ,", client_address
            client_socket.setblocking(0)
            inputs.append(client_socket)
            message_queues[client_socket] = Queue.Queue()
        else:
            data = readable.recv(1024)
            if data:
                print "received ",data, "from ", readable.getpeername()
                message_queues[readable].put(data)
                # Add output channel for response
                if readable not in outputs:
                    outputs.append(readable)
            else:
                #Interpret empty result as closed connection
                print " closing", client_address
                if readable in outputs :
                    outputs.remove(readable)
                inputs.remove(readable)
                readable.close()
                #remove message queue
                del message_queues[readable]
    for writable in writables :
        try:
            next_msg = message_queues[writable].get_nowait()
        except Queue.Empty :
            print " ",writable.getpeername(), 'queue empty'
            outputs.remove(writable)
        else:
            print ' sending ', next_msg , ' to ', writable.getpeername()
            writable.send(next_msg)
    for exceptional in exceptionals :
        print ' exceptionals condition on ', exceptional.getpeername()
        #stop lisening for input on the connection
        inputs.remove(exceptional)
        if exceptional in outputs :
            outputs.remove(exceptional)
        exceptional.close()
        #Remove message queue
        del message_queues[exceptional]
