import argparse

import tcp
import udp


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()

    PARSER.add_argument('ip', type=str)
    PARSER.add_argument('port', type=int)

    PARSER.add_argument('-cn', dest='connect_udp', action='store_true')

    CONNECT_ROLE = PARSER.add_mutually_exclusive_group()
    CONNECT_ROLE.add_argument('-s', dest='server', action='store_true')
    CONNECT_ROLE.add_argument('-c', dest='client', action='store_true')

    CONNECT_TYPE = PARSER.add_mutually_exclusive_group()
    CONNECT_TYPE.add_argument('-u', dest='udp_connect', action='store_true')
    CONNECT_TYPE.add_argument('-t', dest='tcp_connect', action='store_true')

    ARGS = PARSER.parse_args()

    HOST = ARGS.ip
    PORT = ARGS.port

    if ARGS.server:
        if ARGS.udp_connect:
            udp.server(HOST, PORT)
        else:
            tcp.server(HOST, PORT)
    else:
        if ARGS.udp_connect:
            if ARGS.connect_udp:
                udp.connect_client(HOST, PORT)
            else:
                udp.client(HOST, PORT)
        else:
            tcp.client(HOST, PORT)
