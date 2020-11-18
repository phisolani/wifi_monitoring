#!/usr/bin/env python
__author__ = "Daniel Kulenkamp"
__copyright__ = "Copyright 2020, QoS-aware WiFi Slicing"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Kulenkamp"
__email__ = "dkulenka@asu.edu"
__status__ = "Prototype"

" Python script for making all graphs at once for sensors experiment 1"

from graphs.enhanced_qos.lines_graph import *

fig_size = [10, 3.4]

# Scenario B (DL v UL)
path = 'scenario_d/'

#Throughput
output_name = 'scenario_d_throughput'
make_line_graph(
    experiment_path=path,
    filename='throughput',
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max={'min': 0, 'max': 300},
    y_axes=['BE Throughput', 'QoS Throughput'],
    y_axis_label='Throughput (Mbps)',
    y_axis_min_max={'min': 0, 'max': 25},
    fig_size=fig_size,
    output_name=output_name
)

# Quantum
output_name = 'scenario_d_quantum'
make_line_graph(
    experiment_path=path,
    filename='throughput',
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max={'min': 0, 'max': 300},
    y_axes=['BE Quantum', 'QoS Quantum'],
    y_axis_label='Current Quantum (μsec)',
    y_axis_min_max={'min': 0, 'max': 13000},
    y_log_scale=True,
    fig_size=fig_size,
    output_name=output_name
)

output_name = 'scenario_d_delay'
make_line_graph(
    experiment_path=path,
    filename='throughput',
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max={'min': 0, 'max': 300},
    y_axes=['Delay BE', 'Delay QoS'],
    y_axis_label='Delay (msec)',
    y_axis_min_max={'min': 0, 'max': 40000},
    y_log_scale=True,
    fig_size=fig_size,
    output_name=output_name
)