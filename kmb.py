from socket import *

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("ip", type=str)
parser.add_argument("port", type=int)

parser.add_argument("-s", dest="server", action="store_true")
parser.add_argument("-c", dest="client", action="store_true")

args = parser.parse_args()

host = args.ip
port = args.port

if args.server:
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(('', port))
    serverSocket.listen(1)

    while 1:
        connectionSocket, addr = serverSocket.accept()
        if addr[0] == host:
            print("request from host:", addr)
	    resp_msg = f'{add[0]}:{addr[1]}'
            connectionSocket.sendall(resp_msg.encode())

    connectionSocket.close()

if args.client:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((host, port))

    message = clientSocket.recv(2048)
    print(message.decode())
    clientSocket.close()


# main          (!)
# decomposition (!)

