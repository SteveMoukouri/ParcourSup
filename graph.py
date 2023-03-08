#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

with open("troisieme.csv",'r') as f:
    with open("troisieme_modified.csv",'w') as f1:
        next(f) # skip header line
        for line in f:
            f1.write(line)
data = np.genfromtxt("troisieme_modified.csv", delimiter=",",dtype=str,usecols=np.arange(3,5),max_rows=5)
names = []
values = []

for i in range(len(data)):
    names.insert(i, data[i][0])
    values.insert(i, data[i][1])

plt.pie(values, labels = [names[0], names[1], names[2], names[3], names[4]], normalize = True)
plt.show()

