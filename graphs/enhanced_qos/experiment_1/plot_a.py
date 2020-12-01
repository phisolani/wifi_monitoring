#!/usr/bin/env python
__author__ = "Daniel Kulenkamp"
__copyright__ = "Copyright 2020, QoS-aware WiFi Slicing"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Kulenkamp"
__email__ = "dkulenka@asu.edu"
__status__ = "Prototype"

"Python script for making all graphs at once for sensors experiment 1"

from graphs.enhanced_qos.lines_graph import make_share_x_graph
from graphs.enhanced_qos.experiment1_styles import experiment1_styles

# Scenario A (UL v UL)
path = 'scenario_a/'
filename = 'a_results'
x_axis_min_max = {'min': 0, 'max': 300}
output_name = 'plots/scenario_a_sharex_graph'

plot_info = {
    'x_axis': 'Time',
    'x_axis_label': 'Time (sec)',
    'x_axis_min_max': x_axis_min_max,
    'subplots': [
        {
            'y_shared': False,
            'y_axes': ['Shaper BE', 'Shaper QoS','Throughput BE', 'Throughput QoS'],
            'y_axes_labels': [r'$\lambda^{STA 1}$', r'$\lambda^{STA 2}$',
                              r'$\mu^{BE, STA 1}$', r'$\mu^{QoS, STA 2}$'],
            'y_axis_min_max': {'min': 0, 'max': 1000},
            'y_axis_label': 'Throughput (Mbps)',
            'y_log_scale': True,
            'y_axis_colors': experiment1_styles['colors']['shaper'] + experiment1_styles['colors']['throughput'],
            'y_axis_styles': experiment1_styles['line_styles']['shaper'] + experiment1_styles['line_styles']['throughput'],
        },
        {
            'y_shared': True,
            'y_axes': ['Shaper BE', 'Shaper QoS'],
            'y_axes_labels': [r'$\lambda^{STA 1}$', r'$\lambda^{STA 2}$'],
            'y_axis_min_max': {'min': 0, 'max': 1000},
            'y_axis_label': 'Throughput (Mbps)',
            'y_log_scale': True,
            'y_axis_colors': experiment1_styles['colors']['shaper'],
            'y_axis_styles': experiment1_styles['line_styles']['shaper'],
            'right_y_axes': ['Delay BE', 'Delay QoS'],
            'right_y_axes_labels': [r'$D^{BE}$', r'$D^{QoS}$'],
            'right_y_axis_min_max': {'min': 0, 'max': 50},
            'right_y_axis_label': 'Queueing delay (ms)',
            'right_y_log_scale': True,
            'right_y_axis_colors': experiment1_styles['colors']['delay'],
            'right_y_axis_styles': experiment1_styles['line_styles']['delay'],
        },
        {
            'y_shared': True,
            'y_axes': ['Shaper BE', 'Shaper QoS'],
            'y_axes_labels': [r'$\lambda^{STA 1}$', r'$\lambda^{STA 2}$'],
            'y_axis_min_max': {'min': 0, 'max': 1000},
            'y_axis_label': 'Throughput (Mbps)',
            'y_log_scale': True,
            'y_axis_colors': experiment1_styles['colors']['shaper'],
            'y_axis_styles': experiment1_styles['line_styles']['shaper'],
            'right_y_axes': ['Loss BE', 'Loss QoS'],
            'right_y_axes_labels': [r'$\lambda^{STA 1}_{\mathrm{LOSS}}$', r'$\lambda^{STA 2}_{\mathrm{LOSS}}$'],
            'right_y_axis_min_max': {'min': 0, 'max': 300},
            'right_y_axis_label': 'Loss (frames/sec)',
            'right_y_log_scale': False,
            'right_y_axis_colors': experiment1_styles['colors']['loss'],
            'right_y_axis_styles': experiment1_styles['line_styles']['loss'],
         }
    ]
}

fig_size = [14, 8]
make_share_x_graph(
    experiment_path=path,
    filename=filename,
    fig_size=fig_size,
    output_name=output_name,
    plot_info=plot_info
)
