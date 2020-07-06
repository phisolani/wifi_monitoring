import matplotlib.pyplot as plt

# fake data
d0 = [[4.5, 5, 6, 4],[4.5, 5, 6, 4]]
d1 = [[1, 2, 3, 3.3],[1, 2, 3, 3.3]]

# basic plot
bp0 = plt.boxplot(d0, patch_artist=True)
bp1 = plt.boxplot(d1, patch_artist=True)

for box in bp0['boxes']:
    # change outline color
    box.set(color='white', linewidth=0)
    # change fill color
    box.set(facecolor='y')
    # change hatch
    box.set(hatch='*')

for box in bp1['boxes']:
    box.set(color='blue', linewidth=5)
    box.set(facecolor = 'red' )

plt.show()