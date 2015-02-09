#!/usr/bin/python
# -*- coding: utf-8 -*-

from BaseHTTPServer import HTTPServer

import config
from server.handlers.requestHandler import requestHandler
from server.support import multithreadSupport
from server.utils import statusCheck
from server.utils import checkFolders
import argparse



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', action="store_true", default=config.__VERBOSE_MODE__)
    parser.add_argument('-p', action="store", default=config.__INTERNAL_PORT__, type=int)
    parsed = parser.parse_args()
    if config.__ACCEPT_ARGS__ == True:
        config.__VERBOSE_MODE__ = bool(parsed.v)
        config.__INTERNAL_PORT__ = int(parsed.p)


    checkFolders.createIfNotExists()
    if config.__ENABLE_MULTITHREADING__ == False:
        server = HTTPServer((config.__LISTEN_ADDRESS__, config.__INTERNAL_PORT__), requestHandler)
        #print "MULTI-THREADING: DISABLED"
    else:
        server = multithreadSupport.ThreadedHTTPServer((config.__LISTEN_ADDRESS__, config.__INTERNAL_PORT__),
                                                       requestHandler)
        #print "MULTI-THREADING: ENABLED"
    statusCheck.printConfigs()
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
