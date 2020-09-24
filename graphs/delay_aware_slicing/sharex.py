#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2020, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

" Python script for making graphs with CSV output"

import matplotlib.pyplot as plt
import seaborn as sns

from graphs.delay_aware_slicing import lines_graph

# Applying Seaborn style
# whitegrid, darkgrid, whitegrid, dark, white, and ticks
sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.3, color_codes=True, rc=None)

colors = ['g', 'b', 'c', 'm', 'y']
line_styles = ['-', '--', ':', '-.', '-', '--', ':', '-.']
markers = ['o', '^', '+', 'x', '*', 'D']

# Experiment (Isolani)
experiments = [
    {
        'name': 'isolani',
        'location': '/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/isolani/main/'
    },
    {
        'name': 'gomez',
        'location': '/Users/phisolani/Github/wifi_monitoring/graphs/delay_aware_slicing/results/gomez/main/'
    }
]

x_axis = 'Time'
x_axis_label = 'Time (sec)'

y_axes_stas = ['STA 1', 'STA 2', 'STA 3', 'STA 4']
y_axes_slices = ['QoS 1', 'BE 1', 'BE 2', 'BE 3', 'QoS 2']

wtps = ['wtp1', 'wtp4']

for experiment in experiments:
    for wtp in wtps:
        # Starting figure
        f = plt.figure(figsize=(8.2, 7), dpi=144)

        # First plot ----
        ax1 = f.add_subplot(311)

        # Adjust x Axis
        plt.tight_layout()

        # Reading CSV results
        csv_file = experiment['location'] + wtp + '_association' + '.csv'
        data_dict = lines_graph.read_results(filename=csv_file, x_axis=x_axis, y_axes=y_axes_stas)

        y_values = []
        for axis in data_dict:
            if 'x_axis' not in axis:
                y_values.append(data_dict[axis]['values'])

        pal = ["g", "b", "m", "y"]

        stacks = ax1.stackplot(data_dict['x_axis']['values'], y_values, labels=y_axes_stas, colors=pal)
        # colors=pal, alpha=0.6)
        hatches = ['+', 'x', '.', '*', '\\', 'O', 'o', '-']
        for stack, hatch in zip(stacks, hatches):
            stack.set_hatch(hatch)

        plt.legend(loc='upper left')
        ax1.set_ylabel("Assigned STAs")

        plt.legend(y_axes_stas, loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=len(y_axes_stas))  # shadow=True)
        plt.ylim(0, 6)
        plt.setp(ax1.get_xticklabels(), visible=False)

        xcoords = [10, 40, 70, 100, 130, 160, 190]
        for xc in xcoords:
            plt.axvline(x=xc, linestyle='--', color='dimgray')

        # Second plot ----------------
        ax2 = f.add_subplot(312, sharex=ax1)

        # Reading CSV results
        csv_file = experiment['location'] + wtp + '_throughput' + '.csv'
        data_dict = lines_graph.read_results(filename=csv_file, x_axis=x_axis, y_axes=y_axes_slices)

        lines = []
        for y in range(len(y_axes_slices)):
            p, = ax2.plot(data_dict['x_axis']['values'], data_dict['y' + str(y) + '_axis']['values'],
                          color=colors[y],
                          linestyle=line_styles[y],
                          linewidth=2,
                          label=str(y_axes_slices[y]))
            lines.append(p)

        plt.legend(y_axes_slices, loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=len(y_axes_slices))  # shadow=True)
        ax2.set_ylabel("Dequeueing rate (Mbps)")
        plt.ylim(0, 20)
        plt.setp(ax2.get_xticklabels(), visible=False)

        xcoords = [10, 40, 70, 100, 130, 160, 190]
        for xc in xcoords:
            plt.axvline(x=xc, linestyle='--', color='dimgray')

        # Third plot ----------------
        ax3 = f.add_subplot(313, sharex=ax1)
        ax3.set_yscale('log')

        # Reading CSV results
        csv_file = experiment['location'] + wtp + '_queueing_delay' + '.csv'
        data_dict = lines_graph.read_results(filename=csv_file, x_axis=x_axis, y_axes=y_axes_slices)
        #
        lines = []
        for y in range(len(y_axes_slices)):
            p, = ax3.plot(data_dict['x_axis']['values'], data_dict['y' + str(y) + '_axis']['values'],
                          color=colors[y],
                          linestyle=line_styles[y],
                          linewidth=2,
                          label=str(y_axes_slices[y]))
            lines.append(p)

        plt.legend(y_axes_slices, loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=len(y_axes_slices))  # shadow=True)
        ax3.set_ylabel("Queueing delay (ms)")
        ax3.set_xlabel("Time (sec)")
        plt.ylim(0, 100000)
        plt.setp(ax3.get_xticklabels(), visible=True)

        xcoords = [10, 40, 70, 100, 130, 160, 190]
        for xc in xcoords:
            plt.axvline(x=xc, linestyle='--', color='dimgray')

        plt.xlim(0, 300.0)

        plt.savefig('sharex_' + experiment['name'] + '_' + wtp + '.eps', format="eps", bbox_inches="tight")
        plt.savefig('sharex_' + experiment['name'] + '_' + wtp + '.png', format="png", bbox_inches="tight")
        plt.show()