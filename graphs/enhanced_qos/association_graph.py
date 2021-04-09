#!/usr/bin/env python
__author__ = "Daniel Kulenkamp"
__copyright__ = "Copyright 2020, The SDN WiFi MAC Manager"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Kulenkamp"
__email__ = "dkulenka@asu.edu"
__status__ = "Prototype"

" Python script creating the user association graph from csv association data"

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import pandas as pd


def make_association_graph(experiment_path, filenames):
    sns.set(style="whitegrid", font='Times New Roman', palette='deep', font_scale=1.5, color_codes=True, rc=None)
    
    data, y_values = get_data(experiment_path, filenames)

    # Sensors
    # fig, ax = plt.subplots(figsize=(7, 5), dpi=144)
    # Thesis
    fig, ax = plt.subplots(figsize=(5.5, 5), dpi=144)

    plt.tight_layout()

    # colors = ["#001B2E", "#294C60", "#ADBC64"]
    colors = ['#CAE7B9', '#F3DE8A', '#EB9486']
    # colors = ['#00BBCC', '#F96E46', '#F9C846']
    # colors = ['#00BBCC', '#F96E46', '#78DB57']
    # colors = ['brown', 'orange', 'olive']
    colors = ['darkcyan', 'steelblue', 'slategray']

    # hatches = ['\\', '.', '/']
    hatches = ['', '.', '/']

    legend_labels = [name[:4].upper().replace('_', ' ') for name in filenames]
    xmin = 0
    xmax = min([len(x) for x in data])
    ymin = 0
    ymax = len(y_values) + 1

    ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
    y_axis = np.arange(0.5, len(y_values), 1)

    plt.yticks(y_axis, y_values)

    handles = []

    for color, hatch, label in zip(colors, hatches, legend_labels):
        handles.append(mpatches.Patch(facecolor=color, label=label, hatch=hatch, edgecolor='w'))

    ax.legend(handles=handles, loc='upper center', ncol=3)

    xcoords = [10, 70, 130, 190]
    for xc in xcoords:
        plt.axvline(x=xc, linestyle=':', color='r', linewidth=2)

    for i in range(len(data)):
        current = None #(current wtp, value first seen)
        for j in range(len(data[i])):
            if current is None:
                current = (data[i][j], j)
            elif data[i][j] != current[0]:
                ax.fill_between([current[1], j+1], i, i+1, color=colors[data[i][j-1]], hatch=hatches[data[i][j-1]], edgecolor='w', linewidth=2)
                current = (data[i][j], j)
            elif j == (len(data[i]) - 1):
                ax.fill_between([current[1], j+1], i, i+1, color=colors[data[i][j]], hatch=hatches[data[i][j]], edgecolor='w', linewidth=2)

    for i in range(len(data)+1):
        ax.axhline(y=i, color='w', linewidth=2)

    ax.set_xlabel('Time (sec)')
    ax.set_xticks([0, 100, 200, 300, 400, 500, 600])

    filename = 'association'
    plt.savefig(str(experiment_path) + str(filename) + '.pdf', format="pdf", bbox_inches="tight")
    plt.savefig(str(experiment_path) + str(filename) + '.png', format="png", bbox_inches="tight")
    plt.savefig(str(experiment_path) + str(filename) + '.eps', format="eps", bbox_inches="tight")

    plt.show()
    print('Done!')

  
def get_data(directory, filenames):

    raw_data_dicts = []
    stations = []

    for f in filenames:
        d = {}
        path = directory + f + '.csv'
        df = pd.read_csv(path, ';', header=0)
        for header_val in df.columns.values:
            if 'STA' in header_val:
                d[header_val] = []
                if header_val not in stations:
                    stations.append(header_val)

        for index, row in df.iterrows():
            for key, _ in d.items():
                d[key].append(row[key])

        raw_data_dicts.append(d)

    final_data = []

    for sta in stations:
        vals = []
        # check for each second of the exp
        for second in range(len(df)):
            # for each wtp, check if the sta is connected
            for i in range(len(raw_data_dicts)):
                if raw_data_dicts[i][sta][second] == 1:
                    vals.append(i)
                    break

        temp = {sta: vals}
        final_data.append(temp)

    labels = []
    final = []
    for d in final_data:
        for key, value in d.items():
            labels.append(key)
            final.append(value)

    return final, labels
