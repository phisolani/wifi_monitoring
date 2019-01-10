#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2018, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

" Python script for parsing ICMP output to CSV format "

from configs.logger import *
import csv
import re


def format_icmp_raw_results(experiment_path, raw_results_filename, options):
    wifi_monitoring_logger.debug('Parsing ICMP raw results on:' + str(experiment_path + raw_results_filename))
    # Reading raw results file
    with open(str(experiment_path + raw_results_filename), 'r') as file:
        # Instantiating auxiliary fields for ICMP results
        fieldnames = []
        values_section_flag = summary_section_flag = False

        # Opening result CSV file
        icmp_results_file = open(experiment_path + '/' + options.hostname + '_icmp_results.csv', 'w')
        icmp_summary_results_file = open(experiment_path + '/' + options.hostname + '_icmp_summary_results.csv', 'w')

        units = {'time': ''}

        # Iterating over raw results file
        for line in file:
            line = line.replace('\n', '')

            # Skipping blank lines
            if not line.strip(): continue

            # Header parsing
            if "PING" in line:
                tmp_line = open(str(experiment_path +
                                    raw_results_filename)).readlines()[1].replace('\n', '').split(' ')
                units['time'] = tmp_line[-1]

                fieldnames.append('Latency (' + units['time'] + ')')
                # Writing the header
                writer = csv.DictWriter(icmp_results_file, fieldnames=fieldnames)
                writer.writeheader()
                # Skip file header
                line = skip_file_lines(file=file, number_of_lines=1)
                values_section_flag = True

            # Values parsing
            if values_section_flag:
                if 'ping statistics' in line:
                    line = skip_file_lines(file=file, number_of_lines=1)
                    values_section_flag = False
                    summary_section_flag = True
                else:
                    row_dict_values = dict((k, '') for k in fieldnames)
                    row_dict_values[fieldnames[0]] = line.split(' ')[-2].split('=')[1]  # Latency value
                    # Write row values to file
                    writer.writerow(row_dict_values)

            # Summary parsing
            if summary_section_flag:
                fieldnames = ['Packets transmitted',
                              'Packets received',
                              'Packet Loss (%)',
                              'Round-trip min (' + units['time'] + ')',
                              'Round-trip avg (' + units['time'] + ')',
                              'Round-trip max (' + units['time'] + ')',
                              'Round-trip stddev (' + units['time'] + ')']
                # Writing the header
                writer = csv.DictWriter(icmp_summary_results_file, fieldnames=fieldnames)
                writer.writeheader()

                row_dict_values = dict((k, '') for k in fieldnames)

                # First Line
                tmp_line = re.split(' |%', line)
                row_dict_values[fieldnames[0]] = tmp_line[0]  # Packets transmitted
                row_dict_values[fieldnames[1]] = tmp_line[3]  # Packets received
                row_dict_values[fieldnames[2]] = tmp_line[6]  # Packet Loss

                line = skip_file_lines(file=file, number_of_lines=1)
                tmp_line = re.split(' |=', line)
                row_dict_values[fieldnames[3]] = tmp_line[-2].split('/')[0]  # Round-trip min
                row_dict_values[fieldnames[4]] = tmp_line[-2].split('/')[1]  # Round-trip avg
                row_dict_values[fieldnames[5]] = tmp_line[-2].split('/')[2]  # Round-trip max
                row_dict_values[fieldnames[6]] = tmp_line[-2].split('/')[3]  # Round-trip stddev

                # Write row values to file
                writer.writerow(row_dict_values)
                summary_section_flag = False

    # Closing CSV files
    icmp_results_file.close()
    icmp_summary_results_file.close()
    iperf3_monitoring_logger.debug('Parsing ICMP results done!')


def skip_file_lines(file, number_of_lines):
    line = ''
    for _ in range(number_of_lines):
        line = next(file)
    return line.replace('\n', '')