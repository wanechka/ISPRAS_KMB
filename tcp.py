from socket import *

def server_tcp(host, port):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    
    serverSocket.bind(('', port))
    serverSocket.listen(1)
    
    while 1:
        connectionSocket, addr = serverSocket.accept()
        
        if addr[0] == host:
                print("request from host:", addr)
                
                resp_msg = f'{addr[0]}:{addr[1]}'
                connectionSocket.sendall(resp_msg.encode())
                
                connectionSocket.close()
            


def client_tcp(host, port):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((host, port))
    
    message = clientSocket.recv(2048)
    print(message.decode())
    
    clientSocket.close()

