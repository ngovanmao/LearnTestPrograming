
import socket
import time
import argparse

def main(args):

    server_address = (args.server_ip, args.server_port)
    message = args.msg
    sock = socket.socket(socket.AF_INET,   #IPv6
                        socket.SOCK_DGRAM) # UDP
    print("message = ", message)
    sock.sendto(message.encode(), server_address)
    """
    try:
        data, fromaddr = sock.recvfrom(1024)
        print("return message {} from {}".format(data, fromaddr))
    except:
        print("no return message")
    """
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--verbose',
        action='store_true')
    parser.add_argument(
        '--server_ip',
        type=str,
        help='Server IP address, default is 127.0.0.1.',
        default='127.0.0.1')
    parser.add_argument(
        '--server_port',
        type=int,
        help='Server listening port. Default: 6666',
        default=6666)
    parser.add_argument(
        '--msg',
        type=str,
        help='Sending message. Default: Hello.',
        default='Hello')

    args = parser.parse_args()

    main(args)

