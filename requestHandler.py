__author__ = 'bernardo'
from BaseHTTPServer import BaseHTTPRequestHandler

from handlers import getHandler
import postHandler


class requestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        getHandler.do_GET(self)

    def do_POST(self):
        postHandler.do_POST(self)
