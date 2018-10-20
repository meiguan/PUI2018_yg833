# Mei Guan, NYU, Sept. 2018
#############################################
# Homework 3 
# Assignment 4
# "Get Bus Information"
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
if not len(sys.argv) == 4:
    print ("Invalid number of arguments.")
    sys.exit()

# pass in the py args
key_arg = sys.argv[1]
bus_arg = sys.argv[2]
# file out open to the second arg and "W" is to write the file
fout = open(sys.argv[3], "w")

#URL Format : http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=YOUR_KEY&VehicleMonitoringDetailLevel=calls&LineRef=B52
url_1 ="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
url_2 = "&VehicleMonitoringDetailLevel=calls&LineRef="

#concatenate the URL
url = url_1+key_arg+url_2+bus_arg 

# open and read the URL
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

#set an object to bus_n
bus_n = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

# write the headers for the file
fout.write("Latitude," + "Longitude," + "Stop Name, " + "Stop Status\n")

# write the file itself
for i in range(len(bus_n)):
    lat = str(bus_n[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    long = str(bus_n[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    
    if bool(bus_n[i]['MonitoredVehicleJourney']['OnwardCalls']):
        status = str(bus_n[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
        stop_name = str(bus_n[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
        fout.write(lat + "," + long + "," + stop_name + ","+status)
        fout.write("\n")
    else:
        fout.write(lat + "," + long + "," + "N/A" + ","+"N/A")
        fout.write("\n")
