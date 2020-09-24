#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2020, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

" Python script for making graphs with CSV output"

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


def make_line_graph(experiment_path, filename, x_axis, y_axes,
                    title=None,
                    fig_size=None,
                    x_axis_label=None,
                    x_axis_ticks=True,
                    x_axis_min_max=None,
                    y_axis_label=None,
                    y_axis_min_max=None,
                    y_log_scale=None,
                    stacked=None):

    # Applying Seaborn style
    # whitegrid, darkgrid, whitegrid, dark, white, and ticks
    sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)

    # Reading CSV results
    csv_file = experiment_path + filename + '.csv'
    data_dict = read_results(filename=csv_file, x_axis=x_axis, y_axes=y_axes)

    # Plotting just the first values of the experiment (16, 8)
    if fig_size is not None:
        fig, host = plt.subplots(figsize=(fig_size[0], fig_size[1]), dpi=144)
    else:
        fig, host = plt.subplots(figsize=(12, 6), dpi=144)

    # Adjust x Axis
    plt.tight_layout()

    if y_log_scale is not None:
        host.set_yscale('log')

    #colors = ['darkblue', 'darkviolet', 'mediumblue', 'deeppink', 'dodgerblue', 'magenta']
    # colors = ['darkolivegreen', 'darkblue', 'deepskyblue', 'magenta', 'goldenrod']
    colors = ['g', 'b', 'c', 'm', 'y']
    line_styles = ['-', '--', ':', '-.', '-', '--', ':', '-.']
    markers = ['o', '^', '+', 'x', '*', 'D']

    if stacked:
        y_values = []
        for axis in data_dict:
            if 'x_axis' not in axis:
                y_values.append(data_dict[axis]['values'])

        # original
        # pal = ["#9b59b6", "#e74c3c", "#34495e", "#2ecc71"]
        # pal = ["darkolivegreen", "darkblue", "darkmagenta", "goldenrod"]
        pal = ["g", "b", "m", "y"]

        stacks = host.stackplot(data_dict['x_axis']['values'], y_values, labels=y_axes, colors=pal)
                                # colors=pal, alpha=0.6)
        hatches = ['+', 'x', '.', '*', '\\', 'O', 'o', '-']
        for stack, hatch in zip(stacks, hatches):
            stack.set_hatch(hatch)

        # plt.stackplot(data_dict['x_axis']['values'], y_values, labels=y_axes, colors=pal, alpha=0.4)
        plt.legend(loc='upper left')
    else:
        lines = []
        for y in range(len(y_axes)):
            p, = host.plot(data_dict['x_axis']['values'], data_dict['y' + str(y) + '_axis']['values'],
                           color=colors[y],
                           # marker=markers[y],
                           # mfc='none',
                           # markersize=6,
                           # markevery=2,
                           linestyle=line_styles[y],
                           linewidth=2,
                           label=str(y_axes[y]))
            lines.append(p)

    if x_axis_min_max is None:
        host.set_xlim(0,
                      len(data_dict['x_axis']['values']))
    else:
        host.set_xlim(x_axis_min_max['min'],
                      x_axis_min_max['max'])

    if y_axis_min_max is None:
        host.set_ylim(0)
    else:
        host.set_ylim(y_axis_min_max['min'],
                      y_axis_min_max['max'])

    plt.xticks(np.arange(0, 330, step=50))

    if not x_axis_ticks:
        plt.setp(host.get_xticklabels(), visible=False)

    if x_axis_label is not None:
        host.set_xlabel(x_axis_label)

    if y_axis_label is not None:
        host.set_ylabel(y_axis_label)

    plt.legend(y_axes, loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=len(y_axes))  # shadow=True)

    xcoords = [10, 40, 70, 100, 130, 160, 190]
    for xc in xcoords:
        plt.axvline(x=xc, linestyle='--', color='dimgray')

    if title is not None:
        plt.title(title)

    plt.savefig(str(experiment_path) + str(filename) + '.pdf', format="pdf", bbox_inches="tight")
    plt.savefig(str(experiment_path) + str(filename) + '.png', format="png", bbox_inches="tight")
    plt.savefig(str(experiment_path) + str(filename) + '.eps', format="eps", bbox_inches="tight")

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

