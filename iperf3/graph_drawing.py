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

# Experimentation parameters and values
parser = OptionParser()
parser.add_option("", "--hostname", type="string", default="hostname")
parser.add_option("", "--host_ip", type="string", default="192.168.2.51")
parser.add_option("", "--timeout", type="int", default=60)  # e.g., 30, 60 sec
parser.add_option("", "--measurements", type="int", default=1)
parser.add_option("", "--server_ip", type="string", default="192.168.2.1")  # e.g., the DHCP server
parser.add_option("", "--server_port", type="int", default=5003)  # e.g., 5003, 5004
parser.add_option("", "--protocol", type="string", default="TCP")  # e.g., TCP, UDP
parser.add_option("", "--output", type="string", default="CMD")  # e.g., JSON, CMD
parser.add_option("", "--bandwidth", type="string", default="30Mbps")  # e.g., 0, 20Mbps, 40Mbps, 10GB
parser.add_option("", "--experiment_path", type="string",
                  default="/Users/.../hostname_192.168.2.1_2019-01-11-14h-04m-44s")  # results folder path

(options, args) = parser.parse_args()

graphs_drawing_logger.info('Starting iperf3/ICMP graph drawing with: ' + str(options))
make_iperf3_graphs(experiment_path=options.experiment_path,
                   options=options)
graphs_drawing_logger.info('Done!')