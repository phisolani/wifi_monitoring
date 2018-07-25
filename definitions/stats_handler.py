#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__credits__ = "Carlos Donato"
__copyright__ = "Copyright 2018, The SDW Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

'''Stats types for monitoring IEEE 802.11 networks'''
from models.ring_buffer import RingBuffer


class WTPRawStats:
    def __init__(self, options):
        self.data = {
            'NAME': 'WTP1',
            'OPTIONS': {'INTERFACE': options.interface,
                        'MODE': options.mode,
                        'TIMEOUT': options.timeout,
                        'PACKETS': options.packets,
                        'FILENAME': options.filename,
                        'BUFFER_SIZE': options.buffer_size},
            'MANAGEMENT': {},
            'CONTROL': {},
            'DATA': {},
            'OTHER': {}
        }

    def get(self):
        return self.data


class WTPAggregatedStats:
    def __init__(self, wtp_name, options):
        self.data = {
            'WTPS': [
                {'NAME': wtp_name,
                 'OPTIONS': {'INTERFACE': options.interface,
                             'MODE': options.mode,
                             'TIMEOUT': options.timeout,
                             'PACKETS': options.packets,
                             'FILENAME': options.filename,
                             'BUFFER_SIZE': options.buffer_size
                             },
                 'MEASUREMENTS':
                     {'PACKETS': RingBuffer(options.buffer_size)}
                 }
            ]
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
        }

    def get(self):
        return self.data