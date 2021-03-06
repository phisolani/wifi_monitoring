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
colors = ['c', 'm', 'y', 'k']
line_styles = [':', '-.', '-', '--', ':', '-.']
col_list = ['BE 3', 'BE 4', 'QoS 1']
filename = 'isolani/queueing_delay/overall_isolani_slice_queueing_delay'
cdf_data = pd.read_csv(filename + '.csv', usecols=col_list, sep=';')
print(cdf_data)
# Frequency
stats_df = cdf_data.groupby('QoS 1')['QoS 1'].agg('count').pipe(pd.DataFrame).rename(columns = {'QoS 1': 'frequency'})

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
n, bins, patches = ax.hist(cdf_data['BE 3'].values,
                           n_bins,
                           density=True,
                           histtype='step',
                           cumulative=True,
                           color=colors[0],
                           linestyle=line_styles[0],
                           linewidth=2,
                           # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
                           label='BE 3')

ax.hist(cdf_data['BE 4'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[1],
        linestyle=line_styles[1],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='BE 4')

ax.hist(cdf_data['QoS 1'].values,
        n_bins,
        density=True,
        histtype='step',
        cumulative=True,
        color=colors[2],
        linestyle=line_styles[2],
        linewidth=2,
        # weights=np.ones(len(x_aux.values)) / len(x_aux.values),
        label='QoS 1')

plt.axvline(x=5, linestyle=':', color='r', linewidth=2)
ax.annotate(r'$D^{QoS1}_{QoS}$' + '\n' + '$(93\%)$',
            xy=(5, 0.93),
            xytext=(60000, 0.70),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# tidy up the figure
ax.grid(True)
ax.legend(loc='center left')
ax.set_xscale('log')
# ax.set_title('Cumulative step histograms')
ax.set_xlabel('Queueing Delay (ms)')
ax.set_ylabel('Likelihood (%)')
# plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
plt.yticks(np.arange(0, 1.01, 0.2))
ax.set_xticks([0.01, 0.1, 1, 10, 100, 1000, 10000, 100000])
# ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.tight_layout()
plt.savefig(filename.replace('overall', 'cdf') + '.pdf', format='pdf', bbox_inches='tight')
plt.savefig(filename.replace('overall', 'cdf') + '.png', format='png', bbox_inches='tight')
plt.savefig(filename.replace('overall', 'cdf') + '.eps', format='eps', bbox_inches='tight')
plt.show()
