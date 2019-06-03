from Code.load_dataset import load_dataset
from sklearn import linear_model
import numpy as np
from sklearn.linear_model import Lasso
from yellowbrick.regressor import PredictionError
from sklearn.linear_model import Ridge
from yellowbrick.regressor import ResidualsPlot
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import heapq
import matplotlib.pyplot as plt

regr = linear_model.LinearRegression()

data = load_dataset()
comment = data['comments'].tolist()

# n = 20
# max_index_list = map(comment.index, heapq.nlargest(n, comment))
# listMAX = list(max_index_list)
# print(listMAX)
# listMAX.sort(reverse=True)
# print(listMAX)
# min_index_list = map(comment.index, heapq.nsmallest(n, comment))
# listMIN = list(min_index_list)
#
# for item in range(n):
#     print(comment[listMAX[item]])
#     comment.remove(comment[listMAX[item]])
#     # comment.remove(comment[listMIN[item]])
#     data = data[~data.comments.isin([comment[listMAX[item]]])]
#     # data = data[-data.comments.isin([comment[listMIN[item]]])]


average = np.mean(comment)
print('\n' + 'Average: ' + str(average))
max = np.max(comment)
print('Maximum: ' + str(max))
min = np.min(comment)
print('Minimum: ' + str(min) + '\n')

plt.hist(comment, range=(1000,8000), bins=50, rwidth=1)
plt.show()

train_data = data[:-500]
test_data = data[-500:]

target = train_data['comments']
train = train_data[['duration', 'published_date', 'views']]
# train = train_data[['views']]

target_test = test_data['comments']
train_test = test_data[['duration', 'published_date', 'views']]
# train_test = test_data[['views']]

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


rfr = RandomForestRegressor(max_features=3, random_state=0, n_estimators=100)
rfr.fit(train, target)
print("\n")
print('MSE: ' + str(mean_squared_error(target_test, rfr.predict(train_test))))
print('MSE(Calculate MSE according to the formula): ' + str(np.mean((rfr.predict(train_test) - target_test)**2)))
print('RMSE:', str(np.sqrt(mean_squared_error(target_test, rfr.predict(train_test)))))
