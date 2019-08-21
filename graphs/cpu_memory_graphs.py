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


def make_graph(filename, title):

    # Applying Seaborn style
    sns.set(style="whitegrid")

    # Reading iperf3 CSV results
    cpu_load_data_dict = read_cpu_results(filename=filename)
    # Reading ICMP CSV results
    memory_data_dict = read_memory_results(filename=filename)

    # Plotting just the first values of the experiment
    fig, host = plt.subplots(figsize=(16, 8), dpi=144)
    fig.subplots_adjust(right=0.75)

    par1 = host.twinx()

    # Offset the right spine of par2.  The ticks and label have already been
    # placed on the right by twinx above.
    # Having been created by twinx, par2 has its frame off, so the line of its
    # detached spine is invisible.  First, activate the frame but make the patch
    # and spines invisible.
    p1, = host.plot(cpu_load_data_dict['x_axis']['values'], cpu_load_data_dict['y1_axis']['values'], "b-", marker="D",
                    label=cpu_load_data_dict['y1_axis']['label'])
    p2, = par1.plot(cpu_load_data_dict['x_axis']['values'], memory_data_dict['y1_axis']['values'], "-r", marker="o",
                    label=memory_data_dict['y1_axis']['label'])

    axis_padding = 0.3  # percentage
    host.set_xlim(min(cpu_load_data_dict['x_axis']['values']),
                  max(cpu_load_data_dict['x_axis']['values']))
    host.set_ylim(0,
                  max(cpu_load_data_dict['y1_axis']['values']) +
                  (max(cpu_load_data_dict['y1_axis']['values'])*axis_padding))
    par1.set_ylim(0,
                  max(memory_data_dict['y1_axis']['values']) +
                  (max(memory_data_dict['y1_axis']['values']) * axis_padding))

    host.set_xlabel(cpu_load_data_dict['x_axis']['label'])
    host.set_ylabel(cpu_load_data_dict['y1_axis']['label'])
    par1.set_ylabel(memory_data_dict['y1_axis']['label'])


    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())

    tkw = dict(size=4, width=1.5)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)

    lines = [p1, p2]

    # Title of the graph
    plt.title(title)
    plt.legend(lines, [l.get_label() for l in lines])
    plt.savefig(title + '.png', format="png")


    plt.show()


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


def read_cpu_results(filename):
    # Common dict structure
    data_dict = {'x_axis': {'label': '', 'values': []},
                 'y1_axis': {'label': '', 'values': []}}

    # Filename definition
    df = pd.read_csv(filename, sep=',', header=0)

    # Headers definition
    header_names = {'x_axis': 'Time (sec)',
                    'y1_axis': 'CPU Load (%)'}

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


def read_memory_results(filename):
    data_dict = {'x_axis': {'label': '', 'values': []},
                 'y1_axis': {'label': '', 'values': []}}

    df = pd.read_csv(filename, sep=',', header=0)
    header_names = {'x_axis': 'Time (sec)',
                    'y1_axis': 'Memory (%)'}

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


iperf3_monitoring_logger.info('Making Iperf3 graphs!')
# Making graph with UDP server results
make_graph(filename="graphs/cpu_and_memory_results/cpu_memory_output.csv",
           title="Empower Controller withouth APs")
iperf3_monitoring_logger.info('Done!')