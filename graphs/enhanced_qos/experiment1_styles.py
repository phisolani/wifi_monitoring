#!/usr/bin/env python
__author__ = "Daniel Kulenkamp"
__copyright__ = "Copyright 2020, QoS-aware WiFi Slicing"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Kulenkamp"
__email__ = "dkulenka@asu.edu"
__status__ = "Prototype"

"File for defining the colors and line styles for experiment 1 graphs"


experiment1_styles = {
    'colors': {
        'throughput': ['tab:blue', 'tab:orange'],
        'shaper': ['tab:red', 'tab:green'],
        'delay': ['tab:purple', 'tab:brown'],
        'loss': ['tab:pink', 'tab:gray'],
        'quantum': ['tab:olive', 'tab:cyan'],
    },
    'line_styles': {
        'throughput': ['-', '-'],
        'shaper': ['--', '--'],
        'delay': [':', ':'],
        'loss': ['-.', '-.'],
        'quantum': ['--', '--'],
    },
}
