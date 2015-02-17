from server.managers import sessionManager

__author__ = 'BernardoGO'
from cgi import parse_header, parse_multipart

import mimetypes




import sys
if sys.version_info >= (3, 0):
    from urllib.parse import parse_qs
    import urllib.parse as urlparse
else:
    from urlparse import parse_qs
    import urlparse

from server.handlers import fileHandler, cookieHandler
import config
from server.managers import sessionManager


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
    if sys.version_info >= (3, 0):
        self.wfile.write(bytes((response[1]), 'UTF-8'))
    else:
        self.wfile.write(((response[1])))
    return


extensions_map = mimetypes.types_map.copy()
extensions_map.update({'': 'application/octet-stream',
 '.py': 'text/plain',
 '.c': 'text/plain',
 '.h': 'text/plain'})