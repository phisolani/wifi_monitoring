#!/usr/bin/env python
__author__ = "Pedro Heleno Isolani"
__copyright__ = "Copyright 2020, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pedro Heleno Isolani"
__email__ = "pedro.isolani@uantwerpen.be"
__status__ = "Prototype"

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter

n_bins = 50

# colors = ['darkolivegreen', 'darkblue', 'deepskyblue', 'magenta', 'goldenrod']
colors = ['g', 'b', 'c', 'm', 'y']
line_styles = ['-', '--', ':', '-.', '-', '--', ':', '-.']
col_list = ["QoS 1", "BE 1", "BE 2", "BE 3", "QoS 2"]

sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.3, color_codes=True, rc=None)
# fig, ax = plt.subplots(figsize=(5, 3.6))

# Starting figure
f = plt.figure(figsize=(9.5, 3.4), dpi=144)

cdf_delay = pd.read_csv("results/isolani/main/cdf_isolani_queueing_delay.csv",
                             usecols=col_list, sep=';')
cdf_throughput = pd.read_csv("results/isolani/main/cdf_isolani_throughput.csv",
                             usecols=col_list, sep=';')

# First plot ----
ax1 = f.add_subplot(121)

# plot the cumulative histogram
n, bins, patches = ax1.hist(cdf_throughput['QoS 1'].values,
                           n_bins,
                           density=True,
                           histtype='step',
                           cumulative=True,
                           color=colors[0],
                           linestyle=line_styles[0],
                           linewidth=2,
                           # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
                           label='QoS 1')

ax1.hist(cdf_throughput['BE 1'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[1],
        linestyle=line_styles[1],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 1')

ax1.hist(cdf_throughput['BE 2'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[2],
        linestyle=line_styles[2],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 2')

ax1.hist(cdf_throughput['BE 3'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[3],
        linestyle=line_styles[3],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 3')

ax1.hist(cdf_throughput['QoS 2'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[4],
        linestyle=line_styles[4],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='QoS 2')

# tidy up the figure
ax1.grid(True)
ax1.legend(loc='right')
# ax.set_title('Cumulative step histograms')
ax1.set_xlabel('Dequeueing rate (Mbps)')
ax1.set_ylabel('Likelihood (%)')
plt.yticks(np.arange(0, 1.01, 0.2))
plt.xticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.tight_layout()

# share x only
ax2 = plt.subplot(122, sharey=ax1)
# make these tick labels invisible
plt.setp(ax2.get_yticklabels(), visible=False)


# plot the cumulative histogram
n, bins, patches = ax2.hist(cdf_delay['QoS 1'].values,
                           n_bins,
                           density=True,
                           histtype='step',
                           cumulative=True,
                           color=colors[0],
                           linestyle=line_styles[0],
                           linewidth=2,
                           # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
                           label='QoS 1')

ax2.hist(cdf_delay['BE 1'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[1],
        linestyle=line_styles[1],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 1')

ax2.hist(cdf_delay['BE 2'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[2],
        linestyle=line_styles[2],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 2')

ax2.hist(cdf_delay['BE 3'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[3],
        linestyle=line_styles[3],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 3')

ax2.hist(cdf_delay['QoS 2'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[4],
        linestyle=line_styles[4],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='QoS 2')

ax2.annotate(r'$D^{QoS2}_{QoS}$ (76%)',
            xy=(50, 0.76),
            xytext=(560, 0.35),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

ax2.annotate(r'$D^{QoS1}_{QoS}$ (95%)',
            xy=(30, 0.95),
            xytext=(550, 0.86),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# tidy up the figure
ax2.grid(True)
ax2.legend(loc='center right', ncol=1)
# ax.set_xscale('log')
# ax.set_title('Cumulative step histograms')
ax2.set_xlabel('Queueing delay (ms)')
# plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
plt.yticks(np.arange(0, 1.01, 0.25))
ax2.set_xticks([0, 250, 500, 750, 1000])
# ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.tight_layout()
filename = "results/isolani/main/cdf_isolani"

plt.savefig(str(filename) + '.pdf', format="pdf", bbox_inches="tight")
plt.savefig(str(filename) + '.png', format="png", bbox_inches="tight")
plt.savefig(str(filename) + '.eps', format="eps", bbox_inches="tight")
plt.show()