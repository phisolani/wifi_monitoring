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

colors = ['darkolivegreen', 'darkblue', 'deepskyblue', 'magenta', 'goldenrod']
line_styles = ['-', '--', ':', '-.', '-', '--', ':', '-.']
col_list = ["QoS 1", "BE 1", "BE 2", "BE 3", "QoS 2"]
cdf_delay_mcda = pd.read_csv("cdf_results/gomez/delay_results/cdf_queueing_delay_gomez.csv",
                             usecols=col_list, sep=';')

sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)
fig, ax = plt.subplots(figsize=(10, 3.6))

# plot the cumulative histogram
n, bins, patches = ax.hist(cdf_delay_mcda['QoS 1'].values,
                           n_bins,
                           density=True,
                           histtype='step',
                           cumulative=True,
                           color=colors[0],
                           linestyle=line_styles[0],
                           linewidth=2,
                           # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
                           label='QoS 1')

ax.hist(cdf_delay_mcda['BE 1'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[1],
        linestyle=line_styles[1],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 1')

ax.hist(cdf_delay_mcda['BE 2'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[2],
        linestyle=line_styles[2],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 2')

ax.hist(cdf_delay_mcda['BE 3'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[3],
        linestyle=line_styles[3],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 3')

ax.hist(cdf_delay_mcda['QoS 2'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[4],
        linestyle=line_styles[4],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='QoS 2')

ax.annotate('50ms (70%)',
            xy=(50, 0.68),
            xytext=(250, 0.6),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

ax.annotate('30ms (86%)',
            xy=(30, 0.86),
            xytext=(500, 0.7),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# tidy up the figure
ax.grid(True)
ax.legend(loc='right')
# ax.set_xscale('log')
# ax.set_title('Cumulative step histograms')
ax.set_xlabel('Queueing delay (ms)')
ax.set_ylabel('Likelihood (%)')
# plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
plt.yticks(np.arange(0, 1.01, 0.2))
ax.set_xticks([0, 50, 100, 200, 300, 400, 500, 600,  700, 800, 900, 1000])
# ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.tight_layout()
filename = "cdf_queueing_delay_gomez"
plt.savefig(str(filename) + '.pdf', format="pdf", bbox_inches="tight")
plt.savefig(str(filename) + '.png', format="png", bbox_inches="tight")
plt.savefig(str(filename) + '.eps', format="eps", bbox_inches="tight")

plt.show()
