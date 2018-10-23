#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__credits__ = "Carlos Donato"
__copyright__ = "Copyright 2018, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

'''Ring buffer for monitoring IEEE 802.11 networks'''


class RingBuffer:
    def __init__(self, size):
        self.data = [None for i in xrange(size)]

    def __str__(self):
        return str(self.data)

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data