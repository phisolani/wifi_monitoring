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
x_max = 200

# Scenario A (UL v UL)
path = 'scenario_a/'

# Throughput
output_name = 'scenario_a_throughput'
make_line_graph(
    experiment_path=path,
    filename='sta_throughput',
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max={'min': 0, 'max': x_max},
    y_axes=['BE Throughput', 'QoS Throughput', 'Shaper BE', 'Shaper QoS'],
    y_axis_label='Throughput (Mbps)',
    y_axis_min_max={'min': 0, 'max': 1010},
    y_log_scale=True,
    markers=["", "", "D", "1"],
    fig_size=fig_size,
    output_name=output_name
)

# Delay with shaper
output_name = 'scenario_a_delay_with_shaper'
make_two_axis_line_graph(
    experiment_path=path,
    filename='sta_throughput',
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max={'min': 0, 'max': x_max},
    left_y_axes=['Shaper BE', 'Shaper QoS'],
    left_y_axis_min_max={'min': 0, 'max': 1010},
    left_y_axis_label='Shaper Value (Mbps)',
    left_y_log_scale=True,
    right_y_axes=['Delay BE', 'Delay QoS'],
    right_y_axis_min_max={'min': 0, 'max': 100},
    right_y_axis_label='Queueing delay (ms)',
    right_y_log_scale=True,
    fig_size=fig_size,
    output_name=output_name
)

# Loss with Shaper
output_name = 'scenario_a_loss_with_shaper'
make_two_axis_line_graph(
    experiment_path=path,
    filename='sta_throughput',
    x_axis='Time',
    x_axis_label='Time (sec)',
    x_axis_min_max={'min': 0, 'max': x_max},
    left_y_axes=['Shaper BE', 'Shaper QoS'],
    left_y_axis_min_max={'min': 0, 'max': 1010},
    left_y_axis_label='Throughput (Mbps)',
    left_y_log_scale=True,
    right_y_axes=['Loss BE', 'Loss QoS'],
    right_y_axis_min_max={'min': None, 'max': 60},
    right_y_axis_label='Loss (frames/sec)',
    fig_size=fig_size,
    output_name=output_name
)

