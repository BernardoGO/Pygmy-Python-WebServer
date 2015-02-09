__author__ = 'BernardoGO'

from server.core import pythonCore
from server.managers import pathManager
from server.utils.httpMessages import messages
from server.utils.bcolors import bcolors
import config

def read(self, filename, getNpost):
    try:
        if len(filename) < 2:
            filename = config.__INDEX_PAGE__
        filepath = config.__WWW_DIR__ +"/"+  filename
        if config.__VERBOSE_MODE__ == True:
            print ( bcolors.OKGREEN+"Requested File: " +filepath + bcolors.ENDC)
        allow = pathManager.verify_all(filepath)
        if allow == False:
            if config.__VERBOSE_MODE__ == True:
                print ( bcolors.BACK_LRED+"  --Forbidden" + bcolors.ENDC)
            return messages.Forbidden
        file_handler = open(filepath, 'rb')
        response = str(file_handler.read().decode('UTF-8'))
        response = pythonCore.replaceAll(self, response, getNpost)
        #print "TYPEEEE: " + str(type(response)) + " " + str(response)

        if isinstance(response, list):
            #if config.__VERBOSE_MODE__:
            #    print ( bcolors.BACK_LRED+"  --InternalError" + bcolors.ENDC)
            return [response[0], "InternalError!"]
        return [messages.Ok[0], response]
    except Exception as e:
        if config.__VERBOSE_MODE__ == True:
            print ( bcolors.BACK_LRED+"  --Not Found" + bcolors.ENDC)
            print ( "fileHandler: " + str(e))
        return [messages.NotFound[0], 'Not Found' ]#+ str(e)