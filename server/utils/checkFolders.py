__author__ = 'rama'

import os
import config


def createIfNotExists():
    if os.path.isdir(config.__SESSIONS_DIR__)  == False:
        os.mkdir(config.__SESSIONS_DIR__)