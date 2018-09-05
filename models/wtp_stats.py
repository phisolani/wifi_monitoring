#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__credits__ = "Carlos Donato"
__copyright__ = "Copyright 2018, The SDW Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

'''WTP stats for monitoring IEEE 802.11 networks'''
from models.ring_buffer import RingBuffer
from configs.wtp_settings import *

import socket


class WTPRawStats:
    def __init__(self):
        self.data = {
            'NAME': wtp_name,
            'OPTIONS': {'INTERFACE': wtp_interface,
                        'HOSTNAME': socket.gethostname(),
                        'MONITOR_TYPE': monitoring_type,
                        'MONITORING_INTERVAL': monitoring_interval,
                        'MONITORING_PACKETS_LIMIT': monitoring_packets_limit,
                        'FILENAME': monitoring_file,
                        'BUFFER_SIZE': monitoring_ring_buffer_size},
            'MANAGEMENT': {},
            'CONTROL': {},
            'DATA': {},
            'OTHER': {}
        }

    def get(self):
        return self.data


# TODO: Use this structure...
class WTPAggregatedDataStats:
    def __init__(self):
        self.data = {
            'TR_BYTES': 0,          # total bytes transmitted
            'RC_BYTES': 0,          # total bytes received
            'TR_DATA_BYTES': 0,     # total bytes transmitted (excluding the headers)
            'RC_DATA_BYTES': 0,     # total bytes received (excluding the headers)
            'RETRIES': 0            # total number of retransmissions
        }


class WTPAggregatedStats:
    def __init__(self):
        self.data = {
            'NAME': wtp_name,
            'OPTIONS': {'INTERFACE': wtp_interface,
                        'HOSTNAME': socket.gethostname(),
                        'MONITOR_TYPE': monitoring_type,
                        'MONITORING_INTERVAL': monitoring_interval,
                        'MONITORING_PACKETS_LIMIT': monitoring_packets_limit,
                        'FILENAME': monitoring_file,
                        'BUFFER_SIZE': monitoring_ring_buffer_size},
            'MEASUREMENTS':
                {'PACKETS': RingBuffer(monitoring_ring_buffer_size),
                 'DATA': RingBuffer(monitoring_ring_buffer_size),  # filled with WTPAggregatedDataStats structure
                 'TIME': RingBuffer(monitoring_ring_buffer_size)}
        }

    def __str__(self):
        return str(self.data)

    def get(self):
        return self.data


class WTPPacketCounters:
    def __init__(self):
        self.data = {
            'MANAGEMENT': 0,
            'CONTROL': 0,
            'DATA': 0,
            'OTHER': 0
            # TODO: Include more packet counters!
            # Number of malformed packets
            # Number of dropped packets
            # Out of order?
        }

    def get(self):
        return self.data