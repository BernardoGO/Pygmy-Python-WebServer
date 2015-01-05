__author__ = 'bernardo'
import os
import cgi
import Cookie
import sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
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

