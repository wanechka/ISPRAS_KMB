import socket as sk
import struct

UHL = 8
IHL = 20

S2C_MARKER = 'SERVER2CLIENTRESPONSEMARKER'
S2C_LENGTH = len(S2C_MARKER)

C2S_MARKER = 'CLIENT2SERVERSENDINGMARKER'
C2S_LENGTH = len(C2S_MARKER)

def server(host, port):
    server_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    server_socket.bind((host, port))

    while True:
        (message, addr) = server_socket.recvfrom(2048)

        print('Message from ', f'{addr[0]}:{addr[1]}')
        print('Message text: ', message)
        resp_msg = f'{addr[0]}:{addr[1]}'
        server_socket.sendto(resp_msg.encode(), (addr[0], addr[1]))



def client(host, port):
    client_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    message = input('Input your sentence:')
    client_socket.sendto(message.encode(), (host, port))

    answer_message = client_socket.recv(2048)
    print('My address is ', answer_message.decode())

    client_socket.close()



def connect_client(host, port):
    client_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    client_socket.connect((host, port))
    message = input('Input your sentence:')
    client_socket.send(message.encode())

    answer_message = client_socket.recv(2048)
    print('My address is ', answer_message.decode())

    client_socket.close()



def raw_server(host, port):
    server_socket = sk.socket(sk.AF_INET, sk.SOCK_RAW, sk.IPPROTO_UDP)
    server_socket.bind((host, port))
    while True:
        (message, addr) = server_socket.recvfrom(2048)

        if message[IHL + UHL:IHL + UHL + C2S_LENGTH] == C2S_MARKER.encode():
            print('Message from ', f'{addr[0]}:{addr[1]}')
            print('Message text: ', message[IHL + UHL + C2S_LENGTH:].decode())
            data = S2C_MARKER + f'{addr[0]}:{addr[1]}'
            data = data.encode()
            dest_port = addr[1]
            source_port = port
            checksum = 0
            length = UHL + len(data)
            udp_header = struct.pack('!HHHH', source_port, dest_port, length, checksum)
            server_socket.sendto(udp_header + data, (addr[0], addr[1]))
            #break



def raw_client(host, port):
    client_socket = sk.socket(sk.AF_INET, sk.SOCK_RAW, sk.IPPROTO_UDP)
    source_port = client_socket.getsockname()[1]
    print("Current port of client side is ", source_port)

    data = C2S_MARKER + input('Input your message, please ')
    data = data.encode()

    dest_port = port
    length = UHL + len(data)
    checksum = 0
    udp_header = struct.pack('!HHHH', source_port, dest_port, length, checksum)

    client_socket.sendto(udp_header + data, (host, port))
    while True:
        message = client_socket.recv(2048)
        if message[IHL + UHL: IHL + UHL + S2C_LENGTH] == S2C_MARKER.encode():
            print("My address is: ", (message[IHL + UHL + S2C_LENGTH:]).decode())
            break
