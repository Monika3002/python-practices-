# K Nearest Neighbor method
"""
step for machine learning:
1. data Gathering 
2. Data PreProcessing
3. Choose on algorithm
4. Training
5. Testing
"""
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier ##algo for pre
from sklearn.model_selection  import train_test_split
from sklearn.metrices import accuracy_score  # testing agencies
data= load_iris()
print (data)
print( data([' DESCR'])) 
X =data['DATA']
Y=data['traget']
x_train,x_test,y_train,y_test=train_test_split(X,Y)

print (type(X),X.shape,X,ndim)
knn=KNeighborsClassifier(n_neighbors=15)
knn.fit(X,Y)
print()
predict=knn.predict(x_test)
print(knn.score(x_train,y_train))
print(accuracy_score(y_test_predict))
# pip install openai

