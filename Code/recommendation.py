import pandas as pd
from numpy import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

#movies=pd.io.parsers.read_csv('C:/Users/w/Downloads/movie_metadata.csv')
movies=pd.io.parsers.read_csv('C:/Users/w/a1/ted_main.csv')
tfidf=TfidfVectorizer(stop_words='english')
movies['tags']=movies['tags'].fillna('')
tfidf_matrix=tfidf.fit_transform(movies['tags'])
s = tfidf_matrix.shape
cosine_sim=linear_kernel(tfidf_matrix,tfidf_matrix)
indices=pd.Series(movies.index,index=movies['title']).drop_duplicates()
def get_recommendation(title,consine_sim=cosine_sim):
    idx=indices[title]
    sim_scores=list(enumerate(cosine_sim[idx]))
    sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True)
    sim_scores=sim_scores[1:11]
    movie_indices=[i[0]for i in sim_scores]
    return movies['title'].iloc[movie_indices]
ans = get_recommendation('Do schools kill creativity?')
print(ans)
