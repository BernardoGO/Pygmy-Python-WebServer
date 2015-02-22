__author__ = 'bernardo'

import urllib2
import time
from datetime import datetime
import argparse

PORT = 8000
ip = "localhost"

parser = argparse.ArgumentParser()
parser.add_argument('-p', action="store", default=PORT, type=int)
parser.add_argument('-ip', action="store", default=ip, type=str)
parsed = parser.parse_args()

raw_input("Start the server on {0}:{1} and press enter.".format(str(parsed.ip), str(parsed.p)))

start_time = datetime.now()
for x in range(0,1000):
    urllib2.urlopen(("http://{0}:{1}/ping.tst").format(str(parsed.ip), str(parsed.p)))
end_time = datetime.now()
print('Duration: {}'.format((end_time - start_time).total_seconds()* 1000))