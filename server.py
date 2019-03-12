#Here is a skeleton code you may use as a starting point.
#This is a very basic HTTP server which listens on port 8080,
#and serves the same response messages regardless of the browser's request.
#It runs on python v3
#Usage: execute this program, open your browser (preferably chrome) and type
#http://servername:8080
#e.g. if server.py and browser are running on the same machine, then use http://localhost:8080
# Import the required libraries
from socket import *
import threading

# Listening port for the server
serverPort = 8080
# Create the server socket object
serverSocket = socket(AF_INET,SOCK_STREAM)
# Bind the server socket to the port
serverSocket.bind(('',serverPort))
# Start listening for new connections
serverSocket.listen(1)
print('The server is ready to receive messages')

def getHTTPMethodType(string):
    stringsplit = string.split(" ")
    method = stringsplit[0]
    return method

def getRequestedFile(string):
    stringsplit = string.split(" ")
    file = stringsplit[1][1:]
    return file

while 1:
# Accept a connection from a client
    connectionSocket, addr = serverSocket.accept()
    ## Retrieve the message sent by the client
    request = connectionSocket.recv(1024)
    stringRequest = request.decode("utf-8")
    # print(getRequestedFile(stringRequest))
    httpMethod = getHTTPMethodType(stringRequest)
    if httpMethod=="GET":
       #extracts filename from the GET request
       filename = getRequestedFile(stringRequest)
       try:
            file = open(filename, "rb")
            result = file.read()
            response = result
            connectionSocket.send('HTTP/1.1 200 OK\n'.encode())
            if (filename.endswith("html")):
               connectionSocket.send('Content-Type: text/html\n\n'.encode())
               connectionSocket.send(response)
            if (filename.endswith("jpg")):
                connectionSocket.send('Content-Type: image/jpeg\n\n'.encode())
                connectionSocket.send(response)
       except FileNotFoundError as e:
           print (e)
           response = "HTTP 404 - Not Found"
           connectionSocket.send(response.encode())

    # Close the connection
    connectionSocket.close()

