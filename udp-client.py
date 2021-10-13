from socket import *

BUFFER_SIZE = 2048

serverName = "127.0.0.1"
serverPort = 12000

sentence = input("Input lowercase sentence: ")

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(sentence.encode(), (serverName, serverPort))

modifiedSentence, serverAddress = clientSocket.recvfrom(BUFFER_SIZE)
print("Received from server {}:{} ->".format(serverAddress[0], serverAddress[1]), modifiedSentence.decode())

clientSocket.close()