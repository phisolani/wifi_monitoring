import pandas as pd
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from itertools import cycle

sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)
fig, ax = plt.subplots(figsize=(10, 3.6))
plt.rcParams['mathtext.fontset'] = 'stix'

data = pd.read_csv('averages_queueing_delay.csv', sep=';')
print('data', data)

def remove_outlier(df):
    low = .01
    high = .99
    quant_df = df.quantile([low, high])
    for name in list(df.columns):
        if is_numeric_dtype(df[name]):
            df = df[(df[name] > quant_df.loc[low, name]) & (df[name] < quant_df.loc[high, name])]
    return df

new_data = remove_outlier(data)
print('new_data', new_data)

my_pal = {"Gómez et al.": "lightslategray", "Proposed": "y"}

ax = sns.boxplot(y='queueing delay',
                 x='slice',
                 data=new_data,
                 palette=my_pal,
                 hue='approach',
                 linewidth=2,
                 notch=True)

# Select which box you want to change
# for artist in ax.artists:
    # Change the appearance of that box
    # mybox.set_facecolor('white')
    # artist.set_edgecolor('white')
    # artist.set_linewidth(2)

hatches = cycle(['+', 'Ox'])
for i, patch in enumerate(ax.artists):
    # Boxes from left to right
    hatch = next(hatches)
    patch.set_hatch(hatch)

plt.axhline(y=50, color='r', linestyle=':', linewidth=2)
plt.axhline(y=30, color='r', linestyle=':', linewidth=2)

ax.annotate(r'$D^{QoS1}_{QoS} (30ms)$',
            xy=(2.5, 30),
            xytext=(2.5, 18),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='top')

ax.annotate(r'$D^{QoS2}_{QoS} (50ms)$',
            xy=(2.5, 50),
            xytext=(2.5, 178),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='top')

# tidy up the figure
ax.grid(True)
ax.legend(loc='upper left', ncol=1)
ax.legend_.findobj(mpl.patches.Rectangle)[0].set_hatch("+")
ax.legend_.findobj(mpl.patches.Rectangle)[1].set_hatch("Ox")
# ax.legend_.findobj(mpl.patches.Rectangle)[0].set_edgecolor('white')
# ax.legend_.findobj(mpl.patches.Rectangle)[1].set_edgecolor('white')
ax.set(xlabel=None)
ax.set_ylabel('Queueing Delay (ms)')
ax.set_yscale('log')
ax.set_yticks([10, 100, 1000, 1500])
plt.tight_layout()
plt.savefig("overall_results_queueing_delay_box_plot.eps", format="eps")
plt.savefig("overall_results_queueing_delay_box_plot.pdf", format="pdf")
plt.savefig("overall_results_queueing_delay_box_plot.png", format="png")
plt.show()
