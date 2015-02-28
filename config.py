from server.utils.wstypes import HTMLVer
import os


import sys
if sys.version_info >= (3, 0):
    import configparser as ConfigParser
else:
    import ConfigParser

configParser = ConfigParser.RawConfigParser()
configFilePath = r'config.conf'
configParser.read(configFilePath)

getc = configParser.get
path = os.path.abspath

__WWW_DIR__ = path(getc('folders', 'wwwFolder'))
__SESSIONS_DIR__ = path(getc('folders', 'sessionsFolder'))
__INTERNAL_PORT__ = int(getc('server', 'port'))
addr = getc('server', 'listenAddress')
if addr != "ALL": __LISTEN_ADDRESS__ = addr
else: __LISTEN_ADDRESS__ = ""
__SESSION_COOKIE_NAME__ = getc('server', 'sessionCookieName')
__ALLOWED_DIRS__ = eval(getc('folders', 'allowedDirs'))
__ALLOWED_DIRS_AND_SUB__ = [path(x) for x in eval(getc('folders', 'allowedDirsAndSubdirs'))]
__ALLOWED_EXTENSIONS__ = eval(getc('files', 'allowedExtensions'))
__DENIED_EXTENSIONS__ = eval(getc('files', 'deniedExtensions'))
__MAX_POST_LENGTH__ = getc('files', 'maxPostLength')
__INDEX_PAGE__ = getc('files', 'indexPage')
__ENABLE_MULTITHREADING__ = eval(getc('server', 'enableMultithreading'))
__HTML_VER__ = eval( "HTMLVer." + getc('server', 'htmlVersion') )
__VERBOSE_MODE__ = eval(getc('server', 'enableVerboseMode'))
__ACCEPT_ARGS__ = eval(getc('server', 'acceptArgs'))
__LOG_ERRORS__ = eval(getc('server', 'enableErrorLogging'))