#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2018, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

from models.wtp_stats import *
from configs.logger import *
import socket

import json


# Function to initialize WTPs aggregated stats file
def initialize_stats_files():
    try:
        live_capture_logger.info('Initializing WTPs stats files...')
        # TODO iterate over WTPs list
        wtp_aggregated_stats_file = open('stats/' + str(socket.gethostname()) + '.aggr.json', 'w+')
        wtp_aggregated_stats_file.write(str(json.dumps(WTPAggregatedStats().get(),
                                                       default=lambda o: o.__dict__['data'])))
        wtp_aggregated_stats_file.close()
    except:
        live_capture_logger.error('Error initializing stats files!')
    live_capture_logger.info('Stats files initialized!')


# Function to add WTPs raw stats into a file
def add_wtp_raw_stats_to_file(wtp_raw_stats):
    try:
        live_capture_logger.info('Adding WTP raw stats into file...')
        wtp_raw_stats_file = open('stats/' + str(socket.gethostname()) + '.raw.json', 'w+')
        wtp_raw_stats_file.write(str(json.dumps(wtp_raw_stats.get())))
        wtp_raw_stats_file.close()
    except:
        live_capture_logger.error('Error adding WTP raw stats into file!')
    live_capture_logger.info('WTP raw stats added!')


# Function to add WTPs aggregated stats into a file
def add_wtp_aggregated_stats_to_file(wtp_aggregated_stats):
    try:
        live_capture_logger.info('Adding WTP aggregated stats into file...')
        wtp_aggregated_stats_file = open('stats/' + str(socket.gethostname()) + '.aggr.json', 'w+')
        wtp_aggregated_stats_file.write(str(json.dumps(wtp_aggregated_stats, default=lambda o: o.__dict__['data'])))
        wtp_aggregated_stats_file.close()
    except:
        live_capture_logger.error('Error adding WTP aggregated stats into file!')
    live_capture_logger.info('WTP aggregated stats added!')