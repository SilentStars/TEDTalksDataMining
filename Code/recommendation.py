import pandas as pd
from numpy import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 100)

movies = pd.io.parsers.read_csv('/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/ted_main.csv')
tfidf = TfidfVectorizer()
movies['tags'] = movies['tags'].fillna('')
tfidf_matrix = tfidf.fit_transform(movies['tags'])
# print(tfidf_matrix)
s = tfidf_matrix.shape
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# print(cosine_sim)
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()


def get_recommendation(title, consine_sim = cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0]for i in sim_scores]
    return movies['title'].iloc[movie_indices]


ans = get_recommendation('Do schools kill creativity?')

print(ans)


# tfidf = TfidfVectorizer()
# movies['description'] = movies['description'].fillna('')
# tfidf_matrix = tfidf.fit_transform(movies['description'])
# s = tfidf_matrix.shape
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()
# ans = get_recommendation('Do schools kill creativity?')
# print(ans)