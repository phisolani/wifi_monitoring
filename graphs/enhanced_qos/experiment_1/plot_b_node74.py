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

fig_size = [7, 4]

# Scenario B (DL v UL)
path = 'scenario_b_node74/'
filename = 'b_results'
x_axis_min_max = {'min': 0, 'max': 300}

#Throughput
output_name = 'scenario_b_74_throughput'
make_line_graph(
    experiment_path=path,
    filename=filename,
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max= x_axis_min_max,
    y_axes=['Throughput BE', 'Throughput QoS', 'Shaper BE'],
    y_axis_label='Throughput (Mbps)',
    y_axis_min_max={'min': 0, 'max': 300},
    y_log_scale=True,
    markers=["", "", "D", "1"],
    fig_size=fig_size,
    output_name=output_name
)

# Delay of AP
output_name = 'scenario_b_74_ap_delay'
make_line_graph(
    experiment_path=path,
    filename=filename,
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max=x_axis_min_max,
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
    filename=filename,
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max=x_axis_min_max,
    left_y_axes=['Shaper BE'],
    left_y_axis_min_max={'min': 0, 'max': 300},
    left_y_axis_label='Throughput (Mbps)',
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
    filename=filename,
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max=x_axis_min_max,
    left_y_axes=['Shaper BE'],
    left_y_axis_min_max={'min': 0, 'max': 300},
    left_y_axis_label='Throughput (Mbps)',
    left_y_log_scale=True,
    right_y_axes=['Loss BE'],
    right_y_axis_min_max={'min': 0, 'max': 60},
    right_y_axis_label='Loss (packets/sec)',
    fig_size=fig_size,
    output_name=output_name
)

