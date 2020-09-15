from socket import *


def server(host, port):
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', port))

    while 1:
        message, addr = serverSocket.recvfrom(2048)
    
        print("Message from ", f'{addr[0]}:{addr[1]}')


def client(host, port):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    
    message = input('Input lowercase sentence:')
    clientSocket.sendto(message.encode(),(host, port))

    clientSocket.close()
