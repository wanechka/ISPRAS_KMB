from __future__ import print_function

import socket as sk


def server(host, port):
    server_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

    server_socket.bind((host, port))
    server_socket.listen(1)

    while True:
        (connection_socket, addr) = server_socket.accept()

        print('request from host:', addr)
        resp_msg = f'{addr[0]}:{addr[1]}'
        connection_socket.sendall(resp_msg.encode())

        connection_socket.close()


def client(host, port):
    client_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    client_socket.connect((host, port))

    message = client_socket.recv(2048)
    print(message.decode())

    client_socket.close()
