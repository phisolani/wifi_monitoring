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
from optparse import OptionParser
from definitions.packet_types import *
from handlers.files_handler import *


# TODO: load it from a configuration file where all WTPs have to be configured
# Parameters from shell (only for testing)
parser = OptionParser()
parser.add_option("", "--interface", type="string", default="en0")
parser.add_option("", "--mode", type="string", default="time")  # other options are: per_packet, file, and time
parser.add_option("", "--timeout", type="int", default=5)
parser.add_option("", "--packets", type="int", default=300)
parser.add_option("", "--filename", type="string", default='traces/test2.pcap')
parser.add_option("", "--buffer_size", type="int", default=10)

(options, args) = parser.parse_args()

live_capture_logger.info('Starting live capture with: ' + str(options))

initialize_stats_files(options)  # Initializing stats file
wtp_aggregated_stats = WTPAggregatedStats(wtp_name='WTP1', options=options)  # Defining wtp aggregated statistics dictionary


try:
    while True:
        # Creating the capture object
        cap = pyshark.LiveCapture(interface=options.interface, monitor_mode=True)

        if options.mode == 'time':  # Mode based on timeout
            cap.sniff(timeout=options.timeout)
            cap = cap._packets  # To keep it generic on the for loop
        elif options.mode == 'per_packet':  # Mode based on the amount of packets monitored
            # TODO: Support mode based on amount of packets transmitted
            for packet in cap.sniff_continuously(packet_count=options.packets):
                live_capture_logger.info('Packet received!\n' + str(packet))
        else:
            cap = pyshark.FileCapture(options.filename)  # Mode based on an input file (.cap or .pcap)

        # TODO: check how this can be done (at the WTPs or Controller side?)
        #  Changing channel for the next iteration...
        #  call('iw dev ' + options.interface + ' set freq ' + random.choice(channel_frequencies), shell=True)

        wtp_raw_stats = WTPRawStats(options=options)  # Defining wtp statistics dictionary
        crr_aggregated_packet_stats = WTPPacketCounters()  # Creating wtp packet counters dictionary
        pkt_counter = 0
        print cap

        for pkt in cap:
            pkt_counter += 1

            # Packet necessary fields
            packet_fields = ['radiotap', 'wlan', 'wlan_radio', 'frame_info']

            if set(packet_fields).issubset(set(dir(pkt))):
                # Checking packet type and subtype
                if PacketType.has_value(int(pkt.wlan.fc_type)):
                    pkt_type = PacketType(int(pkt.wlan.fc_type)).name
                else:
                    pkt_type = 'OTHER'

                crr_aggregated_packet_stats.get()[pkt_type] += 1  # Adding wtp aggregated packets in dictionary

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

                # Retrieving RSSI
                if 'wlan_radio.signal_dbm' in pkt.wlan_radio._all_fields:
                    rssi = int(pkt.wlan_radio.signal_dbm)
                else:
                    rssi = 'null'

                packet_info = {'wlan': {}}

                # Retrieving MAC Addresses
                if 'wlan.sa_resolved' in pkt.wlan._all_fields:
                    packet_info['wlan']['source_address'] = pkt.wlan.sa_resolved

                if 'wlan.da_resolved' in pkt.wlan._all_fields:
                    packet_info['wlan']['destination_address'] = pkt.wlan.da_resolved

                if 'wlan.ta_resolved' in pkt.wlan._all_fields:
                    packet_info['wlan']['transmitter_address'] = pkt.wlan.ta_resolved

                if 'wlan.ra_resolved' in pkt.wlan._all_fields:
                    packet_info['wlan']['receiver_address'] = pkt.wlan.ra_resolved

                if 'wlan.bssid_resolved' in pkt.wlan._all_fields:
                    packet_info['wlan']['bss_id'] = pkt.wlan.bssid_resolved

                # Getting general info
                packet_info['radiotap'] = {'header_length': int(pkt.radiotap.length),
                                           'packet_length': int(pkt.length)}
                packet_info['wlan_radio'] = {'channel': pkt.wlan_radio.channel,
                                             'data_rate': float(pkt.wlan_radio.data_rate),
                                             'duration': int(pkt.wlan_radio.duration),
                                             'frequency': pkt.wlan_radio.frequency,
                                             'rssi': rssi}

                if 'wlan_radio.noise_dbm' in pkt.wlan_radio._all_fields:
                    packet_info['wlan_radio']['noise_level'] = int(pkt.wlan_radio.noise_dbm)

                if 'wlan.fc.retry' in pkt.wlan._all_fields:
                    packet_info['wlan_radio']['retry'] = int(pkt.wlan.fc_retry)

                if 'wlan.seq' in pkt.wlan._all_fields:
                    packet_info['wlan']['sequence_number'] = int(pkt.wlan.seq)
                    packet_info['wlan']['time_epoch'] = float(pkt.frame_info.time_epoch)

                wtp_raw_stats.get()[pkt_type][pkt_subtype].append(packet_info)
                # print json.dumps(wtp_raw_stats)
            else:
                live_capture_logger.warning('Packet with different format arrived! ' + str(pkt))

        # Adding raw statistics into a stats file
        add_wtp_raw_stats_to_file(wtp_raw_stats=wtp_raw_stats)

        # Creating aggregated statistics file
        crr_aggregated_packet_stats.get()['TIME'] = str(datetime.datetime.now().time())
        wtp_aggregated_stats.get()['MEASUREMENTS']['PACKETS'].append(crr_aggregated_packet_stats.get())
        add_wtp_aggregated_stats_to_file(wtp_aggregated_stats=wtp_aggregated_stats)

        # Change channel frequency
        # print random.choice(channel_frequencies)

except KeyboardInterrupt:
    live_capture_logger.info('Done!')