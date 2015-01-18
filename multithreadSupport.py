__author__ = 'bernardo'
from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """ This class allows to handle requests in separated threads.
        No further content needed, don't touch this. """