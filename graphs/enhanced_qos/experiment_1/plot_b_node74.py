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
path = 'scenario_b_node74/'

#Throughput
output_name = 'scenario_b_74_throughput'
make_line_graph(
    experiment_path=path,
    filename='throughput',
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max={'min': 0, 'max': 300},
    y_axes=['BE Throughput', 'QoS Throughput', 'Shaper BE'],
    y_axis_label='Throughput (Mbps)',
    y_axis_min_max={'min': 0, 'max': 110},
    y_log_scale=True,
    markers=["", "", "D", "1"],
    fig_size=fig_size,
    output_name=output_name
)

# Delay of AP
output_name = 'scenario_b_74_ap_delay'
make_line_graph(
    experiment_path=path,
    filename='throughput',
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max={'min': 0, 'max': 300},
    y_axes=['Delay QoS'],
    y_axis_label='Delay (msec)',
    y_axis_min_max={'min': 0, 'max': 1000},
    y_log_scale=True,
    fig_size=fig_size,
    output_name=output_name
)

# Delay with shaper
output_name = 'scenario_b_74_delay_with_shaper'
make_two_axis_line_graph(
    experiment_path=path,
    filename='throughput',
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max={'min': 0, 'max': 300},
    left_y_axes=['Shaper BE'],
    left_y_axis_min_max={'min': 0, 'max': 110},
    left_y_axis_label='Shaper Value (Mbps)',
    left_y_log_scale=True,
    right_y_axes=['Delay BE'],
    right_y_axis_min_max={'min': 0, 'max': 60},
    right_y_axis_label='Delay (msec)',
    fig_size=fig_size,
    output_name=output_name
)

# Loss with Shaper
output_name = 'scenario_b_74_loss_with_shaper'
make_two_axis_line_graph(
    experiment_path=path,
    filename='throughput',
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max={'min': 0, 'max': 300},
    left_y_axes=['Shaper BE'],
    left_y_axis_min_max={'min': 0, 'max': 110},
    left_y_axis_label='Shaper Value (Mbps)',
    left_y_log_scale=True,
    right_y_axes=['Loss BE'],
    right_y_axis_min_max={'min': 0, 'max': 60},
    right_y_axis_label='Loss (packets/sec)',
    fig_size=fig_size,
    output_name=output_name
)

