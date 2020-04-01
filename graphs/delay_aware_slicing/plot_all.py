#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2020, QoS-aware WiFi Slicing"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

" Python script for making all graphs at once"

from graphs.delay_aware_slicing.lines import *

# Throughput graph
make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/throughput_results/",
                filename="throughput_wtp_1",
                x_axis='Time',
                x_axis_label='Time (sec)',
                y_axes=['0x01', '0x02', '0x03', '0x08', '0x20'],
                y_axis_label='Throughput (Mbps)',
                y_axis_min_max={'min': 0, 'max': 15},
                fig_size=[10, 3.4])

make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/throughput_results/",
                filename="throughput_wtp_4",
                x_axis='Time',
                x_axis_label='Time (sec)',
                y_axes=['0x01', '0x02', '0x03', '0x08', '0x20'],
                y_axis_label='Throughput (Mbps)',
                y_axis_min_max={'min': 0, 'max': 8},
                fig_size=[10, 3.4])

make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/throughput_results/",
                filename="channel_utilization",
                x_axis='Time',
                x_axis_label='Time (sec)',
                y_axes=['Resource Block 1', 'Resource Block 2'],
                y_axis_label='Throughput (Mbps)',
                y_axis_min_max={'min': 0, 'max': 0.002},
                fig_size=[10, 3.4])

# Queueing delay graphs
make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/queueing_delay_results/",
                filename="queueing_delay_wtp_1",
                x_axis='Time',
                x_axis_label='Time (sec)',
                y_axes=['0x01', '0x02', '0x03', '0x08', '0x20'],
                y_axis_label='Queueing delay (ms)',
                y_axis_min_max={'min': 0, 'max': 100000},
                y_log_scale=True,
                fig_size=[10, 3.4])

make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/queueing_delay_results/",
                filename="queueing_delay_wtp_4",
                x_axis='Time',
                x_axis_label='Time (sec)',
                y_axes=['0x01', '0x02', '0x03', '0x08', '0x20'],
                y_axis_label='Queueing delay (ms)',
                y_axis_min_max={'min': 0, 'max': 100000},
                y_log_scale=True,
                fig_size=[10, 3.4])

# Slices current quantum graph
make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/queueing_delay_results/",
                filename="slice_current_quantum",
                x_axis='Time',
                x_axis_label='Time (sec)',
                y_axes=['0x01', '0x02', '0x03', '0x08', '0x20'],
                y_axis_label='Current quantum (us)',
                y_axis_min_max={'min': 0, 'max': 16000},
                fig_size=[10, 3.4])

# # Slices current deficit
# make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/queueing_delay_results/",
#                 filename="slice_current_deficit_wtp_1",
#                 x_axis='Time',
#                 x_axis_label='Time (sec)',
#                 y_axes=['0x01', '0x02', '0x03', '0x08', '0x20'],
#                 y_axis_label='Current deficit (us)',
#                 y_axis_min_max={'min': 0, 'max': 16000},
#                 fig_size=[10, 3.4])
#
# make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/queueing_delay_results/",
#                 filename="slice_current_deficit_wtp_4",
#                 x_axis='Time',
#                 x_axis_label='Time (sec)',
#                 y_axes=['0x01', '0x02', '0x03', '0x08', '0x20'],
#                 y_axis_label='Current deficit (us)',
#                 y_axis_min_max={'min': 0, 'max': 16000},
#                 fig_size=[10, 3.4])

# MCDA results
make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/mcda_results/",
                filename="mcda_association_wtp_1",
                x_axis='Time',
                x_axis_label='Time (sec)',
                x_axis_min_max={'min': 0, 'max': 300},
                y_axes=['STA 1', 'STA 2', 'STA 3', 'STA 4'],
                y_axis_label='Assigned STAs',
                y_axis_min_max={'min': 0, 'max': 6},
                fig_size=[10, 3.4],
                stacked=True)

make_line_graph(experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/mcda_results/",
                filename="mcda_association_wtp_4",
                x_axis='Time',
                x_axis_label='Time (sec)',
                x_axis_min_max={'min': 0, 'max': 300},
                y_axes=['STA 1', 'STA 2', 'STA 3', 'STA 4'],
                y_axis_label='Assigned STAs',
                y_axis_min_max={'min': 0, 'max': 6},
                fig_size=[10, 3.4],
                stacked=True)