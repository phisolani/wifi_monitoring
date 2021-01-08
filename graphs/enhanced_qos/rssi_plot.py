#!/usr/bin/env python
__author__ = 'Pedro Heleno Isolani'
__copyright__ = 'Copyright 2021, The SDN WiFi MAC Manager'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'Pedro Heleno Isolani'
__email__ = 'pedro.isolani@uantwerpen.be'
__status__ = 'Prototype'

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


def make_scatter_rssi_shared_y(experiment_path,
                               filenames,
                               x_axis,
                               y_axes,
                               title=None,
                               fig_size=None,
                               x_axis_label=None,
                               x_axis_min_max=None,
                               y_axis_label=None,
                               y_axis_min_max=None,
                               events=None,
                               annotation_info=None):

    # Applying Seaborn style
    # whitegrid, darkgrid, whitegrid, dark, white, and ticks
    sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)

    # Reading CSV results
    csv_files = []
    for filename in filenames:
        csv_files.append(experiment_path + filename + '.csv')

    data_dicts = []
    for csv_file in csv_files:
        data_dicts.append(read_results(filename=csv_file, x_axis=x_axis, y_axes=y_axes))

    # Plotting just the first values of the experiment (16, 8)
    if fig_size is not None:
        fig, axs = plt.subplots(1, len(data_dicts), figsize=(fig_size[0], fig_size[1]), sharey=True, dpi=144)
    else:
        fig, axs = plt.subplots(1, len(data_dicts), figsize=(12, 10), sharey=True, dpi=144)

    #colors = ['darkblue', 'darkviolet', 'mediumblue', 'deeppink', 'dodgerblue', 'magenta', 'darkolivegreen', 'darkblue',
              # 'deepskyblue', 'magenta', 'goldenrod']
    # colors = ['darkolivegreen', 'darkblue', 'deepskyblue', 'magenta', 'goldenrod']
    colors = ['g', 'b', 'c', 'm', 'y', 'r']
    markers = ['o', '^', '+', 'x', '*', 'd', 'o', '^', '+', 'x', '*', 'd']
    # markers = ['\infty', '\spadesuit', '\heartsuit', '\diamondsuit', '\clubsuit', '\\bigodot', '\\bigotimes', '\\bigoplus', '\imath', '\\bowtie','\\bigtriangleup', '\\bigtriangledown', '\oslash' '\ast', '\\times', '\circ', '\\bullet', '\star', '+', '\Theta', '\Xi', '\Phi','\$', '\#', '\%', '\S']

    for i in range(0, 3):
        for y in range(len(y_axes)):
            axs[i].scatter(data_dicts[i]['x_axis']['values'],
                           data_dicts[i]['y' + str(y) + '_axis']['values'],
                           marker=markers[y],
                           # edgecolor='k',
                           c=colors[y],
                           s=100,
                           alpha=0.5
                           # markevery=2
                           )

    plt.rcParams['mathtext.fontset'] = 'stix'

    # Adjust x Axis
    plt.tight_layout()

    ap = 1
    for ax in axs:
        ax.set_xlim(x_axis_min_max['min'],
                    x_axis_min_max['max'])
        ax.set_ylim(y_axis_min_max['min'],
                    y_axis_min_max['max'])
        ax.set_xticks(np.arange(0, x_axis_min_max['max']+1, step=100))
        ax.set_xlabel(x_axis_label)
        ax.set_title('AP ' + str(ap))
        ap += 1

    axs[0].set_ylabel(y_axis_label)

    if y_axis_label is not None:
        axs[0].set_ylabel(y_axis_label)

    fig.legend(y_axes, loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=len(y_axes))  # shadow=True)

    if events:
        xcoords = [10, 70, 130, 190]
        for xc in xcoords:
            for ax in axs:
                ax.axvline(x=xc, linestyle=':', color='r', linewidth=2)

    # if annotation_info:
    #     for annotation in annotation_info:
    #         if annotation['line'] == 'vertical':
    #             plt.axvline(x=annotation['x_coord'], linestyle=':', color='r', linewidth=2)
    #         elif annotation['line'] == 'horizontal':
    #             plt.axhline(y=annotation['y_coord'], linestyle=':', color='r', linewidth=2)
    #
    #         host.annotate(annotation['label'],
    #                       xy=(annotation['x_coord'], annotation['y_coord']),
    #                       xytext=(annotation['x_coord_label'], annotation['y_coord_label']),
    #                       arrowprops=dict(facecolor='black', shrink=0.05),
    #                       horizontalalignment='right', verticalalignment='top')

    if title is not None:
        plt.title(title)

    plt.savefig(str(experiment_path) + 'aps_rssi' + '.pdf', format="pdf", bbox_inches="tight")
    plt.savefig(str(experiment_path) + 'aps_rssi' + '.png', format="png", bbox_inches="tight")
    plt.savefig(str(experiment_path) + 'aps_rssi' + '.eps', format="eps", bbox_inches="tight")

    plt.show()
    print('Done!')


def read_results(filename, x_axis, y_axes):
    # Common dict structure
    data_dict = {'x_axis': {'label': '', 'values': []}}

    for y in range(0, len(y_axes)):
        data_dict['y' + str(y) + '_axis'] = {'label': '', 'values': []}

    # Filename definition
    df = pd.read_csv(filename, sep=';', header=0)

    # Headers definition
    header_names = {'x_axis': x_axis}

    for y in range(0, len(y_axes)):
        header_names['y' + str(y) + '_axis'] = y_axes[y]

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

