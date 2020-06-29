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
gomez_means = [72.5155892, 104.3034556, 90.9691716, 122.3811068, 22.6695836]
gomez_stdev = [4.891895451, 36.24370068, 32.55314513, 54.02524397, 8.982744464]

ours_means = [75.6060732, 149.0562872, 133.3701568, 158.1043268, 27.7821612]
ours_stdev = [0.286385811, 21.92071765, 21.97503862, 43.52921085, 1.130479717]

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
ax.set_ylabel('Overall throughput (MBytes)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

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

plt.savefig("overall_results_throughput_side_by_side.eps", format="eps")
plt.savefig("overall_results_throughput_side_by_side.pdf", format="pdf")
plt.savefig("overall_results_throughput_side_by_side.png", format="png")
plt.show()