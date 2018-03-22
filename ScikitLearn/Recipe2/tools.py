import matplotlib.pyplot as plt
import numpy as np

class ScatterGraph:

    def __init__(self,features):
        self.features = features;

    def show(self):

        X =[];
        Y =[];

        for ele in self.features :

            X.append(ele[0]);

            Y.append(ele[1])

        T = np.arctan2(Y, X)  # for color value

        plt.scatter(X, Y, s=75, c=T, alpha=0.5)

        plt.show()










