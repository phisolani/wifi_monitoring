#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2018, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"


''' Python script for monitoring IEEE 802.11 networks using iperf3 using TCP or UDP
    Please make sure the server is running using iperf3 before running this script!
    Ex: iperf3 -s -i 1 -p 5003
'''

import datetime
import os
from subprocess import call
from optparse import OptionParser
from iperf3.iperf3_csv_parser import *
from iperf3.iperf_graphs import *
from configs.logger import *

# Experimentation parameters and values
parser = OptionParser()
parser.add_option("", "--hostname", type="string", default="hostname")
parser.add_option("", "--host_ip", type="string", default="192.168.2.51")
parser.add_option("", "--timeout", type="int", default=30)  # e.g., 30 sec
parser.add_option("", "--measurements", type="int", default=1)
parser.add_option("", "--server_ip", type="string", default="192.168.2.1")  # e.g., the DHCP server
parser.add_option("", "--server_port", type="int", default=5003)  # e.g., 5003, 5004
parser.add_option("", "--protocol", type="string", default="UDP")  # e.g., TCP, UDP
parser.add_option("", "--output", type="string", default="CMD")  # e.g., JSON, CMD
parser.add_option("", "--bandwidth", type="string", default="30Mbps")  # e.g., 0, 20Mbps, 40Mbps, 10GB

(options, args) = parser.parse_args()
iperf3_monitoring_logger.info('Starting iperf3 monitoring with: ' + str(options))

# Results file formatting
date_and_time = datetime.datetime.now().strftime("%Y-%m-%d-%Hh-%Mm-%Ss")
experiment_path = 'measurements/iperf3/' + \
                  options.protocol + '/' + \
                  options.hostname + '_' + \
                  options.server_ip + '_' + \
                  str(date_and_time)

# Creating experiment folder
os.mkdir(experiment_path)

# Iperf3 command formatting
protocol_parameter = "-u" if options.protocol == "UDP" else ""

output_parameter = "--get-server-output" if options.output == "CMD" else \
    "-J >> " + options.protocol + "/" + options.hostname + ".json"

raw_results_filename = '/raw_result.txt'

terminal_command = ['iperf3', '-c', str(options.server_ip), protocol_parameter, '-p', str(options.server_port),
                    '-t', str(options.timeout), '-b', str(options.bandwidth), output_parameter, '-V', '--bind',
                    options.host_ip, '--logfile', experiment_path + raw_results_filename]

# TODO: measure latency with ping at the same time
# ex: ping -S 192.168.2.51 192.168.2.1


iperf3_monitoring_logger.info('Initializing iperf3 measurement!')
for i in range(0, options.measurements):
    iperf3_monitoring_logger.debug('Running experiment number: ' + str(i+1))
    with open(os.devnull, "w") as f:
        call(terminal_command, stdout=f)

iperf3_monitoring_logger.info('Iperf3 measurement done!')

# Parsing raw results
format_raw_results(experiment_path=experiment_path,
                   raw_results_filename=raw_results_filename,
                   options=options)

# Plotting graph results
make_iperf3_graphs(experiment_path=experiment_path,
                   options=options)
