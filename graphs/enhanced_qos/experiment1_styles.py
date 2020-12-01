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
        'throughput': ['tab:blue', 'tab:cyan'],
        'shaper': ['tab:orange', 'gold'],
        'delay': ['tab:green', 'limegreen'],
        'loss': ['magenta', 'hotpink'],
        'quantum': ['purple', 'mediumpurple'],
    },
    'line_styles': {
        'throughput': ['-', '-'],
        'shaper': ['--', '--'],
        'delay': [':', ':'],
        'loss': ['-.', '-.'],
        'quantum': ['--', '--'],
    },
}
