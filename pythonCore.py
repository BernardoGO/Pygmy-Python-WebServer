# -*- coding: utf-8 -*-
__author__ = 'bernardo'
import socket
import signal
import time
import os, sys
import re
import StringIO
import config
import cookieHandler
import sessionManager
import info
import html
import textStyle

from xml.sax.saxutils import escape, unescape
import codecs
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
    for res in results:
        codeOut = StringIO.StringIO()
        sys.stdout = codeOut
        sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)
        try:
            exec '# -*- coding: utf-8 -*-\n\r\n\r' + res
        except Exception as e:
            print str(e)

        sys.stdout = sys.__stdout__
        response2 = codeOut.getvalue()
        response_content = response_content.replace('<%' + res + '%>', response2)

    match = re.compile('!%(.+?)%!', flags=re.DOTALL)
    results = match.findall(response)
    for res in results:
        response_content = response_content.replace('!%' + res + '%!', eval(res))

    return response_content
