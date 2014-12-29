from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
from cgi import parse_header, parse_multipart
from urlparse import parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler
from requestHandler import requestHandler

from requestHandler import requestHandler

__WWW_DIR__ = "www/"




if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), requestHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
