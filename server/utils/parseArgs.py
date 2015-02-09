__author__ = 'BernardoGO'

import argparse
import config

parsed = None

def parseAll():
    global parsed
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', action="store_true", default=config.__VERBOSE_MODE__)
    parser.add_argument('-p', action="store", default=config.__INTERNAL_PORT__, type=int)
    parser.add_argument('-ip', action="store", default=config.__LISTEN_ADDRESS__, type=str)
    parser.add_argument('--test', action="store_true", default=False)
    parsed = parser.parse_args()
    if config.__ACCEPT_ARGS__ == True:
        config.__VERBOSE_MODE__ = bool(parsed.v)
        config.__INTERNAL_PORT__ = int(parsed.p)
        config.__LISTEN_ADDRESS__ = str(parsed.ip)