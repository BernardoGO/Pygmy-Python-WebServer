# -*- coding: utf-8 -*-
__author__ = 'bernardo'
import sys
import re
import StringIO
from xml.sax.saxutils import escape, unescape
import codecs
from server.utils.httpMessages import messages
import config
from server.utils.bcolors import bcolors
from server.utils import info


html_escape_table = {'"': '&quot;',
 "'": '&apos;'}
html_unescape_table = {v:k for k, v in html_escape_table.items()}

def html_escape(text):
    return escape(text, html_escape_table)


def html_unescape(text):
    return unescape(text, html_unescape_table)

def server_version():
    return info.__SRV_VERSION__

def replaceAll(self, response, getNpost):
    __GET__ = getNpost[0]
    __POST__ = getNpost[1]
    match = re.compile('<%(.+?)%>', flags=re.DOTALL)
    results = match.findall(response)
    response_content = response
    exception = None

    for res in results:
        codeOut = StringIO.StringIO()
        sys.stdout = codeOut
        sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)
        try:
            exec '# -*- coding: utf-8 -*-\n\r\n\r' + res
        except Exception as e:
            exception = e

        sys.stdout = sys.__stdout__
        response2 = codeOut.getvalue()
        response_content = response_content.replace('<%' + res + '%>', response2)
        if exception != None:
            response_content = messages.InternalError
            if config.__VERBOSE_MODE__ == True:
                print ( bcolors.BACK_LRED+"  --InternalError:\n\t\t" + str(exception) + bcolors.ENDC)

    match = re.compile('!%(.+?)%!', flags=re.DOTALL)
    results = match.findall(response)
    for res in results:
        response_content = response_content.replace('!%' + res + '%!', eval(res))

    return response_content
