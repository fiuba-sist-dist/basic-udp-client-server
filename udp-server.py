from socket import *

BUFFER_SIZE = 2048

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

print("Listening packets on port", serverPort)

while (True):
    sentence, clientAddr = serverSocket.recvfrom(BUFFER_SIZE)
    print("Received from client {}:{} ->".format(clientAddr[0], clientAddr[1]), sentence.decode())
    serverSocket.sendto(sentence.decode().upper().encode(), clientAddr)