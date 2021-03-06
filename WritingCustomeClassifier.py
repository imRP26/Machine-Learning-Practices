# Here we will write a Custome Classifier, so Comment the importing Statement of KNeighborCalssifier.
# Create fn euc() to get euclidean distance.
from scipy.spatial import distance
def euc(a,b):
	return distance.euclidean(a,b)
# Create Class ScrapKNN() with fn's : fit,predict and closest
class ScrapKNN():
	def fit(self,X_train,y_train):
		self.X_train=X_train
		self.y_train=y_train

	def predict(self,X_test):
		predictions=[]
		for row in X_test:
			label=self.closest(row)
			predictions.append(label)
		return predictions
	
	def closest(self,row):
		best_dist = euc(row,self.X_train[0])
		best_index = 0
		for i in range(1,len(self.X_train)):
			dist=euc(row,self.X_train[i])
			if dist<best_dist:
				best_dist=dist
				best_index=i
		return self.y_train[best_index]

from sklearn import datasets
iris = datasets.load_iris()
X= iris.data
y= iris.target
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size= .5)
# from sklearn.neighbors import KNeighborsClassifier
my_classifier_KNeighbor = ScrapKNN()
my_classifier_KNeighbor.fit(X_train,y_train)
predictions_Kneighbor = my_classifier_KNeighbor.predict(X_test)
from sklearn.metrics import accuracy_score
print("Accuracy using KNeighbour Custom Classifier : ")
print(accuracy_score(y_test,predictions_Kneighbor))
# Output:
# Accuracy using KNeighbourClassifier : 
# 0.9733333333333334