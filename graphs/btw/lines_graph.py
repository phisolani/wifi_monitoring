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
                    y_axis_ticks=None,
                    log_type='log',
                    stacked=None,
                    annotation_info=None):

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

    plt.rcParams['mathtext.fontset'] = 'stix'

    # Adjust x Axis
    plt.tight_layout()

    if y_log_scale is not None:
        host.set_yscale(log_type)

    colors = ['darkblue', 'darkviolet', 'mediumblue', 'deeppink', 'dodgerblue', 'magenta', 'darkolivegreen', 'darkblue', 'deepskyblue', 'magenta', 'goldenrod']
    # colors += ['darkolivegreen', 'darkblue', 'deepskyblue', 'magenta', 'goldenrod']
    # colors = ['g', 'b', 'c', 'm', 'y']
    line_styles = ['-', '--', ':', '-.', '-', '--', ':', '-.']
    markers = ['o', '^', '+', 'x', '*', 'D', 'o', '^', '+', 'x', '*', 'D']

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
            smask = np.isfinite(data_dict['y' + str(y) + '_axis']['values'])
            xs = np.asarray(data_dict['x_axis']['values'])
            ys = np.asarray(data_dict['y' + str(y) + '_axis']['values'])
            p, = host.plot(xs[smask], ys[smask],
            # p, = host.plot(data_dict['x_axis']['values'], data_dict['y' + str(y) + '_axis']['values'],
                           color=colors[y],
                           marker=markers[y],
                           mfc='none',
                           markersize=8,
                           markeredgewidth=2,
                           markevery=1,
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

    if y_axis_ticks:
        host.set_yticks(y_axis_ticks['ticks'])
        host.set_yticklabels(y_axis_ticks['labels'])

    plt.legend(y_axes, loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=len(y_axes))  # shadow=True)

    # xcoords = [60, 120, 70, 100, 130, 160, 190]
    # for xc in xcoords:
    #     plt.axvline(x=xc, linestyle=':', color='dimgray', linewidth=2)

    if annotation_info:
        for annotation in annotation_info:
            if annotation['line'] == 'vertical':
                plt.axvline(x=annotation['x_coord'], linestyle=':', color='r', linewidth=2)
            elif annotation['line'] == 'horizontal':
                plt.axhline(y=annotation['y_coord'], linestyle=':', color='r', linewidth=2)

            host.annotate(annotation['label'],
                          xy=(annotation['x_coord'], annotation['y_coord']),
                          xytext=(annotation['x_coord_label'], annotation['y_coord_label']),
                          arrowprops=dict(facecolor='black', shrink=0.05),
                          horizontalalignment='right', verticalalignment='top')

    if title is not None:
        plt.title(title)

    plt.savefig(str(experiment_path) + 'plots/' + str(filename) + '.pdf', format="pdf", bbox_inches="tight")
    plt.savefig(str(experiment_path) + 'plots/' + str(filename) + '.png', format="png", bbox_inches="tight")
    plt.savefig(str(experiment_path) + 'plots/' + str(filename) + '.eps', format="eps", bbox_inches="tight")

    plt.show()
    print('Done!')


def make_share_x_graph(experiment_path=None,
                       filenames=None,
                       output_name=None,
                       plot_info=None,
                       fig_size=None,
                       y_axis_colors=None,
                       y_axis_line_styles=None,
                       y_axis_markers=None):
    # Applying Seaborn style
    # whitegrid, darkgrid, whitegrid, dark, white, and ticks
    sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)
    plt.rcParams['mathtext.fontset'] = 'stix'

    x_axis = plot_info['x_axis']
    x_axis_label = plot_info['x_axis_label']
    x_axis_min_max = plot_info['x_axis_min_max']
    fig_title = plot_info['fig_title']

    # figure out how many subplots
    num_subplots = len(plot_info['subplots'])

    if fig_size is not None:
        fig = plt.figure(figsize=(fig_size[0], fig_size[1]), dpi=144)
    else:
        fig = plt.figure(figsize=(12, 6), dpi=144)

    for i in range(num_subplots):
        y_axes = plot_info['subplots'][i]['y_axes']
        y_axes_labels = plot_info['subplots'][i]['y_axes_labels']
        y_axis_min_max = plot_info['subplots'][i]['y_axis_min_max']
        y_axis_label = plot_info['subplots'][i]['y_axis_label']
        y_log_scale = plot_info['subplots'][i]['y_log_scale']
        if 'y_axis_ticks' in plot_info['subplots'][i]:
            y_axis_ticks = plot_info['subplots'][i]['y_axis_ticks']
        else:
            y_axis_ticks = None
        # read in the data
        csv_file = experiment_path + filenames[i] + '.csv'
        data_dict = read_results(filename=csv_file, x_axis=x_axis, y_axes=y_axes)

        print(data_dict)

        plt.tight_layout()

        ax = fig.add_subplot(num_subplots, 1, i+1)
        if i == 0:
            ax.set_title(fig_title)

        if y_log_scale:
            ax.set_yscale('log')

        lines = []

        for y in range(len(y_axes)):
            smask = np.isfinite(data_dict['y' + str(y) + '_axis']['values'])
            xs = np.asarray(data_dict['x_axis']['values'])
            ys = np.asarray(data_dict['y' + str(y) + '_axis']['values'])
            p, = ax.plot(xs[smask], ys[smask],
                         marker=y_axis_markers[y],
                         mfc='none',
                         markersize=8,
                         markeredgewidth=2,
                         color=y_axis_colors[y],
                         linestyle=y_axis_line_styles[y],
                         linewidth=2,
                         label=str(y_axes[y]))
            lines.append(p)

        ax.set_xlim(x_axis_min_max['min'], x_axis_min_max['max'])

        if i == num_subplots - 1:
            ax.set_xlabel(x_axis_label)
            plt.setp(ax.get_xticklabels(), visible=True)
        else:
            plt.setp(ax.get_xticklabels(), visible=False)

        if y_axis_ticks:
            ax.set_yticks(y_axis_ticks['ticks'])
            ax.set_yticklabels(y_axis_ticks['labels'])

        ax.set_ylim(y_axis_min_max['min'], y_axis_min_max['max'])
        ax.set_ylabel(y_axis_label)
        # labels = [l.get_label() for l in lines]
        labels = y_axes_labels
        if len(lines) > 2:
            n_cols = int(len(lines))
        else:
            n_cols = len(lines)

        if i == 0:
            plt.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=n_cols)

    plt.xlim(x_axis_min_max['min'], x_axis_min_max['max'])

    plt.savefig(str(experiment_path) + str(output_name) + '.pdf', format="pdf", bbox_inches="tight")
    plt.savefig(str(experiment_path) + str(output_name) + '.png', format="png", bbox_inches="tight")
    plt.savefig(str(experiment_path) + str(output_name) + '.eps', format="eps", bbox_inches="tight")

    plt.show()


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

