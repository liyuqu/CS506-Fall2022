from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
import random
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
class KNN:

    def __init__(self, k, X_train, y_train):
        self.k = k
        self.X_train = X_train
        self.y_train = y_train
        self.distance_matrix = None
    
    def most_common(lst):
        return max(set(lst), key=lst.count)

    def train(self):
        a,b=self.shape
        c=[[0]*b]*a
        self.distance_matrix = np.norm(self-c)

    def predict(self, example):
        neighbors=[]
        for x in example:
            distances = self.train(x, self.X_train)
            y_sorted = [y for _, y in sorted(zip(distances, self.y_train))]
            neighbors.append(y_sorted[:self.k])
        return list(map(self.most_common, neighbors))

    def get_error(self, predicted, actual):
        return sum(map(lambda x : 1 if (x[0] != x[1]) else 0, zip(predicted, actual))) / len(predicted)

    def test(self, test_input, labels):
        actual = labels
        predicted = (self.predict(test_input))
        print("error = ", self.get_error(predicted, actual))

# Add the dataset here
iris = datasets.load_iris()
data=iris['data']
target=iris['target']
# Split the data 70:30 and predict.
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3)
# create a new object of class KNN
ss = StandardScaler().fit(X_train)
X_train, X_test = ss.transform(X_train), ss.transform(X_test)
# plot a boxplot that is grouped by Species. 
plt.boxplot(iris['target'])
# You may have to ignore the ID column

# predict the labels using KNN
pred=KNN.predict(X_test, X_train)
# use the test function to compute the error
KNN.test(pred, iris['target'])