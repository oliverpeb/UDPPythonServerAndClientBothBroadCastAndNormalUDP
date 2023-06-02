from socket import *

serverName = 'localhost'
serverPort = 4536
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverAddress = ('', serverPort)

webcamData = []

serverSocket.bind(serverAddress)
print('The server is ready')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Received message:" + message.decode())

    webcamData.append(message.decode())

    serverSocket.sendto(str(webcamData).encode(), clientAddress)


