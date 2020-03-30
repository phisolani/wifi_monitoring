#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2018, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

" Python script for making graphs with CSV output"

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def make_graph(experiment_path, filename):

    # Applying Seaborn style
    # whitegrid, darkgrid, whitegrid, dark, white, and ticks
    sns.set(style="whitegrid", font_scale=2, font='Times New Roman')

    # Reading ICMP CSV results
    icmp_data_dict = read_icmp_results(experiment_path=experiment_path,
                                       filename=filename)

    #print(icmp_data_dict)
    fig, host = plt.subplots(figsize=(12, 6), dpi=144)

    #ax1 = plt.subplot(311)
    #plt.setp(host.get_xticklabels())

    # Adjust x Axis
    plt.tight_layout()

    p1, = host.plot(icmp_data_dict['x_axis']['values'], icmp_data_dict['y_axis']['values'], 'b-', marker="d",
                    markevery=1, markersize=10, mfc='none', markeredgewidth=2,
                    label="BE Slice")
    p2, = host.plot(icmp_data_dict['x_axis']['values'], icmp_data_dict['y1_axis']['values'], "-y", marker="x",
                    markevery=1, markersize=10, mfc='none', markeredgewidth=2,  #linewidth=3.5,
                    label="QoS Slice")
    #p3, = host.plot(icmp_data_dict['x_axis']['values'], icmp_data_dict['y2_axis']['values'], "-g", marker="o",
    #                markevery=1, markersize=10, mfc='none', markeredgewidth=2,  #linewidth=2.0,
    #                label="Adaptive Slices")

    axis_padding = 0.3  # percentage
    host.set_xlim(min(icmp_data_dict['x_axis']['values']),
                  max(icmp_data_dict['x_axis']['values']))
    host.set_ylim(0,
                  max(icmp_data_dict['y_axis']['values']+icmp_data_dict['y1_axis']['values']) +
                  (max(icmp_data_dict['y_axis']['values']+icmp_data_dict['y1_axis']['values'])*axis_padding))

    host.set_xlabel("Time (sec)")
    host.set_ylabel("Quantum (us)")

    lines = [p1, p2]

    #plt.title("TESTE")
    plt.legend(lines, [l.get_label() for l in lines], loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=3) #shadow=True)
    plt.savefig(experiment_path + 'quantum_results.pdf', format="pdf", bbox_inches = "tight")

    plt.show()
    print('Done!')


def read_icmp_results(experiment_path, filename):
    data_dict = {'x_axis': {'label': '', 'values': []},
                 'y_axis': {'label': '', 'values': []},
                 'y1_axis': {'label': '', 'values': []}}

    df = pd.read_csv(experiment_path + filename, sep=',', header=0)
    header_names = {'x_axis': 'Time (sec)',
                    'y_axis': 'BE Slice Quantum (us)',
                    'y1_axis': 'QoS Slice Quantum (us)'}

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


make_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/sdn_based_slicing/quantum_results/",
           filename="quantum_plot.csv")

