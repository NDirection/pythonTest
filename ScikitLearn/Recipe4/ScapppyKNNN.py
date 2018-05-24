import  random
from  scipy.spatial import distance

def euc(a,b):
    return  distance.euclidean(a,b)

class ScappyClassify():
    def __init__(self):
        pass
    def fit(self ,X_train ,Y_train):
        self.X_train = X_train
        self.Y_train = Y_train

    def predict(self,X_test):

        print("################")

        predictions = []

        for row in X_test:
            label = self.cloest(row)
            predictions.append(label)

        return  predictions

    def cloest(self,row):

        best_distane = euc(row,self.X_train[0])
        best_index = 0

        for i in range(1,len(self.X_train)):

            dist = euc(row,self.X_train[i])

            if dist < best_distane :
                best_distane = dist
                best_index = i
        return  self.Y_train[best_index]



