import socket as sk


def server(host, port):
    serverSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    
    serverSocket.bind((host, port))
    serverSocket.listen(1)
    
    while True:
        connectionSocket, addr = serverSocket.accept()
        
        print("request from host:", addr)
        resp_msg = f'{addr[0]}:{addr[1]}'
        connectionSocket.sendall(resp_msg.encode())

        connectionSocket.close()
            


def client(host, port):
    clientSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    clientSocket.connect((host, port))
    
    message = clientSocket.recv(2048)
    print(message.decode())
    
    clientSocket.close()

