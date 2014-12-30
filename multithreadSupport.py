__author__ = 'bernardo'
from SocketServer import ThreadingMixIn
import threading
from BaseHTTPServer import HTTPServer
from requestHandler import requestHandler


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """ This class allows to handle requests in separated threads.
        No further content needed, don't touch this. """