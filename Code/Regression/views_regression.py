from Code.load_dataset import load_dataset
from sklearn import linear_model
import numpy as np
from sklearn.linear_model import Lasso
from yellowbrick.regressor import PredictionError
from sklearn.linear_model import Ridge
from yellowbrick.regressor import ResidualsPlot
from sklearn.metrics import mean_squared_error

regr = linear_model.LinearRegression()

data = load_dataset()

train_data = data[:-500]
test_data = data[-500:]

target = train_data['comments']
train = train_data[['duration', 'published_date', 'views']]

target_test = test_data['comments']
train_test = test_data[['duration', 'published_date', 'views']]

regr.fit(train, target)

lasso = Lasso()
visualizer = PredictionError(lasso)
visualizer.fit(train, target)
visualizer.score(train_test, target_test)
g = visualizer.poof()

ridge = Ridge()
visualizer = ResidualsPlot(ridge)
visualizer.fit(train, target)
visualizer.score(train_test, target_test)
k = visualizer.poof()

print('MSE: ' + str(mean_squared_error(target_test, regr.predict(train_test))))
print('MSE(Calculate MSE according to the formula): ' + str(np.mean((regr.predict(train_test) - target_test)**2)))
print('RMSE:', str(np.sqrt(mean_squared_error(target_test, regr.predict(train_test)))))
