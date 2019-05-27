import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 100)

movies = pd.io.parsers.read_csv('/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/ted_main.csv')
tfidf = TfidfVectorizer(max_df=0.8, stop_words='english')
movies['tags'] = movies['tags'].fillna('')
movieList = movies['tags'].tolist()
replaceList = []


for str in movieList:
    get_str = ""
    get_str = str.replace('[', '')
    get_str = get_str.replace(']', '')
    get_str = get_str.replace(' ', '')
    get_str = get_str.replace('\'', '')
    replaceList.append(get_str)


def video_recommendation(input_tag):
    replaceList.append(input_tag)
    tfidf_matrix = tfidf.fit_transform(replaceList)
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    sim_scores = list(enumerate(cosine_sim[-1]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0]for i in sim_scores]
    result = movies['url'].iloc[movie_indices].tolist()
    return result



