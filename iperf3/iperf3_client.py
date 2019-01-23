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
from subprocess import call, Popen
from optparse import OptionParser
from iperf3.iperf3_csv_parser import *
from iperf3.iperf3_graphs import *
from iperf3.icmp_csv_parser import *
from configs.logger import *

# Experimentation parameters and values
parser = OptionParser()
parser.add_option("", "--hostname", type="string", default="hostname")
parser.add_option("", "--host_ip", type="string", default="143.129.81.133")  # Host IP address
parser.add_option("", "--timeout", type="int", default=30)  # e.g., 30, 60 sec
parser.add_option("", "--measurements", type="int", default=1)
parser.add_option("", "--server_name", type="string", default="server")
parser.add_option("", "--server_ip", type="string", default="192.168.2.10")  # e.g., the DHCP server, WTP
parser.add_option("", "--server_port", type="int", default=5003)  # e.g., 5003, 5004
parser.add_option("", "--protocol", type="string", default="UDP")  # e.g., TCP, UDP
parser.add_option("", "--output", type="string", default="CMD")  # e.g., JSON, CMD
parser.add_option("", "--bandwidth", type="string", default="30Mbps")  # e.g., 0, 20Mbps, 40Mbps, 10GB
parser.add_option("", "--reverse_mode", default=True)  # e.g., True or False
parser.add_option("", "--plot_results", default=True)  # e.g., True or False

(options, args) = parser.parse_args()
iperf3_monitoring_logger.info('Starting iperf3 monitoring with: ' + str(options))

# Results file formatting
date_and_time = datetime.datetime.now().strftime("%Y-%m-%d-%Hh-%Mm-%Ss")
mode = "reverse_mode" if options.reverse_mode else "averse_mode"

experiment_path = 'measurements/iperf3/' + \
                  options.protocol + '/' + \
                  mode + '_' + \
                  options.hostname + '_' + \
                  options.server_ip + '_' + \
                  str(date_and_time)

# Creating experiment folder
os.mkdir(experiment_path)
f = open(experiment_path + "/experiment_parameters.txt", "w")
f.write(str(options))
f.close()

# Iperf3 command formatting
protocol_parameter = "-u" if options.protocol == "UDP" else ""

reverse_mode_parameter = "-R" if options.reverse_mode else ""

output_parameter = "--get-server-output" if options.output == "CMD" else \
    "-J >> " + options.protocol + "/" + options.hostname + ".json"

iperf3_raw_results_filename = '/' + str(options.hostname) + '_iperf3_raw_result.txt'
icmp_raw_results_filename = '/' + str(options.hostname) + '_icmp_raw_result.txt'

# Iperf3 terminal command
iperf3_terminal_command = ['iperf3', '-c', str(options.server_ip), protocol_parameter, '-p', str(options.server_port),
                           '-t', str(options.timeout), '-b', str(options.bandwidth), output_parameter, '-V',
                           reverse_mode_parameter, '--bind', options.host_ip, '--logfile', experiment_path +
                           iperf3_raw_results_filename]

# Ping terminal command for latency measurements
ping_terminal_command = ['ping', '-S', str(options.host_ip), '-c', str(options.timeout), str(options.server_ip)]

iperf3_monitoring_logger.info('Initializing iperf3 and ICMP measurements!')
for i in range(0, options.measurements):
    iperf3_monitoring_logger.debug('Running experiment number: ' + str(i+1))
    with open(experiment_path + icmp_raw_results_filename, 'w') as output:
        Popen(ping_terminal_command, stdout=output)
    with open(os.devnull, "w") as f:
        call(iperf3_terminal_command, stdout=f)
iperf3_monitoring_logger.info('Iperf3 and ICMP measurements done!')

# Parsing ICMP raw results
format_icmp_raw_results(experiment_path=experiment_path,
                        raw_results_filename=icmp_raw_results_filename,
                        options=options)

# Parsing iperf3 raw results

format_iperf3_raw_results(experiment_path=experiment_path,
                          raw_results_filename=iperf3_raw_results_filename,
                          options=options)

# Plotting graph results
if options.plot_results:
    make_iperf3_graphs(experiment_path=experiment_path,
                       options=options)
