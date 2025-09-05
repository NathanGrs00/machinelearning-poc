import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 3, 5, 7, 11])

model = LinearRegression()
model.fit(x, y)

def predict_value(val):
    return model.predict([[val]])[0]