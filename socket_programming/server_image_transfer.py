import os
from socket import *
from struct import unpack


class ServerProtocol:

    def __init__(self):
        self.socket = None
        self.output_dir = '.'
        self.file_num = 1

    def listen(self, server_ip, server_port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((server_ip, server_port))
        self.socket.listen(1)

    def handle_images(self):

        try:
            while True:
                (connection, addr) = self.socket.accept()
                try:
                    mode = connection.recv(8)
                    print "mode: ", mode
                    (MODE, ) = unpack('>Q', mode)
                    print "MODE: ", MODE
                    bs = connection.recv(8)
                    print bs
                    (length,) = unpack('>Q', bs)
                    print "length: ", length
                    data = b''
                    while len(data) < length:
                        # doing it in batches is generally better than trying
                        # to do it all in one go, so I believe.
                        to_read = length - len(data)
                        data += connection.recv( 4096 if to_read > 4096 else to_read)

                        # send our 0 ack
                        assert len(b'\00') == 1
                        # connection.sendall(b'\00')



                    with open(os.path.join(
                            self.output_dir, 'server.png'), 'w'
                    ) as fp:
                        fp.write(data)

                    self.file_num += 1
                    connection.sendall(b"done"+str(21))

                finally:
                    connection.shutdown(SHUT_WR)
                    connection.close()
        finally:
            self.close()
            print "image received"

    def close(self):
        self.socket.close()
        self.socket = None

        # could handle a bad ack here, but we'll assume it's fine.


if __name__ == '__main__':
    sp = ServerProtocol()
    sp.listen('localhost', 55555)
    sp.handle_images()