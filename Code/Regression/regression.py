from sklearn.externals import joblib
import numpy as np

modelURL = '/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/model_regression.pkl'


def regression_predict(duration, language, views, published_date):
    rfr = joblib.load(modelURL)
    array = np.array([duration, language, views, published_date])
    input = array.reshape(1, -1)

    result = rfr.predict(input)[0]
    return int(result)


print(regression_predict(957, 25, 1108371, 1442936421))


