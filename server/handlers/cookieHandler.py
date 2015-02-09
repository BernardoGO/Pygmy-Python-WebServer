__author__ = 'BernardoGO'
import os
import cgi


import sys
if sys.version_info >= (3, 0):
    import http.cookies as Cookie
else:
    import Cookie

cookies = []

def ClearCookies(self):
    cookies = []



def ReadCookie(self, key):
    if 'cookie' in self.headers:
        c = Cookie.SimpleCookie(self.headers['cookie'])
        return str(c[key].value)


def WriteCookie(self, key, value):
    form = cgi.FieldStorage()
    c = Cookie.SimpleCookie()
    c[key] = value
    return c.output(header='')


def countCookies(self):
    return len(cookies)

def getCookies(self):
    return cookies

