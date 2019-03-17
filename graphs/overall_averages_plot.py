# Credit: Josh Hemann

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import seaborn as sns


# Applying Seaborn style
# whitegrid, darkgrid, whitegrid, dark, white, and ticks
sns.set(style="whitegrid", font_scale=2.8, font='Times New Roman')

n_groups = 3

means_latency = (34.54, 33.35, 15.18)
std_men = (7.09, 9.46, 1.58)

means_throughput = (32.78, 33.53, 31.16)
std_women = (1.51, 2.11, 1.8)

fig, ax = plt.subplots(figsize=(16, 10), dpi=144)
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3', 'capthick': 4, 'capsize': 4}

rects1 = ax.bar(index, means_latency, bar_width,
                alpha=opacity, color='b',
                yerr=std_men, error_kw=error_config,
                label='QoS (Latency)')

rects2 = ax2.bar(index + bar_width, means_throughput, bar_width,
                alpha=opacity, color='y',
                yerr=std_women, error_kw=error_config,
                label='BE (Throughput)')

axis_padding = 0.3  # percentage

ax.set_ylim(0,50)
ax2.set_ylim(0,50)


#ax.set_xlabel('Scenario Configuration')
ax.set_ylabel('Average Latency (ms)')
ax2.set_ylabel('Average Throughput (Mbps)')


ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('Single Slices (A)', 'Static Slices (B)', 'Adaptive Slices (C)'))

ax.legend(bbox_to_anchor=(0.35, 1.00))
ax2.legend()
ax.grid(False)
ax2.grid(False)

fig.tight_layout()

plt.savefig("/Users/phisolani/Github/wifi_monitoring/graphs/overall_results/overall_results.pdf", format="pdf")

plt.show()