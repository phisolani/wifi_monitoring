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
from graphs.btw.experiment_style import node, slice, e2e, quantum

fig_size_paper = [8, 4]
fig_size_wide = [22, 4]
events = [132, 177, 271]
requirements_latency = [10]
requirements_jitter = [5]

# Apps e2e latency
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_slicing/",
    filename="apps_e2e_latency",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['APP 1', 'APP 2'],
    y_axis_label='Latency (ms)',
    y_axis_min_max={'min': 0.1, 'max': 100000},
    y_log_scale=True,
    log_type='log',
    fig_size=fig_size_paper,
    colors=e2e['colors'],
    line_styles=e2e['line_styles'],
    markers=e2e['markers'],
    events=events,
    requirements=requirements_latency)

# Apps e2e jitter
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_slicing/",
    filename="apps_e2e_jitter",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['APP 1', 'APP 2'],
    y_axis_label='Jitter (ms)',
    y_axis_min_max={'min': 0.1, 'max': 100000},
    y_log_scale=True,
    log_type='symlog',
    fig_size=fig_size_paper,
    colors=e2e['colors'],
    line_styles=e2e['line_styles'],
    markers=e2e['markers'],
    events=events,
    requirements=requirements_jitter)

# Node MCS
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_slicing/",
    filename="node_mcs",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': 0, 'max': 12},
    y_axes=['AP 3 (APP 2)',
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
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_slicing/",
    filename="node_rssi",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': -70, 'max': -10},
    y_axes=['AP 3 (APP 2)',
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
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_slicing/",
    filename="node_retransmission_flag",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': 0, 'max': 1.2},
    y_axes=['AP 3 (APP 2)',
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
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_slicing/",
    filename="node_processing_delay",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': 0, 'max': 20},
    y_axes=['AP 3 (APP 2)',
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

# AP 3 slice throughput
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_slicing/",
    filename="slice_throughput",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': 0, 'max': 6},
    y_axes=['Slice (APP 1)',
            'Slice (APP 2)'],
    y_axis_label='Throughput (Mbps)',
    fig_size=fig_size_paper,
    colors=slice['colors'],
    line_styles=slice['line_styles'],
    events=events)

# AP 3 slice quantum
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_slicing/",
    filename="slice_quantum",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': 0, 'max': 150000},
    y_log_scale=True,
    log_type='log',
    y_axes=['Slice (APP 1)',
            'Slice (APP 2)'],
    y_axis_label='Quantum (us)',
    fig_size=fig_size_paper,
    colors=quantum['colors'],
    line_styles=quantum['line_styles'],
    events=events)