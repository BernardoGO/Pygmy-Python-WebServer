__author__ = 'bernardo'
import config

def check_allowed(filepath):
    if len(config.__ALLOWED_EXTENSIONS__) < 1:
        return True
    for peach in config.__ALLOWED_EXTENSIONS__:
        if filepath.endswith(peach.replace('*', '')):
            return True

    return False


def check_denied(filepath):
    if len(config.__DENIED_EXTENSIONS__) < 1:
        return True
    for peach in config.__DENIED_EXTENSIONS__:
        if filepath.endswith(peach.replace('*', '')):
            return False

    return True
