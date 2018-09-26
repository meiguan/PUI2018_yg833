# Mei Guan, NYU, Sept. 2018
#############################################
# Homework 3 
# Assignment 3
# "Show Bus Location"
############################################

# Import packages
from __future__ import print_function #for compatibility between python2 and python3
import os # allows for a way of using operating system dependent functionality
import sys # allows for reading from system args
import json # allows for encoding and decoding JSON data.
try:
    import urllib2 as urllib # for working with URLs
except ImportError:
    import urllib.request as urllib

#checks the length of the args to only run script if the num of args match
if not len(sys.argv) == 3:
    print ("Invalid number of arguments.")
    sys.exit()

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

bus_line = "Bus Line : " # string for the bus line
print(bus_line + bus_arg) # print the string

# get var for the length of line
bus_num = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
bus_num_str = "Number of Active Buses : " # print string of the num of buses
bus_n = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'] # #set an object to bus_n

print(bus_num_str, bus_num) # print the strings

bus_loc1 = "Bus "
bus_loc2 = " is at latitude "
bus_loc3 = " and longitude "

# iterate and print each bus location
for i in range(len(bus_n)):
    lat = bus_n[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    long = bus_n[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print(bus_loc1 +str(i) + bus_loc2 + str(lat)+bus_loc3 + str(long))
