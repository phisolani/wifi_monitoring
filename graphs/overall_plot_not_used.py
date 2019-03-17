import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO

import seaborn as sns
sns.set(style="whitegrid", font_scale=2, font='Times New Roman')


s = StringIO("""     latency_avg     latency_stdev     throughput_avg   throughput_stdev
A     15     5   10     4
B     30     5   10     3
C     20     5   20     1
""")

df = pd.read_csv(s, index_col=0, delimiter=' ', skipinitialspace=True)

fig = plt.figure() # Create matplotlib figure

ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

width = 0.3

df.latency_avg.plot(kind='bar', yerr=df.latency_stdev, color='red', ax=ax, width=width, position=1)
df.throughput_avg.plot(kind='bar', yerr=df.throughput_stdev, color='blue', ax=ax2, width=width, position=0)

ax.set_ylabel('Average Latency (ms)')
ax2.set_ylabel('Average Throughput (Mbps)')

plt.show()