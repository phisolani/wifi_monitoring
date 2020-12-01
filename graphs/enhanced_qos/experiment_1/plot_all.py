#!/usr/bin/env python
__author__ = "Daniel Kulenkamp"
__copyright__ = "Copyright 2020, QoS-aware WiFi Slicing"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Kulenkamp"
__email__ = "dkulenka@asu.edu"
__status__ = "Prototype"

" Python script for making all graphs at once for sensors experiment 1 (all scenarios)."

import argparse
import sys
import os
import glob

from graphs.enhanced_qos.experiment_1.plot_a import plot_a
from graphs.enhanced_qos.experiment_1.plot_b_rpi import plot_b_rpi
from graphs.enhanced_qos.experiment_1.plot_b_node74 import plot_b_74
from graphs.enhanced_qos.experiment_1.plot_c import plot_c
from graphs.enhanced_qos.experiment_1.plot_d import plot_d



def clean_directories():
    dirs = [
        'scenario_a',
        'scenario_b_node74',
        'scenario_b_rpi',
        'scenario_c',
        'scenario_d',
    ]
    dirs = [os.path.join(dir, 'plots', '*') for dir in dirs]
    files = [glob.glob(dir) for dir in dirs]
    files = [file for array in files for file in array]
    for file in files:
        try:
            os.remove(file)
        except OSError as e:
            print(f'Error: {e}')

parser = argparse.ArgumentParser()
parser.add_argument("--clean", help="clean output directories before plotting")
parser.add_argument("--cleanOnly", help="only clean output directories--don't plot", action='store_true')
args = parser.parse_args()

if args.clean or args.cleanOnly:
    print('cleaning...')
    clean_directories()

if args.cleanOnly:
    print('exiting...')
    sys.exit()

print('Plotting scenario a...')
plot_a()

print('Plotting scenario b rpi...')
plot_b_rpi()

print('Plotting scenario b   74...')
plot_b_74()

print('Plotting scenario c...')
plot_c()

print('Plotting scenario d...')
plot_d()