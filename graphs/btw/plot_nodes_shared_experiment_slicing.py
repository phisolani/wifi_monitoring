#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2020, QoS-aware WiFi Slicing"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

" Python script for making all graphs at once"

from graphs.btw.lines_graph import *
from graphs.btw.experiment_style import node


# Experiment slicing 1st hop
path = 'experiment_slicing/'
filenames = ['node_mcs', 'node_rssi', 'node_retransmission_flag', 'node_processing_delay']
x_axis_min_max = {'min': 0, 'max': 300}
output_name = 'plots/nodes_sharex_1st_hop_graph'
fig_size = [6, 6]
events = [132, 177, 271]

y_axes = ['AP 3 (APP 1)', 'AP 3 (APP 2)']
y_axes_labels = ['APP 1', 'APP 2']
plot_info = {
    'x_axis': 'Time',
    'x_axis_label': 'Time (sec)',
    'x_axis_min_max': x_axis_min_max,
    'fig_title': '1st hop',
    'font_scale': 1,
    'markersize': 8,
    'markeredgewidth': 1,
    'linewidth': 1,
    'subplots': [
        {
            'y_axes': y_axes,
            'y_axes_labels': y_axes_labels,
            'y_axis_min_max': {'min': 0, 'max': 12},
            'y_axis_label': 'MCS',
            'y_log_scale': False,
        },
        {
            'y_axes': y_axes,
            'y_axes_labels': y_axes_labels,
            'y_axis_min_max': {'min': -80, 'max': -20},
            'y_axis_label': 'RSSI (dBm)',
            'y_log_scale': False,
        },
        {
            'y_axes': y_axes,
            'y_axes_labels': y_axes_labels,
            'y_axis_min_max': {'min': -0.2, 'max': 1.2},
            'y_axis_ticks': {'ticks': [0, 1], 'labels': ['False', 'True']},
            'y_axis_label': 'Retransmission flag',
            'y_log_scale': False,
        },
        {
            'y_axes': y_axes,
            'y_axes_labels': y_axes_labels,
            'y_axis_min_max': {'min': 0, 'max': 10},
            'y_axis_label': 'Processing delay (ms)',
            'y_log_scale': True
        }
    ]
}

make_share_x_graph(
    experiment_path=path,
    filenames=filenames,
    fig_size=fig_size,
    output_name=output_name,
    plot_info=plot_info,
    y_axis_colors=node['colors'],
    y_axis_line_styles=node['line_styles'],
    y_axis_markers=node['markers'],
    events=events,
)

# Experiment slicing 2nd hop
path = 'experiment_slicing/'
filenames = ['node_mcs', 'node_rssi', 'node_retransmission_flag', 'node_processing_delay']
x_axis_min_max = {'min': 0, 'max': 300}
output_name = 'plots/nodes_sharex_2nd_hop_graph'
fig_size = [6, 6]

y_axes = ['STA 7 (APP 1)', 'STA 8 (APP 2)']
y_axes_labels = ['APP 1', 'APP 2']
plot_info = {
    'x_axis': 'Time',
    'x_axis_label': 'Time (sec)',
    'x_axis_min_max': x_axis_min_max,
    'fig_title': '2nd hop',
    'font_scale': 1,
    'markersize': 8,
    'markeredgewidth': 1,
    'linewidth': 1,
    'subplots': [
        {
            'y_axes': y_axes,
            'y_axes_labels': y_axes_labels,
            'y_axis_min_max': {'min': 0, 'max': 12},
            'y_axis_label': 'MCS',
            'y_log_scale': False,
        },
        {
            'y_axes': y_axes,
            'y_axes_labels': y_axes_labels,
            'y_axis_min_max': {'min': -80, 'max': -20},
            'y_axis_label': 'RSSI (dBm)',
            'y_log_scale': False,
        },
        {
            'y_axes': y_axes,
            'y_axes_labels': y_axes_labels,
            'y_axis_min_max': {'min': -0.2, 'max': 1.2},
            'y_axis_ticks': {'ticks': [0, 1], 'labels': ['False', 'True']},
            'y_axis_label': 'Retransmission flag',
            'y_log_scale': False,
        },
        {
            'y_axes': y_axes,
            'y_axes_labels': y_axes_labels,
            'y_axis_min_max': {'min': 0, 'max': 10},
            'y_axis_label': 'Processing delay (ms)',
            'y_log_scale': True
        }
    ]
}

make_share_x_graph(
    experiment_path=path,
    filenames=filenames,
    fig_size=fig_size,
    output_name=output_name,
    plot_info=plot_info,
    y_axis_colors=node['colors'],
    y_axis_line_styles=node['line_styles'],
    y_axis_markers=node['markers'],
    events=events
)