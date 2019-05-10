from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

diabetes = datasets.load_diabetes()

print(diabetes.data.shape)

diabetes_X_train = diabetes.data[:-20]
diabetes_X_test = diabetes.data[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)

print(np.mean((regr.predict(diabetes_X_test) - diabetes_y_test)**2))

