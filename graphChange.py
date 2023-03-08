#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

with open("delta_place_candidature.csv", 'r') as f:
    with open("delta_place_candidature_modified.csv", 'w') as f1:
        next(f)  # skip header line
        for line in f:
            f1.write(line)
with open("troisieme.csv", 'r') as f:
    with open("troisieme_modified.csv", 'w') as f1:
        next(f)  # skip header line
        for line in f:
            f1.write(line)
data = np.genfromtxt("troisieme_modified.csv", delimiter=",", dtype=str, usecols=np.arange(3, 5), max_rows=5)
names = []
values = []
plt.rc('font', family='Arial')

for i in range(len(data)):
    names.insert(i, data[i][0])
    values.insert(i, data[i][1])

data = np.genfromtxt("delta_place_candidature_modified.csv", delimiter=",", dtype=str, usecols=np.arange(3, 6),
                     max_rows=5)
names = []
values = []
valuesToCompare = []
for i in range(len(data)):
    names.insert(i, data[i][0])
    values.insert(i, data[i][1])
    valuesToCompare.insert(i, data[i][2])
print(names)

for i in range(5):
    values[i] = int(values[i])/1000
    valuesToCompare[i] = int(valuesToCompare[i])/1000
print(values)
print(valuesToCompare)
x = np.arange(len(names))  # the label locations
width = 0.35  # size of bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, values, width, label='Candidats')
rects2 = ax.bar(x + width/2, valuesToCompare, width, label='Places')

ax.set_ylabel('Candidatures')
ax.set_title('Delta entre places et candidatures')
ax.set_xticks(x)
ax.set_xticklabels(names)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
