# Taken from curio: https://github.com/dabeaz/curio

from gevent.server import StreamServer
from socket import *

# this handler will be run for each incoming connection in a dedicated greenlet
def echo(socket, address):
    print('New connection from %s:%s' % address)
    try:
        socket.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
    except (OSError, NameError):
        pass
    while True:
        data = socket.recv(100000)
        if not data:
            break
        socket.sendall(data)
    socket.close()

if __name__ == '__main__':
    server = StreamServer(('0.0.0.0', 25000), echo)
    server.serve_forever()
