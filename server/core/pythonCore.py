# -*- coding: utf-8 -*-
__author__ = 'bernardo'
import sys
import re

from xml.sax.saxutils import escape, unescape
import codecs
from server.utils.httpMessages import messages
import config
from server.utils.bcolors import bcolors
from server.utils import info
from subprocess import Popen, PIPE
import subprocess

import sys
if sys.version_info >= (3, 0):
    import io as strIO
else:
    import StringIO as strIO


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

        if sys.version_info >= (3, 0):
            codeOut = strIO.BytesIO()
        else:
            codeOut = strIO.StringIO()

        sys.stdout = codeOut
        sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)
        try:
            exec('# -*- coding: utf-8 -*-\n\r\n\r' + res)
        except Exception as e:
            exception = e



        sys.stdout = sys.__stdout__
        response2 = codeOut.getvalue()
        if sys.version_info >= (3, 0):
            response2 = response2.decode('UTF-8')
        response_content = response_content.replace('<%' + res + '%>',
                                                    str(response2))
        if exception != None:
            response_content = messages.InternalError
            if config.__VERBOSE_MODE__ == True:

                print ( bcolors.BACK_LRED+ \
                        "  --InternalError:\n\t\t" + str(exception) + \
                        bcolors.ENDC)


    match = re.compile('<pl%(.+?)%pl>',
                       flags=re.DOTALL)
    results = match.findall(response)

    perlUseLib = "use lib '"+config.__WWW_DIR__+"';"
    for res in results:

        p = subprocess.Popen(["perl", "-e "+perlUseLib +res+""],
                             stdout=subprocess.PIPE)
        out, err = p.communicate()
        response_content = response_content.replace('<pl%' +  res + '%pl>',
                                                    str(out.decode('UTF-8')))




    match = re.compile('!%(.+?)%!',
                       flags=re.DOTALL)

    results = match.findall(response)

    for res in results:
        response_content = response_content.replace('!%' + res + '%!',
                                                    eval(res))

    return response_content
