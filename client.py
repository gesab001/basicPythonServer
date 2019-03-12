#This code demostrates the basics of HTTP request sent by a client, 
#and the response received from the server using TCP sockets.
#Here we demostrate the simple interaction between this client application,
# and google's web server.
#Execute this code with python v3

# Import the required libraries
from socket import *

# Address for the server
serverName = '127.0.0.1'

# Server's listening port
serverPort = 8090

# Create the socket object
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server at the specified port
clientSocket.connect((serverName,serverPort))

request = "GET /index.html HTTP/1.1\nHost:127.0.0.1:8080\n\n"

## Send the message
clientSocket.send(request.encode())

## Receive the reply
response = clientSocket.recv(1024)

# For print the response
print('From Server:', response)

# Close the socket
clientSocket.close() 

