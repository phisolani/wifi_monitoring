#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2018, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

" Python script for parsing iperf3 output to CSV format "

from configs.logger import *
import csv
import re


def format_iperf3_raw_results(experiment_path, raw_results_filename, options):
    iperf3_monitoring_logger.debug('Parsing Iperf3 raw results on:' + str(experiment_path + raw_results_filename))
    # Reading raw results file
    with open(str(experiment_path + raw_results_filename), 'r') as file:
        # Instantiating auxiliary fields for client and server-side results
        fieldnames = []
        cli_header_section_flag = cli_values_section_flag = cli_summary_section_flag = False
        serv_header_section_flag = serv_values_section_flag = serv_summary_section_flag = False

        # Opening result CSV files
        csv_cli_file = open(experiment_path + '/' + options.hostname + '_iperf3_client_results.csv', 'w')
        csv_cli_summary_file = open(experiment_path + '/' + options.hostname + '_iperf3_client_summary_results.csv', 'w')
        csv_serv_file = open(experiment_path + '/' + options.hostname + '_iperf3_server_results.csv', 'w')
        csv_serv_summary_file = open(experiment_path + '/' + options.hostname + '_iperf3_server_summary_results.csv', 'w')

        summaries = []
        units = {'time': '', 'transfer': '', 'rate': '', 'jitter':''}

        # Iterating over raw results file
        for line in file:
            line = line.replace('\n', '')
            if "Starting Test" in line:
                cli_header_section_flag = True

            # Writing Cli Results CSV header
            if cli_header_section_flag:
                tmp_unit_line = 8
                if options.protocol == "TCP":
                    tmp_unit_line = 9
                # Getting header units
                tmp_line = re.split(',', re.sub("\s+", ",", open(str(experiment_path + raw_results_filename)).readlines()[tmp_unit_line].strip()))

                units['time'] = tmp_line[3]
                units['transfer'] = tmp_line[5]
                units['rate'] = tmp_line[7]

                fieldnames.append('Interval From (' + units['time'] + ')')
                fieldnames.append('Interval Until (' + units['time'] + ')')
                fieldnames.append('Transfer (' + units['transfer'] + ')')
                fieldnames.append('Bitrate (' + units['rate'] + ')')

                if options.protocol == "UDP":
                    fieldnames.append('Total Datagrams')  # no need to update units

                writer = csv.DictWriter(csv_cli_file, fieldnames=fieldnames)
                writer.writeheader()
                # Skip file header
                line = skip_file_lines(file=file, number_of_lines=2)
                cli_header_section_flag = False
                cli_values_section_flag = True

            if cli_values_section_flag:
                if "- - - - - - - - - - - - - - - - - -" in line:
                    # Skip lines to the summary
                    line = skip_file_lines(file=file, number_of_lines=3)

                    # Remove total datagrams from fieldnames
                    if options.protocol == "UDP":
                        fieldnames.pop()
                        units['jitter'] = re.split(',', re.sub("\s+", ",", line.strip()))[9]
                        fieldnames.extend(['Jitter (' + units['jitter'] + ')',
                                           'Lost Datagrams',
                                           'Total Datagrams',
                                           'Loss Percentage (%)'])

                    # Preparing fieldnames for summary data
                    fieldnames.extend(['Sender/Receiver',
                                       'CPU Utilization (overall)',
                                       'CPU Utilization (user)',
                                       'CPU Utilization (system)'])

                    summaries = {'sender': dict((k, '') for k in fieldnames),
                                 'receiver': dict((k, '') for k in fieldnames)}  # sender/receiver

                    summaries['sender']['Sender/Receiver'] = 'sender'
                    summaries['receiver']['Sender/Receiver'] = 'receiver'

                    # Writing header on CSV file
                    writer = csv.DictWriter(csv_cli_summary_file, fieldnames=fieldnames)
                    writer.writeheader()

                    cli_values_section_flag = False
                    cli_summary_section_flag = True
                else:
                    row_dict_values = dict((k, '') for k in fieldnames)
                    tmp_line = re.split(',', re.sub("\s+", ",", line.strip()))

                    row_dict_values[fieldnames[0]] = tmp_line[2].split('-')[0]  # Interval From
                    row_dict_values[fieldnames[1]] = tmp_line[2].split('-')[1]  # Interval Until
                    row_dict_values[fieldnames[2]] = tmp_line[4]  # Transfer
                    row_dict_values[fieldnames[3]] = tmp_line[6]  # Bitrate

                    if options.protocol == "UDP":
                        row_dict_values[fieldnames[4]] = tmp_line[8]

                    # Write row values to file
                    writer.writerow(row_dict_values)

            if cli_summary_section_flag:
                iperf3_monitoring_logger.debug(line.split(' '))

                if 'CPU Utilization' in line:
                    tmp_line = re.split('CPU Utilization: local/sender | %|% |%| \(|s\)|\(| remote/receiver | |u/', line)

                    # Sender
                    summaries['sender']['CPU Utilization (overall)'] = tmp_line[1]  # Overall
                    summaries['sender']['CPU Utilization (user)'] = tmp_line[3]  # User
                    summaries['sender']['CPU Utilization (system)'] = tmp_line[5]  # System

                    # Receiver
                    summaries['receiver']['CPU Utilization (overall)'] = tmp_line[8]  # Overall
                    summaries['receiver']['CPU Utilization (user)'] = tmp_line[10]  # User
                    summaries['receiver']['CPU Utilization (system)'] = tmp_line[12]  # System

                    writer.writerow(summaries['sender'])
                    writer.writerow(summaries['receiver'])

                    line = skip_file_lines(file=file, number_of_lines=9)

                    cli_summary_section_flag = False
                    serv_header_section_flag = True
                else:
                    tmp_line = re.split(',', re.sub("\s+", ",", line.strip()))
                    tmp_sender_or_receiver_column = -1
                    if options.protocol == 'UDP':
                        summaries[tmp_line[tmp_sender_or_receiver_column]][fieldnames[4]] = tmp_line[8]  # Jitter
                        summaries[tmp_line[tmp_sender_or_receiver_column]][fieldnames[5]] = tmp_line[10].split('/')[
                        0]  # Lost Datagrams
                        summaries[tmp_line[tmp_sender_or_receiver_column]][fieldnames[6]] = tmp_line[10].split('/')[
                        1]  # Total Datagrams
                        summaries[tmp_line[tmp_sender_or_receiver_column]][fieldnames[7]] = tmp_line[11].strip('(%)')
                        # Percentage

                    summaries[tmp_line[tmp_sender_or_receiver_column]][fieldnames[0]] = tmp_line[2].split('-')[
                        0]  # Interval From
                    summaries[tmp_line[tmp_sender_or_receiver_column]][fieldnames[1]] = tmp_line[2].split('-')[
                        1]  # Interval Until

                    summaries[tmp_line[tmp_sender_or_receiver_column]][fieldnames[2]] = tmp_line[4]  # Transfer
                    summaries[tmp_line[tmp_sender_or_receiver_column]][fieldnames[3]] = tmp_line[6]  # Bitrate

            if serv_header_section_flag:
                fieldnames = [fieldnames[0], fieldnames[1], fieldnames[2], 'Bandwidth (' + units['rate'] + ')']
                if options.protocol == 'UDP':
                    fieldnames.extend(['Jitter (' + units['jitter'] + ')',
                                       'Lost Datagrams',
                                       'Total Datagrams',
                                       'Loss Percentage (%)',
                                       'Out-of-order (datagrams)',
                                       'Out-of-order From (' + units['time'] + ')',
                                       'Out-of-order Until (' + units['time'] + ')'])

                writer = csv.DictWriter(csv_serv_file, fieldnames=fieldnames)
                writer.writeheader()

                serv_header_section_flag = False
                serv_values_section_flag = True

            if serv_values_section_flag:
                if "- - - - - - - - - - - - - - - - - -" in line:
                    # Skip lines to the summary
                    line = skip_file_lines(file=file, number_of_lines=2)

                    if options.protocol == "TCP":
                        fieldnames.append('Sender/Receiver')

                    # Writing header on CSV file
                    writer = csv.DictWriter(csv_serv_summary_file, fieldnames=fieldnames)
                    writer.writeheader()

                    serv_values_section_flag = False
                    serv_summary_section_flag = True
                else:
                    row_dict_values = dict((k, '') for k in fieldnames)
                    tmp_line = re.split(',', re.sub("\s+", ",", line.strip()))

                    if options.protocol == "UDP":
                        row_dict_values[fieldnames[4]] = tmp_line[8]  # Jitter
                        row_dict_values[fieldnames[5]] = tmp_line[10].split('/')[0]  # Lost Datagrams
                        row_dict_values[fieldnames[6]] = tmp_line[10].split('/')[1]  # Total Datagrams
                        row_dict_values[fieldnames[7]] = tmp_line[11].strip('(%)')  # Percentage

                    row_dict_values[fieldnames[0]] = tmp_line[2].split('-')[0]  # Interval From
                    row_dict_values[fieldnames[1]] = tmp_line[2].split('-')[1]  # Interval Until
                    row_dict_values[fieldnames[2]] = tmp_line[4]  # Transfer
                    row_dict_values[fieldnames[3]] = tmp_line[6]  # Bandwidth

                    # Write row values to file
                    writer.writerow(row_dict_values)

            if serv_summary_section_flag:
                if line.strip():
                    row_dict_values = dict((k, '') for k in fieldnames)
                    tmp_line = re.split(',', re.sub("\s+", ",", line.strip()))
                    if tmp_line[0] == "[SUM]":
                        row_dict_values[fieldnames[8]] = tmp_line[3]  # Out-of-order (datagrams)
                        row_dict_values[fieldnames[9]] = tmp_line[1].split('-')[0]  # Out-of-order From
                        row_dict_values[fieldnames[10]] = tmp_line[1].split('-')[1]  # Out-of-order Until
                    else:
                        if options.protocol == "TCP":
                            row_dict_values[fieldnames[4]] = tmp_line[-1]  # Sender/Receiver
                        else:  # UDP
                            row_dict_values[fieldnames[4]] = tmp_line[8]  # Jitter
                            row_dict_values[fieldnames[5]] = tmp_line[10].split('/')[0]  # Lost Datagrams
                            row_dict_values[fieldnames[6]] = tmp_line[10].split('/')[1]  # Total Datagrams
                            row_dict_values[fieldnames[7]] = tmp_line[11].strip('(%)')  # Percentage
                            row_dict_values[fieldnames[8]] = 0  # Out-of-order (datagrams)
                            row_dict_values[fieldnames[9]] = 0  # Out-of-order From
                            row_dict_values[fieldnames[10]] = 0  # Out-of-order Until

                        row_dict_values[fieldnames[0]] = tmp_line[2].split('-')[0]  # Interval From
                        row_dict_values[fieldnames[1]] = tmp_line[2].split('-')[1]  # Interval Until
                        row_dict_values[fieldnames[2]] = tmp_line[4]  # Transfer
                        row_dict_values[fieldnames[3]] = tmp_line[6]  # Bandwidth

                        # Write row values to file
                        writer.writerow(row_dict_values)
                else:
                    serv_summary_section_flag = False
    # Closing CSV files
    csv_cli_file.close()
    csv_cli_summary_file.close()
    csv_serv_file.close()
    csv_serv_summary_file.close()
    iperf3_monitoring_logger.debug('Parsing Iperf3 results done!')


def skip_file_lines(file, number_of_lines):
    line = ''
    for _ in range(number_of_lines):
        line = next(file)
    return line.replace('\n', '')