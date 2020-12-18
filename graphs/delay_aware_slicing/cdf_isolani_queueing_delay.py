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
cdf_data = pd.read_csv("results/isolani/main/cdf_isolani_queueing_delay.csv",
                        usecols=col_list, sep=';')

qos_flows = ['QoS 1', 'QoS 2']

for qos_flow in qos_flows:
    # Frequency
    stats_df = cdf_data.groupby(qos_flow)[qos_flow].agg('count').pipe(pd.DataFrame).rename(
        columns={qos_flow: 'frequency'})

    # PDF
    stats_df['pdf'] = stats_df['frequency'] / sum(stats_df['frequency'])

    # CDF
    stats_df['cdf'] = stats_df['pdf'].cumsum()
    stats_df = stats_df.reset_index()
    print(stats_df.to_string())

sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)
fig, ax = plt.subplots(figsize=(10, 3.6))
plt.rcParams['mathtext.fontset'] = 'stix'

# plot the cumulative histogram
n, bins, patches = ax.hist(cdf_data['QoS 1'].values,
                           n_bins,
                           density=True,
                           histtype='step',
                           cumulative=True,
                           color=colors[0],
                           linestyle=line_styles[0],
                           linewidth=2,
                           # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
                           label='QoS 1')

ax.hist(cdf_data['BE 1'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[1],
        linestyle=line_styles[1],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 1')

ax.hist(cdf_data['BE 2'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[2],
        linestyle=line_styles[2],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 2')

ax.hist(cdf_data['BE 3'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[3],
        linestyle=line_styles[3],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 3')

ax.hist(cdf_data['QoS 2'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[4],
        linestyle=line_styles[4],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='QoS 2')

ax.annotate(r'$D^{QoS2}_{QoS} (68\%)$',
            xy=(50, 0.68),
            xytext=(300, 0.68),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

ax.annotate(r'$D^{QoS1}_{QoS} (95\%)$',
            xy=(30, 0.95),
            xytext=(350, 0.9),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# tidy up the figure
ax.grid(True)
ax.legend(loc='right')
# ax.set_xscale('log')
# ax.set_title('Cumulative step histograms')
ax.set_xlabel('Queueing delay (ms)')
ax.set_ylabel('Likelihood (%)')
plt.yticks(np.arange(0, 1.01, 0.2))
ax.set_xticks([0, 50, 100, 200, 300, 400, 500, 600,  700, 800, 900, 1000])
# ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.tight_layout()
filename = "results/isolani/main/cdf_isolani_queueing_delay"
plt.savefig(str(filename) + '.pdf', format="pdf", bbox_inches="tight")
plt.savefig(str(filename) + '.png', format="png", bbox_inches="tight")
plt.savefig(str(filename) + '.eps', format="eps", bbox_inches="tight")

plt.show()



