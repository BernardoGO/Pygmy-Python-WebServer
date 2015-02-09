__author__ = 'bernardo'


from server.handlers import postHandler, getHandler

import sys
if sys.version_info >= (3, 0):
    from http.server import BaseHTTPRequestHandler, HTTPServer
else:
    from BaseHTTPServer import BaseHTTPRequestHandler as BaseHTTPRequestHandler

class requestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        #pass
        getHandler.do_GET(self)

    def do_POST(self):
        postHandler.do_POST(self)
