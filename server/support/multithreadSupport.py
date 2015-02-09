__author__ = 'bernardogo'

import sys
if sys.version_info >= (3, 0):
    from socketserver import ThreadingMixIn
    from http.server import HTTPServer as http
else:
    from SocketServer import ThreadingMixIn
    from BaseHTTPServer import HTTPServer as http


class ThreadedHTTPServer(ThreadingMixIn, http):
    """ This class allows to handle requests in separated threads.
        No further content needed, don't touch this. """