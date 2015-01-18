__author__ = 'bernardo'
import mimetypes
import urlparse

import config
from handlers import cookieHandler, fileHandler
import sessionManager


def do_GET(self):
    parsed_path = urlparse.urlparse(self.path)
    sessionId = sessionManager.startSession(self)
    par = urlparse.parse_qs(urlparse.urlparse(self.path).query)
    response = fileHandler.read(self, parsed_path.path, [par, None])
    self.send_response(response[0])
    self.send_header('Set-Cookie', cookieHandler.WriteCookie(self, config.__SESSION_COOKIE_NAME__, sessionId))
    self.end_headers()
    self.wfile.write(response[1])
    return



extensions_map = mimetypes.types_map.copy()
extensions_map.update({'': 'application/octet-stream',
 '.py': 'text/plain',
 '.c': 'text/plain',
 '.h': 'text/plain'})
