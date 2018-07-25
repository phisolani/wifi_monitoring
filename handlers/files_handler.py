#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__credits__ = "Carlos Donato"
__copyright__ = "Copyright 2018, The SDW Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"


from configs.logger import *
from definitions.stats_handler import *
import json


# Function to initialize WTPs aggregated stats file
def initialize_stats_files(options):
    try:
        live_capture_logger.info('Initializing WTPs stats files...')
        # TODO iterate over WTPs list
        wtp_aggregated_stats_file = open('stats/wtp1_aggregated_stats.json', 'w+')
        wtp_aggregated_stats_file.write(str(json.dumps(WTPAggregatedStats(wtp_name='WTP1', options=options).get(),
                                                       default=lambda o: o.__dict__['data'])))
        wtp_aggregated_stats_file.close()
    except:
        live_capture_logger.error('Error initializing stats files!')
    live_capture_logger.info('Stats files initialized!')


def add_wtp_raw_stats_to_file(wtp_raw_stats):
    try:
        live_capture_logger.info('Adding WTP raw stats into file...')
        wtp_raw_stats_file = open('stats/wtp1_raw_stats.json', 'w+')
        wtp_raw_stats_file.write(str(json.dumps(wtp_raw_stats.get())))
        wtp_raw_stats_file.close()
    except:
        live_capture_logger.error('Error adding WTP raw stats into file!')
    live_capture_logger.info('WTP raw stats added!')


def add_wtp_aggregated_stats_to_file(wtp_aggregated_stats):
    try:
        live_capture_logger.info('Adding WTP aggregated stats into file...')
        wtp_aggregated_stats_file = open('stats/wtp1_aggregated_stats.json', 'w+')
        wtp_aggregated_stats_file.write(str(json.dumps(wtp_aggregated_stats, default=lambda o: o.__dict__['data'])))
        wtp_aggregated_stats_file.close()
    except:
        live_capture_logger.error('Error adding WTP aggregated stats into file!')
    live_capture_logger.info('WTP aggregated stats added!')