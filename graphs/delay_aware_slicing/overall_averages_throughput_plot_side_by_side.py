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
gomez_means = [1.975758939, 3.985007752, 3.986751672, 6.442928888, 2.007656017]
gomez_stdev = [0.171415301, 0.298013831, 0.337032262, 2.344181848, 0.030178547]

ours_means = [2.07560512, 5.230245371, 5.386185946, 6.194488779, 2.066035894]
ours_stdev = [0.008662744, 0.535378484, 0.613370964, 1.358109561, 0.013715413]

error_config = {'ecolor': '0.3', 'capthick': 4, 'capsize': 4}

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 3.6))
rects1 = ax.bar(x - width/2, gomez_means, width,
                hatch=hatches[0], color='k',
                yerr=gomez_stdev, error_kw=error_config,
                label='Gómez et al. [14]')
rects2 = ax.bar(x + width/2, ours_means, width,
                hatch=hatches[3], yerr=ours_stdev, error_kw=error_config,
                label='Proposed')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Throughput (Mbps)')
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