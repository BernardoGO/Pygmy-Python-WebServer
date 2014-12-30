from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
from cgi import parse_header, parse_multipart
from urlparse import parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler
from requestHandler import requestHandler
import config

from requestHandler import requestHandler

__WWW_DIR__ = "www/"




if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer((config.__LISTEN_ADDRESS__, config.__INTERNAL_PORT__), requestHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
