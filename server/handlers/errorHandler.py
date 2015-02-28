__author__ = 'BernardoGO'

import config
from server.utils.bcolors import bcolors

#level = 0-10

def handle(message, color = bcolors.FAIL, level=5):
    if config.__VERBOSE_MODE__ == True:
        print ( color+ message + bcolors.ENDC)

    if config.__LOG_ERRORS__ == True:
        f = open('errors.log', 'a')
        f.write(message)
        f.close()