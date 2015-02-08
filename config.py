from server.utils.wstypes import HTMLVer
import os
import ConfigParser

configParser = ConfigParser.RawConfigParser()
configFilePath = r'config.conf'
configParser.read(configFilePath)

path = os.path.abspath

__WWW_DIR__ = path('../elab/www/')
__SESSIONS_DIR__ = path('sessions/')
__INTERNAL_PORT__ = int(configParser.get('server', 'port'))
__LISTEN_ADDRESS__ = ''
__SESSION_COOKIE_NAME__ = 'sessionId'
__ALLOWED_DIRS__ = []
__ALLOWED_DIRS_AND_SUB__ = \
    [
        path('../elab/www/')
    ]
__ALLOWED_EXTENSIONS__ = []
__DENIED_EXTENSIONS__ = ['*.exe']
__MAX_POST_LENGTH__ = 2097152
__INDEX_PAGE__ = 'index.py'
__ENABLE_MULTITHREADING__ = True
__HTML_VER__ = HTMLVer.HTML5
__VERBOSE_MODE__ = True
