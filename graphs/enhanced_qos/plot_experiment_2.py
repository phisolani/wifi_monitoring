#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2020, Enhanced QoS"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

" Python script for making all graphs at once"

from graphs.enhanced_qos.lines_graph import *

fig_size = [10, 3.4]

# LVAP Shaper (Scenario A)
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/enhanced_qos/experiment_2/scenario_a/",
    filename="lvap_shaper",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['STA 1', 'STA 2'],
    y_axis_label='Throughput (Mbps)',
    y_axis_min_max={'min': 0, 'max': 1000},
    y_log_scale=True,
    fig_size=fig_size)

# LVAP Throughput (Scenario A)
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/enhanced_qos/experiment_2/scenario_a/",
    filename="lvap_throughput",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['STA 1', 'STA 2'],
    y_axis_label='Throughput (Mbps)',
    y_axis_min_max={'min': 0, 'max': 25},
    fig_size=fig_size)



