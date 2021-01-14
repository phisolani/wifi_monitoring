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
from graphs.btw.experiment_style import node, slice, e2e

fig_size_paper = [8, 4]
fig_size_wide = [22, 4]
events = [85, 170, 250]

# Apps e2e latency
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_mcs/",
    filename="apps_e2e_latency",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['APP 1', 'APP 2', 'APP 3', 'APP 4'],
    y_axis_label='Latency (ms)',
    y_axis_min_max={'min': 0.1, 'max': 100000},
    y_log_scale=True,
    log_type='symlog',
    fig_size=fig_size_paper,
    colors=e2e['colors'],
    line_styles=e2e['line_styles'],
    markers=e2e['markers'],
    events=events)

# Apps e2e jitter
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_mcs/",
    filename="apps_e2e_jitter",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['APP 1', 'APP 2', 'APP 3', 'APP 4'],
    y_axis_label='Jitter (ms)',
    y_axis_min_max={'min': 0.1, 'max': 100000},
    y_log_scale=True,
    log_type='symlog',
    fig_size=fig_size_paper,
    colors=e2e['colors'],
    line_styles=e2e['line_styles'],
    markers=e2e['markers'],
    events=events)

# Node MCS
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_mcs/",
    filename="node_mcs",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': 0, 'max': 12},
    y_axes=['AP 1 (APP 3)',
            'STA 2 (APP 3)',
            'STA 3 (APP 4)',
            'AP 2 (APP 4)',
            'AP 3 (APP 2)',
            'STA 8 (APP 2)',
            'STA 7 (APP 1)',
            'AP 3 (APP 1)'],
    y_axis_label='MCS',
    fig_size=fig_size_wide,
    colors=node['colors'],
    line_styles=node['line_styles'],
    markers=node['markers'],
    events=events)

# Node RSSI
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_mcs/",
    filename="node_rssi",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': -70, 'max': -10},
    y_axes=['AP 1 (APP 3)',
            'STA 2 (APP 3)',
            'STA 3 (APP 4)',
            'AP 2 (APP 4)',
            'AP 3 (APP 2)',
            'STA 8 (APP 2)',
            'STA 7 (APP 1)',
            'AP 3 (APP 1)'],
    y_axis_label='RSSI (dBm)',
    fig_size=fig_size_wide,
    colors=node['colors'],
    line_styles=node['line_styles'],
    markers=node['markers'],
    events=events)

# Node retransmission flag
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_mcs/",
    filename="node_retransmission_flag",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': 0, 'max': 1.2},
    y_axes=['AP 1 (APP 3)',
            'STA 2 (APP 3)',
            'STA 3 (APP 4)',
            'AP 2 (APP 4)',
            'AP 3 (APP 2)',
            'STA 8 (APP 2)',
            'STA 7 (APP 1)',
            'AP 3 (APP 1)'],
    y_axis_label='Retransmission flag (true/false)',
    y_axis_ticks={'ticks': [0, 1], 'labels': ['False', 'True']},
    fig_size=fig_size_wide,
    colors=node['colors'],
    line_styles=node['line_styles'],
    markers=node['markers'],
    events=events)

# Node processing delay
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_mcs/",
    filename="node_processing_delay",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': 0, 'max': 20},
    y_axes=['AP 1 (APP 3)',
            'STA 2 (APP 3)',
            'STA 3 (APP 4)',
            'AP 2 (APP 4)',
            'AP 3 (APP 2)',
            'STA 8 (APP 2)',
            'STA 7 (APP 1)',
            'AP 3 (APP 1)'],
    y_axis_label='Processing delay (ms)',
    y_log_scale=True,
    fig_size=fig_size_wide,
    colors=node['colors'],
    line_styles=node['line_styles'],
    markers=node['markers'],
    events=events)

# AP 1 slice throughput
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_mcs/",
    filename="ap_1_slice_throughput",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': 0, 'max': 0.01},
    y_axes=['Slice (APP 3)'],
    y_axis_label='Throughput (Mbps)',
    fig_size=fig_size_paper,
    colors=slice['colors'],
    line_styles=slice['line_styles'],
    events=events)

# AP 2 slice throughput
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_mcs/",
    filename="ap_2_slice_throughput",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': 0, 'max': 0.01},
    y_axes=['Slice (APP 4)'],
    y_axis_label='Throughput (Mbps)',
    fig_size=fig_size_paper,
    colors=slice['colors'],
    line_styles=slice['line_styles'],
    events=events)

# AP 3 slice throughput
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_mcs/",
    filename="ap_3_slice_throughput",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': 0, 'max': 8},
    y_axes=['Slice (APP 1)',
            'Slice (APP 2)'],
    y_axis_label='Throughput (Mbps)',
    fig_size=fig_size_paper,
    colors=slice['colors'],
    line_styles=slice['line_styles'],
    events=events)