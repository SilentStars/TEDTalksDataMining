import pandas as pd
from numpy import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn import metrics
import matplotlib.pyplot as plt

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

# num_clusters = 8
# km = KMeans(n_clusters=num_clusters)
# km.fit(tfidf_matrix)
# clusters = km.labels_.tolist()
# print(clusters)
# joblib.dump(km, modelURL)
# print(metrics.silhouette_score(tfidf_matrix, km.labels_, metric='euclidean'))
x = []
y = []

for n in range(15,25):
    x.append(n)
    km = KMeans(n_clusters=n)
    km.fit(tfidf_matrix)
    y.append(metrics.silhouette_score(tfidf_matrix, km.labels_, metric='euclidean'))

plt.figure(figsize=(10, 10))
plt.plot(x,y)
plt.xlabel("n")
plt.ylabel("Silhouette")
plt.show()
# def get_recommendation(title, consine_sim = cosine_sim):
#     idx = indices[title]
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:11]
#     movie_indices = [i[0]for i in sim_scores]
#     return movies['title'].iloc[movie_indices]
#
#
# ans = get_recommendation('Do schools kill creativity?')
#
# print(ans)
