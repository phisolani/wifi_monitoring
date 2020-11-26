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


def make_two_axis_line_graph(experiment_path, filename, x_axis, left_y_axes, right_y_axes, output_name,
                             title=None,
                             fig_size=None,
                             x_axis_label=None,
                             x_axis_ticks=True,
                             x_axis_min_max=None,
                             left_y_axis_label=None,
                             left_y_axis_min_max=None,
                             left_y_log_scale=None,
                             right_y_axis_label=None,
                             right_y_axis_min_max=None,
                             right_y_log_scale=None):
    # Applying Seaborn style
    # whitegrid, darkgrid, whitegrid, dark, white, and ticks
    sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)

    # Reading CSV results
    csv_file = experiment_path + filename + '.csv'
    left_data_dict = read_results(filename=csv_file, x_axis=x_axis, y_axes=left_y_axes)
    right_data_dict = read_results(filename=csv_file, x_axis=x_axis, y_axes=right_y_axes)

    # Plotting just the first values of the experiment (16, 8)
    if fig_size is not None:
        fig, ax1 = plt.subplots(figsize=(fig_size[0], fig_size[1]), dpi=144)
    else:
        fig, ax1 = plt.subplots(figsize=(12, 6), dpi=144)

    ax2 = ax1.twinx()

    # Adjust x Axis
    plt.tight_layout()
    if left_y_log_scale is not None:
        ax1.set_yscale('log')

    if right_y_log_scale is not None:
        ax2.set_yscale('log')

    # colors = ['darkblue', 'darkviolet', 'mediumblue', 'deeppink', 'dodgerblue', 'magenta']
    # colors = ['darkolivegreen', 'darkblue', 'deepskyblue', 'magenta', 'goldenrod']
    colors_l = ['g', 'b', 'c']#, 'm', 'y', 'r']
    colors_r = ['m', 'r', 'y']
    line_styles = ['-', '--', ':', '-.', '-', '--', ':', '-.']

    lines = []

    for y_left in range(len(left_y_axes)):
        p, = ax1.plot(left_data_dict['x_axis']['values'], left_data_dict['y' + str(y_left) + '_axis']['values'],
                           color=colors_l[y_left],
                           linestyle=line_styles[y_left],
                           linewidth=2,
                           label=str(left_y_axes[y_left]))
        lines.append(p)

    for y_right in range(len(right_y_axes)):
        p, = ax2.plot(right_data_dict['x_axis']['values'], right_data_dict['y' + str(y_right) + '_axis']['values'],
                           color=colors_r[y_right],
                           linestyle=line_styles[y_right],
                           linewidth=2,
                           label=str(right_y_axes[y_right]))
        lines.append(p)

    if x_axis_min_max is None:
        ax1.set_xlim(0,
                      len(left_data_dict['x_axis']['values']))
    else:
        ax1.set_xlim(x_axis_min_max['min'],
                      x_axis_min_max['max'])

    if left_y_axis_min_max is None:
        ax1.set_ylim(0)
    else:
        ax1.set_ylim(left_y_axis_min_max['min'],
                      left_y_axis_min_max['max'])

    if right_y_axis_min_max is None:
        ax2.set_ylim(0)
    else:
        ax2.set_ylim(right_y_axis_min_max['min'],
                     right_y_axis_min_max['max'])

    x_range = left_data_dict['x_axis']['values'][-1]
    plt.xticks(np.arange(0, x_range, step=50))

    if not x_axis_ticks:
        plt.setp(ax1.get_xticklabels(), visible=False)

    if x_axis_label is not None:
        ax1.set_xlabel(x_axis_label)

    if left_y_axis_label is not None:
        ax1.set_ylabel(left_y_axis_label)

    if right_y_axis_label is not None:
        ax2.set_ylabel(right_y_axis_label)

    labels = [l.get_label() for l in lines]
    if len(lines) > 2:
        n_cols = int(len(lines)) // 2
    else:
        n_cols = len(lines)
    plt.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=n_cols)  # shadow=True)

    # xcoords = [10, 40, 70, 100, 130, 160, 190]
    # for xc in xcoords:
    #     plt.axvline(x=xc, linestyle='--', color='dimgray')

    if title is not None:
        plt.title(title)

    plt.savefig(str(experiment_path) + str(output_name) + '.pdf', format="pdf", bbox_inches="tight")
    plt.savefig(str(experiment_path) + str(output_name) + '.png', format="png", bbox_inches="tight")
    plt.savefig(str(experiment_path) + str(output_name) + '.eps', format="eps", bbox_inches="tight")

    plt.show()
    print('Done!')


