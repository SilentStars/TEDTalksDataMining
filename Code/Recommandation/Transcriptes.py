from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity
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

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 100)

transcripts = pd.read_csv("/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/transcripts.csv")
# print(transcripts.head())

# get the title
transcripts['title'] = transcripts['url'].map(lambda x:x.split("/")[-1])
# print(transcripts.head())

Text=transcripts['transcript'].tolist()
tfidf=text.TfidfVectorizer(input=Text,stop_words="english")
matrix=tfidf.fit_transform(Text)
# print(matrix.shape)

model = MiniBatchKMeans(8)
visualizer = SilhouetteVisualizer(model)

visualizer.fit(matrix)
visualizer.poof()

# x = []
# y = []
#
# for n in range(8, 16):
#     x.append(n)
#     km = KMeans(n_clusters=n)
#     km.fit(matrix)
#     y.append(metrics.silhouette_score(matrix, km.labels_, metric='euclidean'))
#     print(n)
#
# plt.figure(figsize=(10, 10))
# plt.plot(x, y)
# plt.xlabel("n")
# plt.ylabel("Silhouette")
# plt.show()

# sim_unigram = cosine_similarity(matrix)
#
#
# def get_similar_articles(x):
#     return ",".join(transcripts['title'].loc[x.argsort()[-5:-1]])
#
#
# transcripts['similar_articles_unigram']=[get_similar_articles(x) for x in sim_unigram]
# print(transcripts.head())