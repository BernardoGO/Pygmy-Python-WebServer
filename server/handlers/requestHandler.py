__author__ = 'bernardo'
from BaseHTTPServer import BaseHTTPRequestHandler

from server.handlers import postHandler, getHandler


class requestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        #pass
        getHandler.do_GET(self)

    def do_POST(self):
        postHandler.do_POST(self)
