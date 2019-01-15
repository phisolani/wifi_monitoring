#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2018, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

" Python script for making graphs with iperf3 CSV output"

import matplotlib.pyplot as plt
from configs.logger import *
import pandas as pd
import seaborn as sns


def make_graph(experiment_path, options):

    # Applying Seaborn style
    sns.set(style="whitegrid")

    # Reading iperf3 CSV results
    iperf3_data_dict = read_iperf3_server_results(experiment_path=experiment_path,
                                                  options=options)
    # Reading ICMP CSV results
    icmp_data_dict = read_icmp_server_results(experiment_path=experiment_path,
                                              options=options)
    # Plotting just the first values of the experiment
    while len(iperf3_data_dict['x_axis']['values']) > int(options.timeout):
        iperf3_data_dict['x_axis']['values'].pop()
        iperf3_data_dict['y1_axis']['values'].pop()
        if options.protocol == 'UDP':
            iperf3_data_dict['y2_axis']['values'].pop()
            iperf3_data_dict['y3_axis']['values'].pop()

    while len(icmp_data_dict['x_axis']['values']) > int(options.timeout):
        icmp_data_dict['x_axis']['values'].pop()
        icmp_data_dict['y1_axis']['values'].pop()

    if len(iperf3_data_dict['x_axis']['values']) != len(icmp_data_dict['x_axis']['values']):
        graphs_drawing_logger.error('Iperf3 and ICMP measurements have different length!')
        graphs_drawing_logger.error('Iperf3 -> length: ' + str(len(iperf3_data_dict['x_axis']['values'])) +
                                    ' data: ' + str(iperf3_data_dict))
        graphs_drawing_logger.error('ICMP -> length: ' + str(len(icmp_data_dict['x_axis']['values'])) +
                                    ' data: ' + str(icmp_data_dict))

    fig, host = plt.subplots(figsize=(16, 8), dpi=144)
    fig.subplots_adjust(right=0.75)

    par1 = host.twinx()
    if options.protocol == "UDP":
        par2 = host.twinx()
        par3 = host.twinx()

    # Offset the right spine of par2.  The ticks and label have already been
    # placed on the right by twinx above.
    if options.protocol == "UDP":
        par2.spines["right"].set_position(("axes", 1.1))
        par3.spines["right"].set_position(("axes", 1.2))

    # Having been created by twinx, par2 has its frame off, so the line of its
    # detached spine is invisible.  First, activate the frame but make the patch
    # and spines invisible.
    if options.protocol == "UDP":
        make_patch_spines_invisible(par2)
        make_patch_spines_invisible(par3)
        # Second, show the right spine.
        par2.spines["right"].set_visible(True)
        par3.spines["right"].set_visible(True)

    p1, = host.plot(iperf3_data_dict['x_axis']['values'], iperf3_data_dict['y1_axis']['values'], "b-", marker="D",
                    label=iperf3_data_dict['y1_axis']['label'])
    p2, = par1.plot(iperf3_data_dict['x_axis']['values'], icmp_data_dict['y1_axis']['values'], "-y", marker="o",
                    label=icmp_data_dict['y1_axis']['label'])
    if options.protocol == "UDP":
        p3, = par2.plot(iperf3_data_dict['x_axis']['values'], iperf3_data_dict['y2_axis']['values'], "r-", marker="s",
                        label=iperf3_data_dict['y2_axis']['label'])
        p4, = par3.plot(iperf3_data_dict['x_axis']['values'], iperf3_data_dict['y3_axis']['values'], "g-", marker="v",
                        label=iperf3_data_dict['y3_axis']['label'])

    axis_padding = 0.3  # percentage
    host.set_xlim(min(iperf3_data_dict['x_axis']['values']),
                  max(iperf3_data_dict['x_axis']['values']))
    host.set_ylim(0,
                  max(iperf3_data_dict['y1_axis']['values']) +
                  (max(iperf3_data_dict['y1_axis']['values'])*axis_padding))
    par1.set_ylim(0,
                  max(icmp_data_dict['y1_axis']['values']) +
                  (max(icmp_data_dict['y1_axis']['values']) * axis_padding))
    if options.protocol == "UDP":
        par2.set_ylim(0,
                      max(iperf3_data_dict['y2_axis']['values']) +
                      (max(iperf3_data_dict['y2_axis']['values'])*axis_padding))
        par3.set_ylim(0,
                      max(iperf3_data_dict['y3_axis']['values']) +
                      (max(iperf3_data_dict['y3_axis']['values'])*axis_padding))

        # Not formatting scales right now
        par3.yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))

    host.set_xlabel(iperf3_data_dict['x_axis']['label'])
    host.set_ylabel(iperf3_data_dict['y1_axis']['label'])
    par1.set_ylabel(icmp_data_dict['y1_axis']['label'])
    if options.protocol == "UDP":
        par2.set_ylabel(iperf3_data_dict['y2_axis']['label'])
        par3.set_ylabel(iperf3_data_dict['y3_axis']['label'])

    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())
    if options.protocol == "UDP":
        par2.yaxis.label.set_color(p3.get_color())
        par3.yaxis.label.set_color(p4.get_color())

    tkw = dict(size=4, width=1.5)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    if options.protocol == "UDP":
        par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
        par3.tick_params(axis='y', colors=p4.get_color(), **tkw)
        host.tick_params(axis='x', **tkw)

    lines = [p1, p2]
    if options.protocol == "UDP":
        lines.extend([p3, p4])

    # Title of the graph
    plt.title(options.hostname + ': Performance using ' + options.protocol + ', ' +
              options.bandwidth + ', over ' + str(options.timeout) + ' seconds')
    plt.legend(lines, [l.get_label() for l in lines])
    plt.savefig(experiment_path + '/' + options.hostname + '_results.png', format="png")
    plt.show()


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


