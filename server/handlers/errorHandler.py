__author__ = 'BernardoGO'

import config
from server.utils.bcolors import bcolors
import datetime

#level = 0-10 where 0 is the most important

def handle(message, color = bcolors.FAIL, level=5):

    datew = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    args = message, bcolors.FAIL, level, datew

    printOnScreen(*args)
    printOnFile(*args)



def printOnScreen(message, color = bcolors.FAIL, level=5, datew = None):

    if datew is None:
        datew = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if config.__VERBOSE_MODE__ == True:
        print (bcolors.OKBLUE + datew  + ":  "+ bcolors.ENDC \
               + color+ message + bcolors.ENDC)


def printOnFile(message, color = bcolors.FAIL, level=5, datew = None):

    if datew is None:
        datew = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if config.__LOG_ERRORS__ == True:
        f = open('errors.log', 'a')
        f.write(datew  + ":  " + message + "\n")
        f.close()