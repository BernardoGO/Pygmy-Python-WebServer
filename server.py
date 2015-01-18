from BaseHTTPServer import HTTPServer

import config
from handlers.requestHandler import requestHandler
import multithreadSupport
import statusCheck


execfile('checkFolders.py')



if __name__ == '__main__':
    if config.__ENABLE_MULTITHREADING__ == False:
        server = HTTPServer((config.__LISTEN_ADDRESS__, config.__INTERNAL_PORT__), requestHandler)
        #print "MULTI-THREADING: DISABLED"
    else:
        server = multithreadSupport.ThreadedHTTPServer((config.__LISTEN_ADDRESS__, config.__INTERNAL_PORT__), requestHandler)
        #print "MULTI-THREADING: ENABLED"
    statusCheck.printConfigs()
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
