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


def plot_c():
    # Scenario C (DL v UL)
    path = 'scenario_c/'
    filename = 'c_results'
    x_axis_min_max = {'min': 0, 'max': 200}
    output_name = 'plots/scenario_c_sharex_graph'
    fig_size = [9, 10]

    plot_info = {
        'x_axis': 'Time',
        'x_axis_label': 'Time (sec)',
        'x_axis_min_max': x_axis_min_max,
        'subplots': [
            {
                'y_shared': False,
                'y_axes': ['Throughput BE', 'Throughput QoS'],
                'y_axes_labels': [r'$\mu^{BE, STA 1}$', r'$\mu^{QoS, STA 2}$'],
                'y_axis_min_max': {'min': 0, 'max': 30},
                'y_axis_label': 'Throughput (Mbps)',
                'y_log_scale': False,
                'y_axis_colors': experiment1_styles['colors']['throughput'],
                'y_axis_styles': experiment1_styles['line_styles']['throughput'],
                'qos_annotation': {
                    'type': 'throughput',
                    'value': 10,
                    'color': experiment1_styles['colors']['requirement'][0],
                    'line_style': experiment1_styles['line_styles']['requirement'][0],
                    'sta_num': 'STA2',
                },
            },
            {
                'y_shared': False,
                'y_axes': ['Quantum BE'],
                'y_axes_labels': [r'$Q^{BE}$'],
                'y_axis_min_max': {'min': 0, 'max': 75000},
                'y_axis_label': 'Current Quantum (μs)',
                'y_log_scale': True,
                'y_axis_colors': experiment1_styles['colors']['quantum'],
                'y_axis_styles': experiment1_styles['line_styles']['quantum'],
                'qos_annotation': False,
            },
            {
                'y_shared': False,
                'y_axes': ['Delay BE'],
                'y_axes_labels': [r'$D^{BE}$'],
                'y_axis_min_max': {'min': 0, 'max': 1200},
                'y_axis_label': 'Queueing Delay (ms)',
                'y_log_scale': False,
                'y_axis_colors': experiment1_styles['colors']['delay'],
                'y_axis_styles': experiment1_styles['line_styles']['delay'],
                'qos_annotation': False,
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

def plot_c_old():
    fig_size = [5, 4]

    # Scenario B (DL v UL)
    path = 'scenario_c/'
    filename = 'c_results'
    x_axis_min_max = {'min': 0, 'max': 300}

    #Throughput
    output_name = 'scenario_c_throughput'
    make_line_graph(
        experiment_path=path,
        filename=filename,
        x_axis='Time',
        x_axis_label='Time (sec)',
        x_axis_min_max=x_axis_min_max,
        y_axes=['Throughput BE', 'Throughput QoS'],
        y_axis_label='Throughput (Mbps)',
        y_axis_min_max={'min': 0, 'max': 35},
        markers=["", "", "D", "1"],
        fig_size=fig_size,
        output_name=output_name
    )
    # Quantum
    output_name = 'scenario_c_quantum'
    make_line_graph(
        experiment_path=path,
        filename=filename,
        x_axis='Time',
        x_axis_label='Time (sec)',
        x_axis_min_max=x_axis_min_max,
        y_axes=['Quantum'],
        y_axis_label='Current Quantum (μsec)',
        y_axis_min_max={'min': 0, 'max': 12000},
        y_log_scale=True,
        fig_size=fig_size,
        output_name=output_name
    )
    # Delay
    output_name = 'scenario_c_delay'
    make_line_graph(
        experiment_path=path,
        filename=filename,
        x_axis='Time',
        x_axis_label='Time (sec)',
        x_axis_min_max=x_axis_min_max,
        y_axes=['Delay BE'],
        y_axis_label='Delay (msec)',
        y_axis_min_max={'min': 0, 'max': 1000},
        fig_size=fig_size,
        output_name=output_name
    )

if __name__ == '__main__':
    plot_c()