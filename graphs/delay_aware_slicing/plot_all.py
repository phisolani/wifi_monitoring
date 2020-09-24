#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2020, QoS-aware WiFi Slicing"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

" Python script for making all graphs at once"

from graphs.delay_aware_slicing.lines_graph import *

fig_size = [10, 3.4]

# Throughput graph (Isolani)
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/isolani/main/",
    filename="wtp1_throughput",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['QoS 1', 'BE 1', 'BE 2', 'BE 3', 'QoS 2'],
    y_axis_label='Dequeueing rate (Mbps)',
    y_axis_min_max={'min': 0, 'max': 15},
    fig_size=fig_size)

make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/isolani/main/",
    filename="wtp4_throughput",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['QoS 1', 'BE 1', 'BE 2', 'BE 3', 'QoS 2'],
    y_axis_label='Dequeueing rate (Mbps)',
    y_axis_min_max={'min': 0, 'max': 15},
    fig_size=fig_size)

# make_line_graph(
#     experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/isolani/main/",
#     filename="channel_utilization",
#     x_axis='Time',
#     x_axis_label='Time (sec)',
#     y_axes=['Resource Block 1', 'Resource Block 2'],
#     y_axis_label='Dequeueing rate (Mbps)',
#     y_axis_min_max={'min': 0, 'max': 0.002},
#     fig_size=fig_size)

# Queueing delay graphs (Isolani)
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/isolani/main/",
    filename="wtp1_queueing_delay",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['QoS 1', 'BE 1', 'BE 2', 'BE 3', 'QoS 2'],
    y_axis_label='Queueing delay (ms)',
    y_axis_min_max={'min': 0, 'max': 100000},
    y_log_scale=True,
    fig_size=fig_size)

make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/isolani/main/",
    filename="wtp4_queueing_delay",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['QoS 1', 'BE 1', 'BE 2', 'BE 3', 'QoS 2'],
    y_axis_label='Queueing delay (ms)',
    y_axis_min_max={'min': 0, 'max': 100000},
    y_log_scale=True,
    fig_size=fig_size)

# Slices current quantum graph
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/isolani/main/",
    filename="slices_current_quantum",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['QoS 1', 'BE 1', 'BE 2', 'BE 3', 'QoS 2'],
    y_axis_label='Current quantum (us)',
    y_axis_min_max={'min': 0, 'max': 20000},
    fig_size=fig_size)

# # # Slices current deficit
# # make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/queueing_delay_results/",
# #                 filename="slice_current_deficit_wtp_1",
# #                 x_axis='Time',
# #                 x_axis_label='Time (sec)',
# #                 y_axes=['QoS 1','BE 1','BE 2','BE 3','QoS 2'],
# #                 y_axis_label='Current deficit (us)',
# #                 y_axis_min_max={'min': 0, 'max': 16000},
# #                 fig_size=fig_size)
# #
# # make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/queueing_delay_results/",
# #                 filename="slice_current_deficit_wtp_4",
# #                 x_axis='Time',
# #                 x_axis_label='Time (sec)',
# #                 y_axes=['QoS 1','BE 1','BE 2','BE 3','QoS 2'],
# #                 y_axis_label='Current deficit (us)',
# #                 y_axis_min_max={'min': 0, 'max': 16000},
# #                 fig_size=fig_size)
#
# Association results (Isolani)
make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/isolani/main/",
                filename="wtp1_association",
                x_axis='Time',
                x_axis_label='Time (sec)',
                x_axis_min_max={'min': 0, 'max': 300},
                y_axes=['STA 1', 'STA 2', 'STA 3', 'STA 4'],
                y_axis_label='Assigned STAs',
                y_axis_min_max={'min': 0, 'max': 6},
                fig_size=fig_size,
                stacked=True)

make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/isolani/main/",
                filename="wtp4_association",
                x_axis='Time',
                x_axis_label='Time (sec)',
                x_axis_min_max={'min': 0, 'max': 300},
                y_axes=['STA 1', 'STA 2', 'STA 3', 'STA 4'],
                y_axis_label='Assigned STAs',
                y_axis_min_max={'min': 0, 'max': 6},
                fig_size=fig_size,
                stacked=True)

# Association results (Gomez)
make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/gomez/main/",
                filename="wtp1_association",
                x_axis='Time',
                x_axis_label='Time (sec)',
                x_axis_min_max={'min': 0, 'max': 300},
                y_axes=['STA 1', 'STA 2', 'STA 3', 'STA 4'],
                y_axis_label='Assigned STAs',
                y_axis_min_max={'min': 0, 'max': 6},
                fig_size=fig_size,
                stacked=True)

make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/gomez/main/",
                filename="wtp4_association",
                x_axis='Time',
                x_axis_label='Time (sec)',
                x_axis_min_max={'min': 0, 'max': 300},
                y_axes=['STA 1', 'STA 2', 'STA 3', 'STA 4'],
                y_axis_label='Assigned STAs',
                y_axis_min_max={'min': 0, 'max': 6},
                fig_size=fig_size,
                stacked=True)

# Throughput graph (Gomez)
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/gomez/main/",
    filename="wtp1_throughput",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['QoS 1', 'BE 1', 'BE 2', 'BE 3', 'QoS 2'],
    y_axis_label='Dequeueing rate (Mbps)',
    y_axis_min_max={'min': 0, 'max': 20},
    fig_size=fig_size)

make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/gomez/main/",
    filename="wtp4_throughput",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['QoS 1', 'BE 1', 'BE 2', 'BE 3', 'QoS 2'],
    y_axis_label='Dequeueing rate (Mbps)',
    y_axis_min_max={'min': 0, 'max': 20},
    fig_size=fig_size)


# Queueing delay graphs (Gomez)
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/gomez/main/",
    filename="wtp1_queueing_delay",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['QoS 1', 'BE 1', 'BE 2', 'BE 3', 'QoS 2'],
    y_axis_label='Queueing delay (ms)',
    y_axis_min_max={'min': 0, 'max': 100000},
    y_log_scale=True,
    fig_size=fig_size)

make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/gomez/main/",
    filename="wtp4_queueing_delay",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['QoS 1', 'BE 1', 'BE 2', 'BE 3', 'QoS 2'],
    y_axis_label='Queueing delay (ms)',
    y_axis_min_max={'min': 0, 'max': 100000},
    y_log_scale=True,
    fig_size=fig_size)