def make_line_graph(experiment_path, filename, x_axis, y_axes, output_name,
                    title=None,
                    fig_size=None,
                    x_axis_label=None,
                    x_axis_ticks=True,
                    x_axis_min_max=None,
                    y_axis_label=None,
                    y_axis_min_max=None,
                    y_log_scale=None,
                    markers=None,
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
    colors = ['g', 'b', 'c', 'm', 'y', 'r']
    line_styles = ['-', '--', ':', '-.', '-', '--', ':', '-.']
    # markers = custom_markers if custom_markers else ['D', 'o', '^', '+', 'x', '*', 'D']

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
            if markers:
                p, = host.plot(data_dict['x_axis']['values'], data_dict['y' + str(y) + '_axis']['values'],
                           color=colors[y],
                           marker=markers[y],
                           mfc='none',
                           markersize=6,
                           markevery=10,
                           linestyle=line_styles[y],
                           linewidth=2,
                           label=str(y_axes[y]))
                lines.append(p)
            else:
                p, = host.plot(data_dict['x_axis']['values'], data_dict['y' + str(y) + '_axis']['values'],
                           color=colors[y],
                           linestyle=line_styles[y],
                           linewidth=2,
                           label=str(y_axes[y]))
                lines.append(p)

    x_range = data_dict['x_axis']['values'][-1]
    plt.xticks(np.arange(0, x_range, step=50))

    if not x_axis_ticks:
        plt.setp(host.get_xticklabels(), visible=False)

    if x_axis_min_max is None:
        print('default')
        host.set_xlim(0,
                      len(data_dict['x_axis']['values']))
    else:
        print('custom')
        host.set_xlim(x_axis_min_max['min'],
                      x_axis_min_max['max'])

    if y_axis_min_max is None:
        host.set_ylim(0)
    else:
        host.set_ylim(y_axis_min_max['min'],
                      y_axis_min_max['max'])

    if x_axis_label is not None:
        host.set_xlabel(x_axis_label)

    if y_axis_label is not None:
        host.set_ylabel(y_axis_label)

    if len(lines) > 2:
        n_cols = len(lines) // 2
    else:
        n_cols = len(lines)
    plt.legend(y_axes, loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=n_cols)  # shadow=True)

    # xcoords = [10, 40, 70, 100, 130, 160, 190]
    # for xc in xcoords:
    #     plt.axvline(x=xc, linestyle='--', color='dimgray')

    if title is not None:
        plt.title(title)

    plt.savefig(str(experiment_path) + str(output_name) + '.pdf', format="pdf", bbox_inches="tight")
    plt.savefig(str(experiment_path) + str(output_name) + '.png', format="png", bbox_inches="tight")
    plt.savefig(str(experiment_path) + str(output_name) + '.eps', format="eps", bbox_inches="tight")

    plt.show()
    print('Done!')


def read_results(filename, x_axis, y_axes):
    # Common dict structure
    data_dict = {'x_axis': {'label': '', 'values': []}}

    for y in range(0, len(y_axes)):
        data_dict['y' + str(y) + '_axis'] = {'label': '', 'values': []}

    # Filename definition
    df = pd.read_csv(filename, sep=',', header=0)

    # Headers definition
    header_names = {'x_axis': x_axis}

    for y in range(0, len(y_axes)):
        header_names['y' + str(y) + '_axis'] = y_axes[y]

    print(header_names)

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

