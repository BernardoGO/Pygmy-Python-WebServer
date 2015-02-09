__author__ = 'bernardogo'
from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer as http


class ThreadedHTTPServer(ThreadingMixIn, http):
    """ This class allows to handle requests in separated threads.
        No further content needed, don't touch this. """