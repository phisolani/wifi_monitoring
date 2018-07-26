#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__credits__ = "Carlos Donato"
__copyright__ = "Copyright 2018, The SDW Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

'''Python script for logging configurations'''

from configs.common_settings import *

import logging

# Creating logs for apps and scripts
live_capture_logger = logging.getLogger('Live Capture')
wifi_monitoring_logger = logging.getLogger('WiFi Monitoring')

# Logging levels
live_capture_logger.setLevel(logging.INFO)
wifi_monitoring_logger.setLevel(logging.INFO)

# Creating file handlers
live_capture_file_handler = logging.FileHandler(application_path + '/logs/live_capture.log')
wifi_monitoring_file_handler = logging.FileHandler(application_path + '/logs/wifi_monitoring.log')

# Setting the log levels
live_capture_file_handler.setLevel(logging.DEBUG)
wifi_monitoring_file_handler.setLevel(logging.DEBUG)

# Creating console handlers with a higher log levels
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# Creating formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Assigning to the file and console handlers
live_capture_file_handler.setFormatter(formatter)
wifi_monitoring_file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Adding the handlers to the loggers
live_capture_logger.addHandler(live_capture_file_handler)
live_capture_logger.addHandler(console_handler)

wifi_monitoring_logger.addHandler(wifi_monitoring_file_handler)
wifi_monitoring_logger.addHandler(console_handler)