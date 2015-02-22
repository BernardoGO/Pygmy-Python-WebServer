__author__ = 'bernardo'

import urllib2


raw_input("Start the server on localhost:8000 and press enter.")


page = urllib2.urlopen("http://localhost:8000/ping.tst").read()
print ("Server Response: " + page)