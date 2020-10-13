import argparse

import tcp
import udp


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()

    PARSER.add_argument('ip', type=str)
    PARSER.add_argument('port', type=int)

    #for using connect() method in UDP regime
    PARSER.add_argument('-c', dest='use_connect', action='store_true')

    PARSER.add_argument('-r', dest='raw_socket', action='store_true')

    PARSER.add_argument('-s', dest='server', action='store_true')

    CONNECT_TYPE = PARSER.add_mutually_exclusive_group()
    CONNECT_TYPE.add_argument('-u', dest='udp_connect', action='store_true')
    CONNECT_TYPE.add_argument('-t', dest='tcp_connect', action='store_true')

    ARGS = PARSER.parse_args()

    HOST = ARGS.ip
    PORT = ARGS.port

    if ARGS.server:
        if ARGS.raw_socket:
            udp.raw_server(HOST, PORT)
        elif ARGS.udp_connect:
            udp.server(HOST, PORT)
        else:
            tcp.server(HOST, PORT)
    else:
        if ARGS.raw_socket:
            udp.raw_client(HOST, PORT)
        elif ARGS.use_connect:
            udp.connect_client(HOST, PORT)
        elif ARGS.udp_connect:
            udp.client(HOST, PORT)
        else:
            tcp.client(HOST, PORT)
