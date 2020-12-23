#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2020, QoS-aware WiFi Slicing"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

" Python script for making all graphs at once"

from graphs.btw.lines_graph import *

fig_size = [10, 3.4]

# MCS experiment E2E latency
make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_mcs/",
    filename="apps_e2e_latency",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['APP 1', 'APP 2', 'APP 3', 'APP 4'],
    y_axis_label='Latency (ms)',
    y_axis_min_max={'min': 0.1, 'max': 100000},
    y_log_scale=True,
    log_type='symlog',
    fig_size=fig_size)

make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/experiment_mcs/",
    filename="apps_e2e_jitter",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axes=['APP 1', 'APP 2', 'APP 3', 'APP 4'],
    y_axis_label='Jitter (ms)',
    y_axis_min_max={'min': 0.1, 'max': 100000},
    y_log_scale=True,
    log_type='symlog',
    fig_size=fig_size)

make_line_graph(
    experiment_path="/Users/phisolani/Github/wifi_monitoring/graphs/btw/",
    filename="eggs",
    x_axis='Time',
    x_axis_label='Time (sec)',
    y_axis_min_max={'min': 0, 'max': 12},
    y_axes=['APP: 3 - Node: 11','APP: 3 - Node: 8860215','APP: 4 - Node: 11880865','APP: 4 - Node: 12','APP: 2 - Node: 13','APP: 2 - Node: 8860310','APP: 1 - Node: 11879605','APP: 1 - Node: 13'],
    y_axis_label='MCS',
    fig_size=fig_size)