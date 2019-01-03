#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2018, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"


''' Python script for parsing iperf3 output to CSV format
    Run: 
'''

from configs.logger import *
import csv


# Function to initialize WTPs aggregated stats file
def format_raw_results(experiment_path, raw_results_filename, options):
    iperf3_monitoring_logger.info('Hello parser! ' + str(experiment_path + raw_results_filename))
    #f = open(str(experiment_path + raw_results_filename), "r")
    with open('results.csv', 'w') as csvfile:
        fieldnames = ['Interval (sec)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        #for line in f:
        #    if "Starting Test" in line:
        #        print(line)