#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2018, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"


''' Python script for generating graphs for iperf3 and ICMP '''

from optparse import OptionParser
from iperf3.iperf3_graphs import *
from iperf3.icmp_csv_parser import *
from iperf3.iperf3_csv_parser import *

# Experimentation parameters and values
parser = OptionParser()
parser.add_option("", "--hostname", type="string", default="hostname")
parser.add_option("", "--host_ip", type="string", default="192.168.2.51")
parser.add_option("", "--timeout", type="int", default=30)  # e.g., 30, 60 sec
parser.add_option("", "--measurements", type="int", default=1)
parser.add_option("", "--server_ip", type="string", default="192.168.2.1")  # e.g., the DHCP server
parser.add_option("", "--server_port", type="int", default=5003)  # e.g., 5003, 5004
parser.add_option("", "--protocol", type="string", default="UDP")  # e.g., TCP, UDP
parser.add_option("", "--output", type="string", default="CMD")  # e.g., JSON, CMD
parser.add_option("", "--bandwidth", type="string", default="30Mbps")  # e.g., 0, 20Mbps, 40Mbps, 10GB
parser.add_option("", "--experiment_path", type="string",
                  default="/Users/.../wifi_monitoring/measurements/iperf3/UDP/<experiment_folder>")  # results folder

(options, args) = parser.parse_args()

iperf3_raw_results_filename = '/' + str(options.hostname) + '_iperf3_raw_result.txt'
icmp_raw_results_filename = '/' + str(options.hostname) + '_icmp_raw_result.txt'

# Parsing ICMP raw results
format_icmp_raw_results(experiment_path=options.experiment_path,
                        raw_results_filename=icmp_raw_results_filename,
                        options=options)

# Parsing iperf3 raw results
format_iperf3_raw_results(experiment_path=options.experiment_path,
                          raw_results_filename=iperf3_raw_results_filename,
                          options=options)

graphs_drawing_logger.info('Starting iperf3/ICMP graph drawing with: ' + str(options))
make_iperf3_graphs(experiment_path=options.experiment_path,
                   options=options)
graphs_drawing_logger.info('Done!')