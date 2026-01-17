from sklearn.linear_model import LinearRegression
import pandas as pd



data = pd.read_csv("DATA.csv")

# 1. Data (examples)
X = data[["hours"]]
y = data["grade"]

model = LinearRegression()
model.fit(X, y)
prediction = model.predict(pd.DataFrame({"hours": [7]}))
if prediction > 100 :
    x = prediction-100
    prediction = prediction-x
print("I think that if X is 7, y will be " , prediction )