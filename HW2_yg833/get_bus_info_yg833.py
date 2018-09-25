# Import libraries
from __future__ import print_function #for compatibility between python2 and python3
import os
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

#pass in the py args
key_arg = sys.argv[1]
bus_arg = sys.argv[2]

#URL Format : http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=YOUR_KEY&VehicleMonitoringDetailLevel=calls&LineRef=B52
url_1 ="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
url_2 = "&VehicleMonitoringDetailLevel=calls&LineRef="

#concatenate the URL
url = url_1+key_arg+url_2+bus_arg

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
