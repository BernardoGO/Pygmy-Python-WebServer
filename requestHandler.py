__author__ = 'bernardo'
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
from cgi import parse_header, parse_multipart
from urlparse import parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler
import config
import getHandler
import postHandler

class requestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        getHandler.do_GET(self)

    def do_POST(self):
        postHandler.do_POST(self)
