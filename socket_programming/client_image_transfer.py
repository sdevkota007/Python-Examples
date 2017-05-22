from socket import *
from struct import pack


class ClientProtocol:

    def __init__(self):
        self.socket = None

    def connect(self, server_ip, server_port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.settimeout(5)
        self.socket.connect((server_ip, server_port))

    def close(self):
        self.socket.shutdown(SHUT_WR)
        self.socket.close()
        self.socket = None

    def send_image(self, image_data):

        # use struct to make sure we have a consistent endianness on the length
        MODE = 1
        mode = pack('>Q', MODE)
        print "length: ", len(image_data)
        length = pack('>Q', len(image_data))
        print "length: ", length
        # sendall to make sure it blocks if there's back-pressure on the socket
        self.socket.sendall(mode)
        self.socket.sendall(length)
        self.socket.sendall(image_data)

        ack = self.socket.recv(8)
        print "image sent and ack received"
        print "server says: ", ack
        # could handle a bad ack here, but we'll assume it's fine.

if __name__ == '__main__':
    cp = ClientProtocol()

    image_data = None
    with open('client.png', 'r') as fp:
        image_data = fp.read()

    assert(len(image_data))
    print "data read"
    cp.connect('localhost', 9999)
    print "connected"
    cp.send_image(image_data)

    cp.close()