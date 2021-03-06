#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2018, The SDN WiFi MAC Manager"
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


class WTPAggregatedDataStats:
    def __init__(self, packet_type, packet_subtype):
        self.data = {
            'PACKET_TYPE': packet_type,         # packet type
            'PACKET_SUBTYPE': packet_subtype,   # packet subtype
            'PACKET_COUNTER': 0,                # packet counter
            'TR_BYTES': 0,                      # total bytes transmitted
            'TR_DATA_BYTES': 0,                 # total bytes transmitted (excluding the headers)
            'RETRIES': 0                        # total number of retransmissions
        }

    def get(self):
        return self.data


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