#!/usr/bin/env python
__author__ = 'Pedro Heleno Isolani'
__copyright__ = 'Copyright 2020, The SDN WiFi MAC Manager'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'Pedro Heleno Isolani'
__email__ = 'pedro.isolani@uantwerpen.be'
__status__ = 'Prototype'

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter

n_bins = 5000
colors = ['g', 'b', 'k']
line_styles = ['-', '--', ':', '-.']
col_list = ['BE 1', 'BE 2', 'QoS 2']
filename = 'isolani/throughput/overall_isolani_lvap_rx_mbps'
cdf_data = pd.read_csv(filename + '.csv', usecols=col_list, sep=';')
print(cdf_data)

# Frequency
stats_df = cdf_data.groupby('QoS 2')['QoS 2'].agg('count').pipe(pd.DataFrame).rename(columns = {'QoS 2': 'frequency'})

# PDF
stats_df['pdf'] = stats_df['frequency'] / sum(stats_df['frequency'])

# CDF
stats_df['cdf'] = stats_df['pdf'].cumsum()
stats_df = stats_df.reset_index()
print(stats_df.to_string())

sns.set(style='whitegrid', font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)
# Sensors
# fig, ax = plt.subplots(figsize=(5, 4))
# Thesis
fig, ax = plt.subplots(figsize=(4.5, 4))
plt.rcParams['mathtext.fontset'] = 'stix'

# plot the cumulative histogram
n, bins, patches = ax.hist(cdf_data['BE 1'].values,
                           n_bins,
                           density=True,
                           histtype='step',
                           cumulative=-1,
                           color=colors[0],
                           linestyle=line_styles[0],
                           linewidth=2,
                           # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
                           label='BE 1')

ax.hist(cdf_data['BE 2'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=-1,
        color=colors[1],
        linestyle=line_styles[1],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 2')

ax.hist(cdf_data['QoS 2'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=-1,
        color=colors[2],
        linestyle=line_styles[2],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='QoS 2')

plt.axvline(x=5, linestyle=':', color='r', linewidth=2)
ax.annotate(r'$\mu^{QoS2}_{QoS} (76\%)$',
            xy=(5, 0.76),
            xytext=(18, 0.55),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# tidy up the figure
ax.grid(True)
ax.legend(loc='upper right')
# ax.set_xscale('log')
# ax.set_title('Cumulative step histograms')
ax.set_xlabel('Throughput (Mbps)')
ax.set_ylabel('Likelihood (%)')
# plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
plt.yticks(np.arange(0, 1.01, 0.2))
# ax.set_xticks([0, 5, 10, 15, 20])
ax.set_xlim(0, 20)
# ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.tight_layout()
plt.savefig(filename.replace('overall', 'cdf') +  '.pdf', format='pdf', bbox_inches='tight')
plt.savefig(filename.replace('overall', 'cdf') +  '.png', format='png', bbox_inches='tight')
plt.savefig(filename.replace('overall', 'cdf') +  '.eps', format='eps', bbox_inches='tight')
plt.show()
