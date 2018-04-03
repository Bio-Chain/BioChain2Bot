#!/usr/bin/python

import socket
import sys

def sendToServer(data):
    #TODO Better port/host input
    port = 12345
    host = socket.gethostname()
    server = socket.socket()
    server.connect((host, port))
    server.send(data)
    response = server.recv(1024)
    server.close()
    return response

if __name__ == "__main__":
    print sendToServer(' '.join(sys.argv[1:]))
