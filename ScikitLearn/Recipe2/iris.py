import numpy as np
import pydotplus
from  sklearn import tree
from sklearn.datasets import load_iris
from  sklearn.externals.six import StringIO

iris = load_iris()

print(iris)

print("##########")



print(iris["feature_names"])
print(iris["target_names"])
print(iris["data"][0])
print(iris["target"])

test_index=[0,50,100]

# train data

print(iris["data"])
train_target = np.delete(iris["target"],test_index,0)
train_data = np.delete(iris["data"],test_index,0)
print(train_data)


# test_data

test_target = iris["target"][test_index]
test_data = iris["data"][test_index]

print(test_target)
print(test_data)
print(iris.feature_names)
print(iris.target_names)


clf = tree.DecisionTreeClassifier()

clf.fit(train_data,train_target)


print(clf.predict(test_data))


#viz code
dot_date = StringIO()

tree.export_graphviz(clf, out_file=dot_date,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_date.getvalue())
graph.write_png("iris.png")