#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__credits__ = "Carlos Donato"
__copyright__ = "Copyright 2018, The SDW Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

'''Python script for monitoring IEEE 802.11 networks'''
import pyshark
import datetime
import os
import sys
from subprocess import call
import json

# Importing custom modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Adding root dir to sys.path
from models.packet_types import *
from handlers.files_handler import *
from configs.wtp_settings import *
from configs.logger import *

live_capture_logger.info('Starting live capture!')
call('ifconfig ' + wtp_interface + ' up', shell=True)  # Setting the WiFi card up
initialize_stats_files()  # Initializing stats file
wtp_aggregated_stats = WTPAggregatedStats()  # Defining wtp aggregated statistics dictionary

try:
    while True:
        # Creating the capture object
        cap = pyshark.LiveCapture(interface=wtp_interface, monitor_mode=monitor_mode)

        if monitoring_type == 'timeout':  # Mode based on timeout
            cap.sniff(timeout=monitoring_interval)
            cap = cap._packets  # To keep it generic on the for loop
        elif monitoring_type == 'per_packet':  # Mode based on the amount of packets monitored
            # TODO: Support mode based on amount of packets transmitted
            for packet in cap.sniff_continuously(packet_count=monitoring_packets_limit):
                live_capture_logger.info('Packet received!\n' + str(packet))
        else:
            cap = pyshark.FileCapture(monitoring_file)  # Mode based on an input file (.cap or .pcap)

        # TODO: check how this can be done (at the WTPs or Controller side?)
        #  Changing channel for the next iteration...
        #  call('iw dev ' + options.interface + ' set freq ' + random.choice(channel_frequencies), shell=True)

        wtp_raw_stats = WTPRawStats()                           # WTP statistics dictionary
        wtp_aggregated_packet_stats = WTPPacketCounters()       # WTP packet counters dictionary
        wtp_aggregated_data_stats = {}                          # WTP dictionary with WTPAggregatedDataStats()

        pkt_counter = 0
        print cap

        for pkt in cap:
            pkt_counter += 1
            crr_wtp_data_stats_key_fields = []  # WTP array with key fields BSS_ID, SRC, DST, TR, RC (all optional)
            crr_wtp_data_stats = WTPAggregatedDataStats()

            # Packet necessary fields
            packet_fields = ['radiotap', 'wlan']

            if set(packet_fields).issubset(set(dir(pkt))):
                # Checking packet type and subtype
                if PacketType.has_value(int(pkt.wlan.fc_type)):
                    pkt_type = PacketType(int(pkt.wlan.fc_type)).name
                else:
                    pkt_type = 'OTHER'

                wtp_aggregated_packet_stats.get()[pkt_type] += 1  # Adding wtp aggregated packets in dictionary

                if PacketSubtype.has_value(int(pkt.wlan.fc_type_subtype)):
                    pkt_subtype = PacketSubtype(int(pkt.wlan.fc_type_subtype)).name
                else:
                    pkt_subtype = 'UNKNOWN'

                if pkt_type == 'OTHER' or pkt_subtype == 'UNKNOWN':
                    live_capture_logger.warning('Unknown packet arrived!' +
                                                '\t TYPE=' + pkt.wlan.fc_type + ' ' + pkt_type +
                                                '\t SUBTYPE=' + pkt.wlan.fc_type_subtype + ' ' + pkt_subtype)

                # Printing packet types
                live_capture_logger.debug('PACKET=' + str(pkt_counter) +
                                          '\t TYPE=' + pkt.wlan.fc_type + ' ' + pkt_type +
                                          '\t SUBTYPE=' + pkt.wlan.fc_type_subtype + ' ' + pkt_subtype)

                if pkt_subtype not in wtp_raw_stats.get()[pkt_type]:
                    wtp_raw_stats.get()[pkt_type][pkt_subtype] = []

                # Getting RADIOTAP info
                packet_info = {'radiotap': {'header_length': int(pkt.radiotap.length),
                                            'packet_length': int(pkt.length),
                                            'channel': int(pkt.radiotap.present_channel),
                                            'mcs': int(pkt.radiotap.present_mcs),
                                            'noise': int(pkt.radiotap.present_db_antnoise),
                                            'signal': int(pkt.radiotap.present_db_antsignal),
                                            'data_rate': float(pkt.radiotap.datarate),
                                            'db_tx_attenuation': int(pkt.radiotap.present_db_tx_attenuation),
                                            'tx_attenuation': int(pkt.radiotap.present_tx_attenuation)}}

                # Getting WLAN info
                packet_info = {'wlan': {}}

                if 'wlan.bssid_resolved' in pkt.wlan._all_fields:
                    packet_info['wlan']['bss_id'] = pkt.wlan.bssid_resolved
                    crr_wtp_data_stats_key_fields.append(pkt.wlan.bssid_resolved)

                # Retrieving MAC Addresses
                if 'wlan.sa_resolved' in pkt.wlan._all_fields:
                    packet_info['wlan']['source_address'] = pkt.wlan.sa_resolved
                    crr_wtp_data_stats_key_fields.append(pkt.wlan.sa_resolved)

                if 'wlan.da_resolved' in pkt.wlan._all_fields:
                    packet_info['wlan']['destination_address'] = pkt.wlan.da_resolved
                    crr_wtp_data_stats_key_fields.append(pkt.wlan.da_resolved)

                if 'wlan.ta_resolved' in pkt.wlan._all_fields:
                    packet_info['wlan']['transmitter_address'] = pkt.wlan.ta_resolved
                    crr_wtp_data_stats_key_fields.append(pkt.wlan.ta_resolved)

                if 'wlan.ra_resolved' in pkt.wlan._all_fields:
                    packet_info['wlan']['receiver_address'] = pkt.wlan.ra_resolved
                    crr_wtp_data_stats_key_fields.append(pkt.wlan.ra_resolved)

                if 'wlan.seq' in pkt.wlan._all_fields:
                    packet_info['wlan']['sequence_number'] = int(pkt.wlan.seq)

                packet_info['wlan']['duration'] = int(pkt.wlan.duration)
                packet_info['wlan']['retry'] = int(pkt.wlan.fc_retry)

                # TODO: Calculate values on crr_wtp_data_stats
                if tuple(crr_wtp_data_stats_key_fields) not in wtp_aggregated_data_stats:
                    wtp_aggregated_data_stats[tuple(crr_wtp_data_stats_key_fields)] = crr_wtp_data_stats.get()

                print 'dictionary: ' + str(wtp_aggregated_data_stats)
                print 'dic json: ' + str(json.dumps(wtp_aggregated_data_stats,
                                                    default=lambda o: o.__dict__['data']))

                wtp_raw_stats.get()[pkt_type][pkt_subtype].append(packet_info)  # Adding to WTP RAW stats
            else:
                live_capture_logger.warning('Packet with different format arrived! ' + str(dir(pkt)))

        # Adding raw statistics into a stats file
        add_wtp_raw_stats_to_file(wtp_raw_stats=wtp_raw_stats)

        # Creating aggregated statistics file
        #wtp_aggregated_packet_stats.get()['TIME'] = str(datetime.datetime.now().time())
        wtp_aggregated_stats.get()['MEASUREMENTS']['PACKETS'].append(wtp_aggregated_packet_stats.get())
        #wtp_aggregated_stats.get()['MEASUREMENTS']['DATA'].append(wtp_aggregated_data_stats)
        wtp_aggregated_stats.get()['MEASUREMENTS']['TIME'].append(str(datetime.datetime.now().time()))
        add_wtp_aggregated_stats_to_file(wtp_aggregated_stats=wtp_aggregated_stats)

        # Change channel frequency
        # print random.choice(channel_frequencies)

except KeyboardInterrupt:
    live_capture_logger.info('Done!')