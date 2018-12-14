#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__credits__ = "Carlos Donato"
__copyright__ = "Copyright 2018, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"


'''Python script for monitoring IEEE 802.11 networks using iperf3
Please make sure the server is running using iperf3 before running this script!
Ex: iperf3 -s -i 0.5
'''

import datetime
from subprocess import call

number_of_measurements = 5
filename = "iperf3_"
date_and_time = datetime.datetime.now().strftime("%Y-%m-%d-%Hh-%Mm-%Ss")
location = 'near'  # 'near' is just next to the WTP and 'workstation' experimenting from my desk
path = '../measurements/iperf3/measurement_' + str(location) + '_' + str(date_and_time)
duration = '120'

print "Initializing iperf3 measurement!"

call('mkdir ' + str(path), shell=True)

for i in range(0, number_of_measurements):
    call('iperf3 -c 192.168.2.1 ' + '-t ' + str(duration) + ' -J >> ' +
         str(path) +
         '/' +
         str(filename) +
         str(i) +
         '_' + str(duration) +
         's_' +
         str(location) +
         '.json',
         shell=True)

print "Iperf3 measurement done!"
