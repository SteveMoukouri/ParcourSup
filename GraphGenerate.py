import numpy as np
import matplotlib.pyplot as plt


class GraphGenerate:
    def __init__(self, file, range_x, range_y):
        self.file = file
        self.__format_file_header()
        self.data = np.genfromtxt(file + "_modified.csv", delimiter=";", dtype=str, usecols=np.arange(range_x, range_y),
                                  max_rows=5)

    def __format_file_header(self):
        with open(self.file + ".csv", 'r') as f:
            with open(self.file + "_modified.csv", 'w') as f1:
                next(f)  # skip header line
                for line in f:
                    f1.write(line)

    def generate_pie_chart(self,title):
        names = []
        values = []

        for i in range(len(self.data)):
            names.insert(i, self.data[i][0])
            values.insert(i, self.data[i][1])
        plt.title(title)
        plt.pie(values, labels=[names[0], names[1], names[2], names[3], names[4]], normalize=True)
        plt.show()

    def generate_hist_chart(self, labels):
        names = []
        values = []
        valuesToCompare = []
        for i in range(len(self.data)):
            names.insert(i, self.data[i][0])
            values.insert(i, self.data[i][1])
            valuesToCompare.insert(i, self.data[i][2])
        print(names)

        for i in range(5):
            values[i] = int(values[i]) / 1000
            valuesToCompare[i] = int(valuesToCompare[i]) / 1000
        print(values)
        print(valuesToCompare)
        x = np.arange(len(names))  # the label locations
        width = 0.35  # size of bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, values, width, label=labels[0])
        rects2 = ax.bar(x + width / 2, valuesToCompare, width, label=labels[1])

        ax.set_ylabel(labels[2])
        ax.set_title(labels[3])
        ax.set_xticks(x)
        ax.set_xticklabels(names)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()

        plt.show()


print("file and graph wanted :")
file, graph_type = map(str,input().split())
if graph_type == 'chart' :
    graph = GraphGenerate(file, 3, 5)
    graph.generate_pie_chart()
if graph_type == 'hist':
    graph = GraphGenerate(file, 3, 6)
    graph.generate_hist_chart(["label","label1","label2","label3","label4","label5","label6"])
else:
    print("type is wrong")