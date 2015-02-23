__author__ = 'BernardoGO'

from server.core import pythonCore
from server.managers import pathManager
from server.utils.httpMessages import messages
from server.utils.bcolors import bcolors
from server.handlers import errorHandler
import traceback

import config
import sys

def read(self, filename, getNpost):
    try:
        if len(filename) < 2:
            filename = config.__INDEX_PAGE__
        if "ping.tst" in filename:
            return [messages.Ok[0], "OK"]
        filepath = config.__WWW_DIR__ +"/"+  filename
        filepath = filepath.replace( "//", "/")
        errorHandler.handle("Requested File: " +filepath, color=bcolors.OKGREEN, level = 2)
        #if config.__VERBOSE_MODE__ == True:
        #    print ( bcolors.OKGREEN+"Requested File: " +filepath + bcolors.ENDC)
        allow = pathManager.verify_all(filepath)
        if allow == False:
            errorHandler.handle("  --Forbidden: "  +filepath, color=bcolors.BACK_LRED, level = 8)
            return messages.Forbidden
        file_handler = open(filepath, 'rb')

        readVal = file_handler.read()

        if sys.version_info >= (3, 0):
            readVal = readVal.decode('UTF-8')

        response = str(readVal)
        response = pythonCore.replaceAll(self, response, getNpost)

        if isinstance(response, list):
            return [response[0], "InternalError!"]
        return [messages.Ok[0], response]
    except Exception as e:

        errorHandler.handle("  --Not Found: "  +filepath, color=bcolors.BACK_LRED, level = 7)
        errorHandler.handle("    fileHandler: " + str(e), color=bcolors.ENDC, level = 7)
        if config.__VERBOSE_MODE__ == True:
            traceback.print_exc()
        return [messages.NotFound[0], 'Not Found' ]#+ str(e)