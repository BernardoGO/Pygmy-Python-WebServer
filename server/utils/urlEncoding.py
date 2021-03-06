__author__ = 'bernardo'
import posixpath
import urllib
import urlparse


def url_fi2x(s, charset = 'utf-8'):
    if isinstance(s, unicode):
        s = s.encode(charset, 'ignore')
    scheme, netloc, path, qs, anchor = urlparse.urlsplit(s)
    path = urllib.quote(path, '/%')
    qs = urllib.quote_plus(qs, ':&=')
    return urlparse.urlunsplit((scheme,
     netloc,
     path,
     qs,
     anchor))

def guess_typ2e(self, path):
    base, ext = posixpath.splitext(path)
    if self.extensions_map.has_key(ext):
        return self.extensions_map[ext]
    else:
        ext = ext.lower()
        if self.extensions_map.has_key(ext):
            return self.extensions_map[ext]
        return self.extensions_map['']

def FixURL(string):
    fix_dict = {' ':'%20','!':'%21','"':'%22','#':'%23','$':'%24',
                '&':'%26',"'":'%27','(':'%28',')':'%29',
                '*':'%2A','+':'%2b','.':'%2E','/':'%2F',':':'%3A',
                ';':'%3B','?':'%3F','@':'%40','{':'%7B','{':'%7D'}

    for k,v in fix_dict.iteritems():
        if k in string:
            string = string.replace(k,v)
    return string