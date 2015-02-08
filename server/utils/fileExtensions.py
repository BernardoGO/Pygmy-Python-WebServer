__author__ = 'bernardogo'
import config
from server.utils.bcolors import bcolors


def check_denied(filepath):
    if len(config.__DENIED_EXTENSIONS__) < 1:
        print bcolors.WARNING + "DENIED LIST EMPTY" + bcolors.ENDC
        return True
    for peach in config.__DENIED_EXTENSIONS__:
        if filepath.endswith(peach.replace('*', '')):
            print bcolors.WARNING + "THE EXT IS NOT ALLOWED" + bcolors.ENDC
            return False

    return True

def check_allowed(filepath):
    if len(config.__ALLOWED_EXTENSIONS__) < 1:
        return True
    for peach in config.__ALLOWED_EXTENSIONS__:
        if filepath.endswith(peach.replace('*', '')):
            return True
    print bcolors.WARNING + "NOT ALLOWED EXTENSION" + bcolors.ENDC
    return False