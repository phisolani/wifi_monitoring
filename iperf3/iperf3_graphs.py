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


def make_four_axis_graph(experiment_path, options):
    #sns.set(style="whitegrid")
    data_dict = read_iperf3_server_results(experiment_path=experiment_path,
                                           options=options)
    fig, host = plt.subplots()
    fig.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()

    # Offset the right spine of par2.  The ticks and label have already been
    # placed on the right by twinx above.
    par2.spines["right"].set_position(("axes", 1.2))
    # Having been created by twinx, par2 has its frame off, so the line of its
    # detached spine is invisible.  First, activate the frame but make the patch
    # and spines invisible.
    make_patch_spines_invisible(par2)
    # Second, show the right spine.
    par2.spines["right"].set_visible(True)

    p1, = host.plot(data_dict['x_axis']['values'],
                    data_dict['y1_axis']['values'], "b-",
                    label=data_dict['y1_axis']['label'])
    p2, = par1.plot(data_dict['x_axis']['values'],
                    data_dict['y2_axis']['values'], "r-",
                    label=data_dict['y2_axis']['label'])
    p3, = par2.plot(data_dict['x_axis']['values'],
                    data_dict['y3_axis']['values'], "g-",
                    label=data_dict['y3_axis']['label'])


    axis_padding = 0.1  # percentage

    host.set_xlim(min(data_dict['x_axis']['values']),
                  max(data_dict['x_axis']['values']))
    host.set_ylim(0,
                  max(data_dict['y1_axis']['values']) + (max(data_dict['y1_axis']['values'])*axis_padding))
    par1.set_ylim(0,
                  max(data_dict['y2_axis']['values']) + (max(data_dict['y2_axis']['values'])*axis_padding))
    par2.set_ylim(0,
                  max(data_dict['y3_axis']['values']) + (max(data_dict['y3_axis']['values'])*axis_padding))

    # Not formatting scales right now
    #par2.yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))

    host.set_xlabel(data_dict['x_axis']['label'])
    host.set_ylabel(data_dict['y1_axis']['label'])
    par1.set_ylabel(data_dict['y2_axis']['label'])
    par2.set_ylabel(data_dict['y3_axis']['label'])

    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())
    par2.yaxis.label.set_color(p3.get_color())

    tkw = dict(size=4, width=1.5)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    host.tick_params(axis='x', **tkw)

    lines = [p1, p2, p3]

    host.legend(lines, [l.get_label() for l in lines])

    plt.savefig(experiment_path + '/' + options.hostname + '_server_results.png')
    plt.show()


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


def read_iperf3_server_results(experiment_path, options):
    data_dict = {'x_axis': {'label': '', 'values': []},
                 'y1_axis': {'label': '', 'values': []},
                 'y2_axis': {'label': '', 'values': []},
                 'y3_axis': {'label': '', 'values': []}}

    df = pd.read_csv(experiment_path + '/' + options.hostname + '_iperf3_server_results.csv', sep=',', header=0)
    header_names = {'x_axis': 'Interval Until',
                    'y1_axis': 'Bandwidth',
                    'y2_axis': 'Jitter',
                    'y3_axis': 'Loss Percentage'}

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


def make_iperf3_graphs(experiment_path, options):
    iperf3_monitoring_logger.info('Making Iperf3 graphs!')
    # Making graph with UDP server results
    if options.protocol == "UDP":
        make_four_axis_graph(experiment_path=experiment_path,
                             options=options)
    iperf3_monitoring_logger.info('Done!')