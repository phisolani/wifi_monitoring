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

n_bins = 5000

# colors = ['darkolivegreen', 'darkblue', 'deepskyblue', 'magenta', 'goldenrod']
colors = ['g', 'b', 'c', 'm', 'y']
line_styles = ['-', '--', ':', '-.', '-', '--', ':', '-.']
col_list = ["QoS 1", "BE 1", "BE 2", "BE 3", "QoS 2"]
cdf_throughput = pd.read_csv("results/isolani/main/cdf_isolani_throughput.csv",
                             usecols=col_list, sep=';')

sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)
fig, ax = plt.subplots(figsize=(10, 3.6))
plt.rcParams['mathtext.fontset'] = 'stix'

# plot the cumulative histogram
n, bins, patches = ax.hist(cdf_throughput['QoS 1'].values,
                           n_bins,
                           density=True,
                           histtype='step',
                           cumulative=True,
                           color=colors[0],
                           linestyle=line_styles[0],
                           linewidth=2,
                           # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
                           label='QoS 1')

ax.hist(cdf_throughput['BE 1'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[1],
        linestyle=line_styles[1],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 1')

ax.hist(cdf_throughput['BE 2'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[2],
        linestyle=line_styles[2],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 2')

ax.hist(cdf_throughput['BE 3'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[3],
        linestyle=line_styles[3],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 3')

ax.hist(cdf_throughput['QoS 2'].values,
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
ax.grid(True)
ax.legend(loc='right')
# ax.set_title('Cumulative step histograms')
ax.set_xlabel('Dequeueing rate (Mbps)')
ax.set_ylabel('Likelihood (%)')
plt.yticks(np.arange(0, 1.01, 0.2))
plt.xticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.tight_layout()
filename = "results/isolani/main/cdf_isolani_throughput"
plt.savefig(str(filename) + '.pdf', format="pdf", bbox_inches="tight")
plt.savefig(str(filename) + '.png', format="png", bbox_inches="tight")
plt.savefig(str(filename) + '.eps', format="eps", bbox_inches="tight")

plt.show()



