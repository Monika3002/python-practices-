import pandas as pd
from sklearn.linear_model import LinearRegression
data=pd.read_csv("SampleCSVFile_2kb.csv")
print(data)
print(type(data))

X,Y=data["lot_size"].to_numpy().reshape(-1,1),\
    data["prices"].to_numpy().reshape(-1,1)

reg=LinearRegression()
reg.fit(X,Y)

print(reg.predict([[2000],[5000,[46]]]))