#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__credits__ = "Carlos Donato"
__copyright__ = "Copyright 2018, The SDW Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

'''Packet types for monitoring IEEE 802.11 networks'''

from enum import Enum

# Channel frequencies
channel_frequencies = [2412, 2417, 2422, 2427, 2432, 2437, 2442, 2447, 2452, 2457, 2462, 2467, 2472, 2484]


class DeviceType(Enum):
    AP = 0
    STA = 1


class PacketType(Enum):
    MANAGEMENT = 0
    CONTROL = 1
    DATA = 2

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class PacketSubtype(Enum):
    # Management Frames
    ASSOCIATION_REQUEST = 0
    ASSOCIATION_RESPONSE = 1
    REASSOCIATION_REQUEST = 2
    REASSOCIATION_RESPONSE = 3
    PROBE_REQUEST = 4
    PROBE_RESPONSE = 5
    BEACON = 8
    ATIM = 9  # Announcement traffic indication map (ATIM)
    DISASSOCIATE = 10
    AUTHENTICATION = 11
    DEAUTHENTICATION = 12
    ACTION_FRAMES = 13

    # Control Frames
    #ARUBA_MANAGEMENT = 15  # ADDED NEW*
    #BEAMFORMING_REPORT_POLL = 20  # ADDED NEW*
    BLOCK_ACK_REQUEST = 24
    BLOCK_ACK = 25
    POWER_SAVE_POLL = 26
    REQUEST_TO_SEND = 27
    CLEAR_TO_SEND = 28
    ACK = 29
    CONTENTION_FREE_PERIOD_END = 30
    CONTENTION_FREE_PERIOD_END_ACK = 31

    # Data Frames
    DATA = 32
    DATA_CONTENTION_FREE_ACK = 33
    DATA_CONTENTION_FREE_POLL = 34
    DATA_CONTENTION_FREE_ACK_CONTENTION_FREE_POLL = 35
    NULL_DATA = 36
    NULL_DATA_CONTENTION_FREE_ACK = 37
    NULL_DATA_CONTENTION_FREE_POLL = 38
    NULL_DATA_CONTENTION_FREE_ACK_CONTENTION_FREE_POLL = 39
    QOS_DATA = 40
    QOS_DATA_CONTENTION_FREE_ACK = 41
    QOS_DATA_CONTENTION_FREE_POLL = 42
    QOS_DATA_CONTENTION_FREE_ACK_CONTENTION_FREE_POLL = 43
    NULL_QOS_DATA = 44
    NULL_QOS_DATA_CONTENTION_FREE_POLL = 46
    NULL_QOS_DATA_CONTENTION_FREE_ACK_CONTENTION_FREE_POLL = 47

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)

