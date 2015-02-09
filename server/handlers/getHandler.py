from server.managers import sessionManager

__author__ = 'bernardo'
import mimetypes

import config
from server.handlers import fileHandler, cookieHandler
from server.managers import sessionManager

import sys
if sys.version_info >= (3, 0):
    from urllib.parse import parse_qs
    import urllib.parse as urlparse
else:
    from urlparse import parse_qs
    import urlparse

def do_GET(self):
    parsed_path = urlparse.urlparse(self.path)
    sessionId = sessionManager.startSession(self)
    par = urlparse.parse_qs(urlparse.urlparse(self.path).query)
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
