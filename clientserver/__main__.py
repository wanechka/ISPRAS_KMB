from tcp import server_tcp, client_tcp
from udp import server_udp, client_udp

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("ip", type=str)
    parser.add_argument("port", type=int)

    parser.add_argument("-s", dest="server", action="store_true")
    parser.add_argument("-c", dest="client", action="store_true")
    parser.add_argument("-u", dest="udp_connect", action="store_true")

    args = parser.parse_args()

    host = args.ip
    port = args.port
    
    if args.server:
        if args.udp_connect:
            server_udp(host, port)
        else:
            server_tcp(host, port)

    
    if args.client:
        if args.udp_connect:
            client_udp(host, port)
        else:
            clietn_tcp(host, port)