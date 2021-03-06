#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2018, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

'''Python script for logging configurations'''

import logging

# Creating logs for apps and scripts
live_capture_logger = logging.getLogger('Live Capture')
wifi_monitoring_logger = logging.getLogger('WiFi Monitoring')
iperf3_monitoring_logger = logging.getLogger('Iperf3 Monitoring')
icmp_monitoring_logger = logging.getLogger('ICMP Monitoring')
graphs_drawing_logger = logging.getLogger('Graphs Drawing')

# Logging levels
live_capture_logger.setLevel(logging.INFO)
wifi_monitoring_logger.setLevel(logging.INFO)
iperf3_monitoring_logger.setLevel(logging.DEBUG)
icmp_monitoring_logger.setLevel(logging.DEBUG)
graphs_drawing_logger.setLevel(logging.DEBUG)

# Creating file handlers
live_capture_file_handler = logging.FileHandler('logs/live_capture.log')
wifi_monitoring_file_handler = logging.FileHandler('logs/wifi_monitoring.log')
iperf3_monitoring_file_handler = logging.FileHandler('logs/iperf3_monitoring.log')
icmp_monitoring_file_handler = logging.FileHandler('logs/icmp_monitoring.log')
graphs_drawing_file_handler = logging.FileHandler('logs/graphs_drawing.log')

# Setting the log levels
live_capture_file_handler.setLevel(logging.DEBUG)
wifi_monitoring_file_handler.setLevel(logging.DEBUG)
iperf3_monitoring_file_handler.setLevel(logging.DEBUG)
icmp_monitoring_file_handler.setLevel(logging.DEBUG)
graphs_drawing_file_handler.setLevel(logging.DEBUG)

# Creating console handlers with a higher log levels
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# Creating formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Assigning to the file and console handlers
live_capture_file_handler.setFormatter(formatter)
wifi_monitoring_file_handler.setFormatter(formatter)
iperf3_monitoring_file_handler.setFormatter(formatter)
icmp_monitoring_file_handler.setFormatter(formatter)
graphs_drawing_file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Adding the handlers to the loggers
live_capture_logger.addHandler(live_capture_file_handler)
live_capture_logger.addHandler(console_handler)

wifi_monitoring_logger.addHandler(wifi_monitoring_file_handler)
wifi_monitoring_logger.addHandler(console_handler)

iperf3_monitoring_logger.addHandler(iperf3_monitoring_file_handler)
iperf3_monitoring_logger.addHandler(console_handler)

icmp_monitoring_logger.addHandler(icmp_monitoring_file_handler)
icmp_monitoring_logger.addHandler(console_handler)

graphs_drawing_logger.addHandler(graphs_drawing_file_handler)
graphs_drawing_logger.addHandler(console_handler)