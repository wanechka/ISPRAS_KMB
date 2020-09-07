from socket import *
import sys

#print("Enter host IP or type")
#host = input()

host = sys.argv[2]
port = int(sys.argv[3])

if "-s" in sys.argv:
    serverSocket = socket(AF_INET, SOCK_STREAM)



    serverSocket.bind(('', port))
    serverSocket.listen(1)

    while 1:
        connectionSocket, addr = serverSocket.accept()
        if addr[0] == host:
            print("request from host:", addr)
            connectionSocket.sendall((str(addr[0]) + ':' + str(addr[1])).encode())

    connectionSocket.close()

if "-c" in sys.argv:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((host, port))

    message = clientSocket.recv(2048)
    print(message.decode())
    clientSocket.close()

