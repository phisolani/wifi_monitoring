#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__credits__ = "Carlos Donato"
__copyright__ = "Copyright 2018, The SDW Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

'''Python script for general settings'''
from configs.logger import *

import ConfigParser

# WiFi Monitoring application settings
wtp_name = None
wtp_interface = None
monitor_mode = None
monitoring_type = None
monitoring_interval = None
monitoring_packets_limit = None
monitoring_file = None
monitoring_ring_buffer_size = None

# OpenCAPWAP settings
opencapwap_path = None

try:
    wifi_monitoring_logger.info('Loading local_settings.ini...')
    # Parsing local_settings.ini
    config = ConfigParser.SafeConfigParser()
    config.read(application_path + '/configs/local_settings.ini')
    if config.has_section('WTP'):
        if config.has_option('WTP', 'wtp_name'):
            wtp_name = config.get('WTP', 'wtp_name')
        if config.has_option('WTP', 'wtp_interface'):
            wtp_interface = config.get('WTP', 'wtp_interface')
    if config.has_section('WiFi Monitoring'):
        if config.has_option('WiFi Monitoring', 'monitor_mode'):
            if config.get('WiFi Monitoring', 'monitor_mode') == 'yes':
                monitor_mode = True
            else:
                monitor_mode = False
        if config.has_option('WiFi Monitoring', 'monitoring_type'):
            monitoring_type = config.get('WiFi Monitoring', 'monitoring_type')
        if config.has_option('WiFi Monitoring', 'monitoring_interval'):
            monitoring_interval = int(config.get('WiFi Monitoring', 'monitoring_interval'))
        if config.has_option('WiFi Monitoring', 'monitoring_packets_limit'):
            monitoring_packets_limit = int(config.get('WiFi Monitoring', 'monitoring_packets_limit'))
        if config.has_option('WiFi Monitoring', 'monitoring_file'):
            monitoring_file = config.get('WiFi Monitoring', 'monitoring_file')
        if config.has_option('WiFi Monitoring', 'monitoring_ring_buffer_size'):
            monitoring_ring_buffer_size = int(config.get('WiFi Monitoring', 'monitoring_ring_buffer_size'))
    if config.has_section('OpenCAPWAP'):
        if config.has_option('OpenCAPWAP', 'path'):
            opencapwap_path = config.get('OpenCAPWAP', 'path')
except:
    wifi_monitoring_logger.error('Error loading local_settings.ini!')
wifi_monitoring_logger.info('Local settings successfully loaded!')