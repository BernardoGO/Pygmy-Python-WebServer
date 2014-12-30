__author__ = 'bernardo'
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
from cgi import parse_header, parse_multipart
from urlparse import parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler
import config
import fileHandler
import cookieHandler
import sessionManager

def parse_POST(self):
    ctype, pdict = parse_header(self.headers['content-type'])
    length = int(self.headers['content-length'])
    accept = True
    if length > config.__MAX_POST_LENGTH__:
        accept = False
    if ctype == 'multipart/form-data':
        postvars = parse_multipart(self.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        postvars = parse_qs(self.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
    if accept == False:
        postvars = None
    return postvars


def do_POST(self):
    sessionId = sessionManager.startSession(self)
    parsed_path = urlparse.urlparse(self.path)
    par = urlparse.parse_qs(urlparse.urlparse(self.path).query)
    try:
        postvars = parse_POST(self)
        response = fileHandler.read(self, parsed_path.path, [par, postvars])
    except:
        response = fileHandler.read(self, parsed_path.path, [par, None])

    self.send_response(response[0])
    self.send_header('Set-Cookie', cookieHandler.WriteCookie(self, config.__SESSION_COOKIE_NAME__, sessionId))
    self.end_headers()
    self.wfile.write(response[1])
    return
