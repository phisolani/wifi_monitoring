# Credit: Josh Hemann

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Applying Seaborn style
# whitegrid, darkgrid, whitegrid, dark, white, and ticks
sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)
plt.rcParams['mathtext.fontset'] = 'stix'
hatches = ['+', 'x', '.', '*', 'o', '\\', 'O', '-']
colors = ['darkolivegreen', 'darkblue', 'deepskyblue', 'magenta', 'goldenrod']

labels = ['QoS 1', 'BE 1', 'BE 2', 'BE 3', 'QoS 2']
gomez_means = [89.35267431, 339.8431904, 386.1869306, 240.2109028, 179.6930408]
gomez_stdev = [14.92014623, 45.55786637, 52.37109333, 92.14260111, 29.79027939]

ours_means = [32.08246915, 374.2717947, 428.4269307, 407.4070388, 96.54814037]
ours_stdev = [9.392062956, 35.37021373, 37.68279283, 78.79840639, 28.48412061]

error_config = {'ecolor': '0.3', 'capthick': 4, 'capsize': 4}

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 3.6))
rects1 = ax.bar(x - width/2, gomez_means, width,
                hatch=hatches[0], color='lightslategray',
                yerr=gomez_stdev, error_kw=error_config,
                label='Gómez et al. [14]')
rects2 = ax.bar(x + width/2, ours_means, width,
                hatch=hatches[3], color='y',
                yerr=ours_stdev, error_kw=error_config,
                label='Proposed')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Queueing delay (ms)')
ax.set_yscale('log')
ax.set_yticks([1, 10, 100, 1000, 10000])
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.annotate(r'$D^{QoS1}_{QoS}$ (30ms)',
            xy=(0, 30),
            xytext=(0, 2500),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='top')

ax.annotate(r'$D^{QoS2}_{QoS}$ (50ms)',
            xy=(4, 50),
            xytext=(4, 2500),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='top')

plt.axhline(y=50, color='r', linestyle='--', linewidth=2)
plt.axhline(y=30, color='r', linestyle='--', linewidth=2)

# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')

# autolabel(rects1)
# autolabel(rects2)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=2)
ax.grid(True)
fig.tight_layout()

plt.savefig("overall_results_delay_side_by_side.eps", format="eps")
plt.savefig("overall_results_delay_side_by_side.pdf", format="pdf")
plt.savefig("overall_results_delay_side_by_side.png", format="png")
plt.show()