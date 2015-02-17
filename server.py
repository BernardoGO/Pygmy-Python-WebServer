#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'BernardoGO'


import config
from server.utils import info
from server.handlers.requestHandler import requestHandler
from server.support import multithreadSupport
from server.utils import statusCheck
from server.utils import checkFolders
from server.utils import parseArgs
import argparse

import sys
if sys.version_info >= (3, 0):
    import http.server as http
else:
    from BaseHTTPServer import HTTPServer as http

def main():
    parseArgs.parseAll()

    checkFolders.createIfNotExists()
    if config.__ENABLE_MULTITHREADING__ == False:
        server = http((config.__LISTEN_ADDRESS__, config.__INTERNAL_PORT__), requestHandler)
    else:
        server = multithreadSupport.ThreadedHTTPServer((config.__LISTEN_ADDRESS__, config.__INTERNAL_PORT__),
                                                       requestHandler)
    statusCheck.printConfigs()


    if parseArgs.parsed.ver == True:
        print ("Server Version: "+str(info.__SRV_VERSION__))
        return

    if parseArgs.parsed.test == False:
        print('Starting server, use <Ctrl-C> to stop')
        server.serve_forever()

if __name__ == '__main__':
    main()


