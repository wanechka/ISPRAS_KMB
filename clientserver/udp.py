import socket as sk


def server(host, port):
    server_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    server_socket.bind((host, port))

    while 1:
        (message, addr) = server_socket.recvfrom(2048)

        print('Message from ', f'{addr[0]}:{addr[1]}')
        print('Message text: ', message)
        resp_msg = f'{addr[0]}:{addr[1]}'
        server_socket.sendto(resp_msg.encode(), (addr[0], addr[1]))


def client(host, port):
    client_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    message = input('Input lowercacketse sentence:')
    client_socket.sendto(message.encode(), (host, port))

    answer_message = client_socket.recv(2048)
    print('My address is ', answer_message.decode())

    client_socket.close()
