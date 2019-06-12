from sklearn.externals import joblib
import numpy as np
import time

modelURL = '/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/model_regression.pkl'


def regression_predict(input_min, input_sec, language, views, input_year, input_month, input_day):
    duration = int(input_min) * 60 + int(input_sec)
    r = (int(input_year), int(input_month), int(input_day), 1, 0, 0, 0, 0, 0)
    published_date = time.mktime(r)
    language = int(language)
    views = int(views)
    rfr = joblib.load(modelURL)
    array = np.array([duration, language, views, published_date])
    input = array.reshape(1, -1)

    result = rfr.predict(input)[0]
    return int(result)


print(regression_predict('4', '42', '25', '1108371', '2005', '2', '14'))


