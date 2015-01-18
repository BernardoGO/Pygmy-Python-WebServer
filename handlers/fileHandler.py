__author__ = 'bernardo'

import pythonCore
import cookieHandler
import pathManager
from httpMessages import messages
import config

def read(self, filename, getNpost):
    try:
        if len(filename) < 2:
            filename = config.__INDEX_PAGE__
        filepath = config.__WWW_DIR__ + filename
        allow = pathManager.verify_all(filepath)
        if allow == False:
            return messages.Forbidden
        file_handler = open(filepath, 'rb')
        response = file_handler.read()
        response = pythonCore.replaceAll(self, response, getNpost)
        return [messages.Ok[0], response]
    except Exception as e:
        return [messages.NotFound, 'Not Found' + str(e)]