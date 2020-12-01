#!/usr/bin/env python
__author__ = "Daniel Kulenkamp"
__copyright__ = "Copyright 2020, QoS-aware WiFi Slicing"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Kulenkamp"
__email__ = "dkulenka@asu.edu"
__status__ = "Prototype"

" Python script for making all graphs at once for sensors experiment 1"

from graphs.enhanced_qos.lines_graph import make_share_x_graph
from graphs.enhanced_qos.experiment1_styles import experiment1_styles

def plot_b_rpi():
    fig_size = [14, 5]

    # Scenario B (DL v UL)
    path = 'scenario_b_rpi/'
    filename = 'brpi_results'
    x_axis_min_max = {'min': 0, 'max': 300}
    output_name = 'plots/scenario_brpi_sharex_graph'

    plot_info = {
        'x_axis': 'Time',
        'x_axis_label': 'Time (sec)',
        'x_axis_min_max': x_axis_min_max,
        'subplots': [
            {
                'y_shared': False,
                'y_axes': ['Shaper BE','Throughput BE', 'Throughput QoS'],
                'y_axes_labels': [r'$\lambda^{STA 1}$',
                                  r'$\mu^{BE, STA 1}$', r'$\mu^{QoS, STA 2}$'],
                'y_axis_min_max': {'min': 0, 'max': 1500},
                'y_axis_label': 'Throughput (Mbps)',
                'y_log_scale': True,
                'y_axis_colors': experiment1_styles['colors']['shaper'][:1] + experiment1_styles['colors']['throughput'],
                'y_axis_styles': experiment1_styles['line_styles']['shaper'][:1] + experiment1_styles['line_styles']['throughput'],
                'qos_annotation': False,
            },
            {
                'y_shared': False,
                'y_axes': ['Delay QoS'],
                'y_axes_labels': [r'$D^{QoS}$'],
                'y_axis_min_max': {'min': 0, 'max': 40000},
                'y_axis_label': 'Queuing Delay (ms)',
                'y_log_scale': True,
                'y_axis_colors': experiment1_styles['colors']['delay'][1:],
                'y_axis_styles': experiment1_styles['line_styles']['delay'][1:],
                'qos_annotation': {
                    'type': 'delay',
                    'value': 30,
                    'color': experiment1_styles['colors']['requirement'][0],
                    'line_style': experiment1_styles['line_styles']['requirement'][0],
                    'sta_num': 'STA2',

                },
            }
        ]
    }

    make_share_x_graph(
        experiment_path=path,
        filename=filename,
        fig_size=fig_size,
        output_name=output_name,
        plot_info=plot_info
    )

if __name__ == '__main__':
    plot_b_rpi()