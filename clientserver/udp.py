import socket as sk


def server(host, port):
    serverSocket = socket(sk.AF_INET, sk.SOCK_DGRAM)
    serverSocket.bind((host, port))

    while 1:
        (message, addr) = socket.recvfrom(2048)

        print ('Message from ', f'{addr[0]}:{addr[1]}')


def client(host, port):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = input('Input lowercase sentence:')
    clientSocket.sendto(message.encode(), (host, port))

    clientSocket.close()

