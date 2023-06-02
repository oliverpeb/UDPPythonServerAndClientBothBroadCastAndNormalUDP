from socket import *

serverPort = 4536
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Uncomment the following lines for broadcast UDP communication
# clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# serverAddress = ('<broadcast>', serverPort)

# Comment out the following line for broadcast UDP communication
serverAddress = ('localhost', serverPort)

while True:
    message = input("Enter webcam data: ")

    # Send the message to the server
    clientSocket.sendto(message.encode(), serverAddress)

    # Receive the response from the server
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    # Print the updated list received from the server
    print("Updated webcam data:", modifiedMessage.decode())

clientSocket.close()
