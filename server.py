from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
from cgi import parse_header, parse_multipart
from urlparse import parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler
from requestHandler import requestHandler
import config
from SocketServer import ThreadingMixIn
import threading
from BaseHTTPServer import HTTPServer
from requestHandler import requestHandler
import multithreadSupport



if __name__ == '__main__':
    if config.__ENABLE_MULTITHREADING__ == False:
        server = HTTPServer((config.__LISTEN_ADDRESS__, config.__INTERNAL_PORT__), requestHandler)
        print "MULTI-THREADING: DISABLED"
    else:
        server = multithreadSupport.ThreadedHTTPServer((config.__LISTEN_ADDRESS__, config.__INTERNAL_PORT__), requestHandler)
        print "MULTI-THREADING: ENABLED"
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
