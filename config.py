from server.utils.wstypes import HTMLVer
import os
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
__SESSION_COOKIE_NAME__ = 'sessionId'
__ALLOWED_DIRS__ = eval(getc('folders', 'allowedDirs'))
__ALLOWED_DIRS_AND_SUB__ = [path(x) for x in eval(getc('folders', 'allowedDirsAndSubdirs'))]
print "ALLOWER: " + str(__ALLOWED_DIRS_AND_SUB__)
__ALLOWED_EXTENSIONS__ = eval(getc('files', 'allowedExtensions'))
__DENIED_EXTENSIONS__ = eval(getc('files', 'deniedExtensions'))
__MAX_POST_LENGTH__ = 2097152
__INDEX_PAGE__ = 'index.py'
__ENABLE_MULTITHREADING__ = True
__HTML_VER__ = HTMLVer.HTML5
__VERBOSE_MODE__ = True
