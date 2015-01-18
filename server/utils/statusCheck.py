__author__ = 'bernardo'
import config


def printConfigs():
    addrr = str(config.__LISTEN_ADDRESS__)
    if len(addrr) < 3:
        addrr = "localhost"
    print "ADDRESS: " + addrr + ":" + str(config.__INTERNAL_PORT__)
    print "FOLDER: " + config.__WWW_DIR__
    print "MULTI-THREADING: " + str(config.__ENABLE_MULTITHREADING__)
    return