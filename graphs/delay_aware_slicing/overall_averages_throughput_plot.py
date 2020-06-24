# Credit: Josh Hemann

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import seaborn as sns


# Applying Seaborn style
# whitegrid, darkgrid, whitegrid, dark, white, and ticks
sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)

hatches = ['+', 'x', '.', '*', 'o', '\\', 'O', '-']
colors = ['darkolivegreen', 'darkblue', 'deepskyblue', 'magenta', 'goldenrod']
n_groups = 2

qos1_mean = (0, 2.074)
qos1_std = (0, 0.00843274)

be1_mean = (0, 5.511)
be1_std = (0, 0.563115342)

be2_mean = (0, 5.706)
be2_std = (0, 0.657287355)

be3_mean = (0, 6.614)
be3_std = (0, 1.391156194)

qos2_mean = (0, 2.067)
qos2_std = (0, 0.016363917)

means_throughput = (6.78, 6.53)
std_throughput = (1.51, 2.11)

fig, ax = plt.subplots(figsize=(10, 3.6))

index = np.arange(n_groups)
bar_width = 0.15

opacity = 0.6
error_config = {'ecolor': '0.3', 'capthick': 4, 'capsize': 4}

rects1 = ax.bar(index, qos1_mean, bar_width,
                alpha=opacity, color=colors[0], hatch=hatches[0],
                yerr=qos1_std, error_kw=error_config,
                label='QoS 1')

ax.bar(index + bar_width, be1_mean, bar_width,
                alpha=opacity, color=colors[1], hatch=hatches[1],
                yerr=be1_std, error_kw=error_config,
                label='BE 1')

ax.bar(index + (2*bar_width), be2_mean, bar_width,
                alpha=opacity, color=colors[2], hatch=hatches[2],
                yerr=be2_std, error_kw=error_config,
                label='BE 2')

ax.bar(index + (3*bar_width), be3_mean, bar_width,
                alpha=opacity, color=colors[3], hatch=hatches[3],
                yerr=be3_std, error_kw=error_config,
                label='BE 3')

ax.bar(index + (4*bar_width), qos2_mean, bar_width,
                alpha=opacity, color=colors[4], hatch=hatches[4],
                yerr=qos2_std, error_kw=error_config,
                label='QoS 2')

axis_padding = 0.3  # percentage

ax.set_ylim(0, 10)

ax.set_ylabel('Throughput (Mbps)')


ax.set_xticks(index + bar_width * 2)
print(index + bar_width / 2)
ax.set_xticklabels(('Gómez et al. [14]', 'Proposed'))

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=5)
ax.grid(True)

fig.tight_layout()

plt.savefig("overall_results_throughput.eps", format="eps")
plt.savefig("overall_results_throughput.pdf", format="pdf")
plt.savefig("overall_results_throughput.png", format="png")

plt.show()