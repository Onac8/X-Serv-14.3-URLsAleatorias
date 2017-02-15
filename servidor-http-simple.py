#!/usr/bin/python3

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostname(), 1234))
# We can bind to "localhost:1234", but that way is chic"

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)
try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        URL = random.randint(0, 1000)
        print('HTTP request received:')
        print(recvSocket.recv(2048))
        print ('Answering back...')
        recvSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n' +
            '<html><body><p><a href=' + str(URL) + '>Dame otra!'+
            '</a></p></body></html>' + '\r\n', 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()
