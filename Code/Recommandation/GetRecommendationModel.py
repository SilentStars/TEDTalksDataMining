import pandas as pd
from numpy import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.cluster import  MiniBatchKMeans
from yellowbrick.cluster import SilhouetteVisualizer

modelURL = '/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/model_cluster.pkl'

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 100)

movies = pd.io.parsers.read_csv('/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/ted_main.csv')
tfidf = TfidfVectorizer(max_df = 0.8, stop_words='english')
movies['tags'] = movies['tags'].fillna('')
tfidf_matrix = tfidf.fit_transform(movies['tags'])

print(tfidf.get_feature_names())
s = tfidf_matrix.shape
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

print(tfidf_matrix)

# 折线图
# x = []
# y = []
# for n in range(15,25):
#     x.append(n)
#     km = KMeans(n_clusters=n)
#     km.fit(tfidf_matrix)
#     y.append(metrics.silhouette_score(tfidf_matrix, km.labels_, metric='euclidean'))
#
# plt.figure(figsize=(10, 10))
# plt.plot(x,y)
# plt.xlabel("n")
# plt.ylabel("Silhouette")
# plt.show()


model = MiniBatchKMeans(8)
visualizer = SilhouetteVisualizer(model)

visualizer.fit(tfidf_matrix)
visualizer.poof()
