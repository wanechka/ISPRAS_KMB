import tcp
import udp


import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("ip", type=str)
    parser.add_argument("port", type=int)

    connectRole = parser.add_mutually_exclusive_group()
    connectRole.add_argument("-s", dest="server", action="store_true")
    connectRole.add_argument("-c", dest="client", action="store_true")
    
    parser.add_argument("-u", dest="udp_connect", action="store_true")

    args = parser.parse_args()

    host = args.ip
    port = args.port
    
    if args.server:
        if args.udp_connect:
            udp.server(host, port)
        else:
            tcp.server(host, port)

    
    if args.client:
        if args.udp_connect:
            udp.client(host, port)
        else:
            tcp.client(host, port)
