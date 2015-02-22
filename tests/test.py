__author__ = 'bernardo'

import urllib2
import time
from datetime import datetime


raw_input("Start the server on localhost:8000 and press enter.")

start_time = datetime.now()
page = urllib2.urlopen("http://localhost:8000/ping.tst").read()
print ("Server Response: " + page)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))