def read_iperf3_server_results(experiment_path, options):
    # Common dict structure
    data_dict = {'x_axis': {'label': '', 'values': []},
                 'y1_axis': {'label': '', 'values': []}}
    if options.protocol == "UDP":
        data_dict['y2_axis'] = {'label': '', 'values': []}
        data_dict['y3_axis'] = {'label': '', 'values': []}

    df = pd.read_csv(experiment_path + '/' + options.hostname + '_iperf3_server_results.csv', sep=',', header=0)

    header_names = {'x_axis': 'Interval Until',
                    'y1_axis': 'Bandwidth'}

    if options.protocol == "UDP":
        header_names['y2_axis'] = 'Jitter'
        header_names['y3_axis'] = 'Loss Percentage'

    # Populating with the header fields
    for header_value in df.columns.values:
        for key, value in header_names.items():
            if value in header_value:
                data_dict[key]['label'] = header_value
                data_dict[key]['values'] = []

    # Populating with the values
    for index, row in df.iterrows():
        for key, value in data_dict.items():
            data_dict[key]['values'].append(row[value['label']])

    for key, value in data_dict.items():
        data_dict[key]['label'] = data_dict[key]['label'].replace('Interval Until', 'Time') \
            if 'Interval Until' in data_dict[key]['label'] else data_dict[key]['label']

    return data_dict


def read_icmp_server_results(experiment_path, options):
    data_dict = {'x_axis': {'label': '', 'values': []},
                 'y1_axis': {'label': '', 'values': []}}

    df = pd.read_csv(experiment_path + '/' + options.hostname + '_icmp_results.csv', sep=',', header=0)
    header_names = {'x_axis': 'ICMP Sequence', 'y1_axis': 'Latency'}

    # Populating with the header fields
    for header_value in df.columns.values:
        for key, value in header_names.items():
            if value in header_value:
                data_dict[key]['label'] = header_value
                data_dict[key]['values'] = []

    # Populating with the values
    for index, row in df.iterrows():
        for key, value in data_dict.items():
            data_dict[key]['values'].append(row[value['label']])

    return data_dict


def make_iperf3_graphs(experiment_path, options):
    iperf3_monitoring_logger.info('Making Iperf3 graphs!')
    # Making graph with UDP server results
    make_graph(experiment_path=experiment_path,
               options=options)
    iperf3_monitoring_logger.info('Done!')