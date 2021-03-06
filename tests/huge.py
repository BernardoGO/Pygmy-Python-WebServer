__author__ = 'bernardo'

import urllib2
import time
from datetime import datetime
import argparse
import thread
import threading

PORT = 8000
ip = "localhost"


def call():
    a = urllib2.urlopen(("http://{0}:{1}/ping.tst").format(str(parsed.ip), str(parsed.p))).read()
    print a

parser = argparse.ArgumentParser()
parser.add_argument('-p', action="store", default=PORT, type=int)
parser.add_argument('-ip', action="store", default=ip, type=str)
parser.add_argument('-f', action="store", default=ip, type=str)
parser.add_argument('-t', action="store", default=1, type=int)

parsed = parser.parse_args()

threads = []

raw_input("Start the server on {0}:{1} and press enter.".format(str(parsed.ip), str(parsed.p)))
for x in xrange(0, parsed.t):
    start_time = datetime.now()
    for x in range(0,1000):
        #thread.start_new_thread(call, ())
        thread = threading.Thread(target=call)
        thread.start()

        threads.append(thread)

    end_time = datetime.now()

    for thread in threads:
        thread.join()

    time = '{}'.format((end_time - start_time).total_seconds()* 1000)
    with open(parsed.f+".txt", "a") as myfile:
        myfile.write(time+"\n")
    print('Duration: '+time)