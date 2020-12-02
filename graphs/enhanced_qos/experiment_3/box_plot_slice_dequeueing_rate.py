import pandas as pd
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from itertools import cycle

sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)
fig, ax = plt.subplots(figsize=(5, 4))
plt.rcParams['mathtext.fontset'] = 'stix'

data = pd.read_csv('overall_slice_dequeueing_rate.csv', sep=';')
print('data', data)

def remove_outlier(df):
    low = .01
    high = .99
    quant_df = df.quantile([low, high])
    for name in list(df.columns):
        if is_numeric_dtype(df[name]):
            df = df[(df[name] > quant_df.loc[low, name]) & (df[name] < quant_df.loc[high, name])]
    return df

#new_data = remove_outlier(data)
new_data = data
print('new_data', new_data)

my_pal = {"Gómez et al.": "cadetblue", "Proposed": "sandybrown"}

ax = sns.boxplot(y='throughput',
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

plt.axhline(y=10, color='r', linestyle=':', linewidth=2)

ax.annotate(r'$\mu^{QoS1}_{QoS}$' + '\n' + '$(10Mbps)$',
            xy=(1.6, 10),
            xytext=(1.6, 20.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='top')


# tidy up the figure
ax.grid(True)
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=2)
plt.legend(bbox_to_anchor=(0., 0.85, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
ax.legend_.findobj(mpl.patches.Rectangle)[0].set_hatch("+")
ax.legend_.findobj(mpl.patches.Rectangle)[1].set_hatch("Ox")
# ax.legend_.findobj(mpl.patches.Rectangle)[0].set_edgecolor('white')
# ax.legend_.findobj(mpl.patches.Rectangle)[1].set_edgecolor('white')
ax.set(xlabel=None)
ax.set_yticks([0, 5, 10, 15, 20, 25])
ax.set_ylim(None, 25)
ax.set_ylabel('Throughput (Mbps)')
plt.tight_layout()
plt.savefig("overall_slice_dequeueing_rate_box_plot.eps", format="eps")
plt.savefig("overall_slice_dequeueing_rate_box_plot.pdf", format="pdf")
plt.savefig("overall_slice_dequeueing_rate_box_plot.png", format="png")
plt.show()
