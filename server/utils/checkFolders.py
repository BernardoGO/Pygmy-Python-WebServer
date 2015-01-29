__author__ = 'rama'

import os
import config


def createIfNotExists():
    if config.__SESSIONS_DIR__[:-1] not in os.listdir(os.curdir):
        os.mkdir(config.__SESSIONS_DIR__)