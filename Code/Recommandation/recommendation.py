import pandas as pd
from numpy import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.cluster import KMeans
from sklearn.externals import joblib

modelURL = '/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/model_cluster.pkl'

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 100)

movies = pd.io.parsers.read_csv('/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/ted_main.csv')
tfidf = TfidfVectorizer(max_df = 0.8, stop_words='english')
movies['tags'] = movies['tags'].fillna('')
movieList = movies['tags'].tolist()
# print(type(movieList))
# print(movieList[-1])
tfidf_matrix = tfidf.fit_transform(movieList)
# # print(tfidf_matrix)
# s = tfidf_matrix.shape
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# print(cosine_sim)
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()


# def get_recommendation(title, consine_sim = cosine_sim):
#     idx = indices[title]
#     print(idx)
#     print(enumerate(cosine_sim[idx]))
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     print(sim_scores)
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:11]
#     movie_indices = [i[0]for i in sim_scores]
#     return movies['title'].iloc[movie_indices]
#
#
# ans = get_recommendation('Do schools kill creativity?')
# print(ans)

tag = "['computer', 'France', 'program']"
# movieList.append(tag)
# print(movieList[-1])
# tfidf_matrix = tfidf.fit_transform(movieList)
# s = tfidf_matrix.shape
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# print(cosine_sim)
# indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()
# ans = get_recommendation('Do schools kill creativity?')
# print(ans)


def video_recommendation(input_tag):
    movieList.append(tag)
    tfidf_matrix_ = tfidf.fit_transform(movieList)
    s = tfidf_matrix_.shape
    cosine_sim_ = linear_kernel(tfidf_matrix, tfidf_matrix)
    sim_scores = list(enumerate(cosine_sim_[-1]))
    print(sim_scores)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0]for i in sim_scores]
    return movies['url'].iloc[movie_indices]


print(video_recommendation(tag))
