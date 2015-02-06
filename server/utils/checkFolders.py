__author__ = 'rama'

import os
import config
from server.utils.bcolors import bcolors

def createIfNotExists():
    if os.path.isdir(config.__SESSIONS_DIR__)  == False:
        if config.__VERBOSE_MODE__:
            print (bcolors.BACK_LRED + "Creating SESSIONS folder." + bcolors.ENDC)
        os.mkdir(config.__SESSIONS_DIR__)