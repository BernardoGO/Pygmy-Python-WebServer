__author__ = 'bernardo'
import config
import pythonCore
import cookieHandler
import pathManager

def read(self, filename, getNpost):
    try:
        if len(filename) < 2:
            filename = config.__INDEX_PAGE__
        filepath = config.__WWW_DIR__ + filename
        allow = pathManager.verify_all(filepath)
        if allow == False:
            return [503, 'Forbidden']
        file_handler = open(filepath, 'rb')
        response = file_handler.read()
        response = pythonCore.replaceAll(self, response, getNpost)
        return [200, response]
    except Exception as e:
        return [404, 'Not Found' + str(e)]
