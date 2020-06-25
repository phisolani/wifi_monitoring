# Credit: Josh Hemann

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import seaborn as sns


# Applying Seaborn style
# whitegrid, darkgrid, whitegrid, dark, white, and ticks
sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)
plt.rcParams['mathtext.fontset'] = 'stix'
hatches = ['+', 'x', '.', '*', 'o', '\\', 'O', '-']
colors = ['darkolivegreen', 'darkblue', 'deepskyblue', 'magenta', 'goldenrod']
n_groups = 2

qos1_mean = (89.35267431, 32.08246915)
qos1_std = (14.92014623, 9.392062956)

be1_mean = (339.8431904, 374.2717947)
be1_std = (45.55786637, 35.37021373)

be2_mean = (386.1869306, 428.4269307)
be2_std = (52.37109333, 37.68279283)

be3_mean = (240.2109028, 407.4070388)
be3_std = (92.14260111, 78.79840639)

qos2_mean = (179.6930408, 96.54814037)
qos2_std = (29.79027939, 28.48412061)

fig, ax = plt.subplots(figsize=(10, 3.6))

index = np.arange(n_groups)
bar_width = 0.14

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

# ax.set_ylim(0, 600)
ax.set_yscale('log')
ax.set_yticks([1, 10, 100, 1000, 10000])
ax.set_ylabel('Queueing delay (ms)')

ax.annotate(r'$D^{QoS1}_{QoS}$ (30ms)',
            xy=(0.78, 30),
            xytext=(0.78, 5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='top')

ax.annotate(r'$D^{QoS2}_{QoS}$ (50ms)',
            xy=(0.78, 50),
            xytext=(0.78, 1000),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='top')

plt.axhline(y=50, color='r', linestyle='--', linewidth=2)
plt.axhline(y=30, color='r', linestyle='--', linewidth=2)

ax.set_xticks(index + bar_width * 2)
ax.set_xticklabels(('Gómez et al. [14]', 'Proposed'))

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=5)
ax.grid(True)

fig.tight_layout()

plt.savefig("overall_results_delay.eps", format="eps")
plt.savefig("overall_results_delay.pdf", format="pdf")
plt.savefig("overall_results_delay.png", format="png")

plt.show()