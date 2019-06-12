from sklearn import svm, tree, naive_bayes, neighbors
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib
from Code.load_dataset import load_dataset
import matplotlib.pyplot as plt
import numpy as np
from Code.get_hist import get_hist
from yellowbrick.classifier import ClassPredictionError
from yellowbrick.classifier import ConfusionMatrix

data = load_dataset()

modelURL = '/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/model_cluster.pkl'
km = joblib.load(modelURL)
cluster = km.labels_.tolist()
# print(cluster)

data['cluster'] = cluster

view = data['views'].tolist()
# get_hist(view, 5e4, 2e6, 50)

comment = data['comments'].tolist()
# get_hist(comment, 0, 400, 50)

duration = data['duration'].tolist()
# get_hist(duration, 0, 2000, 20)


def judge_views_level(views):
    if views > 2e6:
        return 1
    elif 1250000 < views <= 2e6:
        return 2
    elif 1000000 < views <= 1250000:
        return 3
    elif 700000 < views <= 1000000:
        return 4
    else:
        return 5


def judge_comment_level(comments):
    if comments > 200:
        return 1
    elif 150 < comments <= 200:
        return 2
    elif 100 < comments <= 150:
        return 3
    elif 50 < comments <= 100:
        return 4
    else:
        return 5


def judge_duration_level(durations):
    if durations > 1000:
        return 1
    elif 800 < durations <= 1000:
        return 2
    elif 700 < durations <= 800:
        return 3
    elif 500 < durations <= 700:
        return 4
    else:
        return 5


data['views_level'] = list(map(lambda x: judge_views_level(x), data['views']))
data['comment_level'] = list(map(lambda x: judge_comment_level(x), data['comments']))
data['duration_level'] = list(map(lambda x: judge_duration_level(x), data['duration']))

# print(data.head(5))

train_data = data
# print(train_data)
test_data = data[-1500:-1000]
# print(test_data)
target = train_data['views_level']
train = train_data[['cluster', 'comment_level', 'duration_level']]
# train = train_data[['views_level', 'duration_level']]

target_test = test_data['views_level']
train_test = test_data[['cluster', 'comment_level', 'duration_level']]
# train_test = test_data[['views_level', 'duration_level']]

clfs = {'svm': svm.SVC(gamma='auto'),
        'decision_tree':tree.DecisionTreeClassifier(),
        'naive_gaussian': naive_bayes.GaussianNB(),
        'naive_mul':naive_bayes.MultinomialNB(),
        'K_neighbor' : neighbors.KNeighborsClassifier(),
        'bagging_knn' : BaggingClassifier(neighbors.KNeighborsClassifier(), max_samples=0.5,max_features=0.5),
        'bagging_tree': BaggingClassifier(tree.DecisionTreeClassifier(), max_samples=0.5,max_features=0.5),
        'random_forest' : RandomForestClassifier(n_estimators=50),
        'adaboost':AdaBoostClassifier(n_estimators=50),
        'gradient_boost' : GradientBoostingClassifier(n_estimators=50, learning_rate=1.0,max_depth=1, random_state=0)
        }

model = RandomForestClassifier(n_estimators=50)


def try_different_method(clf):
    clf.fit(train, target)
    score = clf.score(train_test, target_test)
    print('the score is :', score)


for clf_key in clfs.keys():
    print('the classifier is :', clf_key)
    clf = clfs[clf_key]
    try_different_method(clf)


classes = ["very popular", "popular", "normal", "little comments", "Nobody cares"]
visualizer = ClassPredictionError(
    model, classes=classes
)
visualizer.fit(train, target)
visualizer.score(train_test, target_test)
g = visualizer.poof()

cm = ConfusionMatrix(model, classes=[1,2,3,4,5])
cm.fit(train, target)
cm.score(train_test, target_test)
cm.poof()
