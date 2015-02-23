__author__ = 'BernardoGO'

import config
from server.utils.bcolors import bcolors

def handle(message, color = bcolors.FAIL):
    if config.__VERBOSE_MODE__ == True:
        print ( color+ message + bcolors.ENDC)