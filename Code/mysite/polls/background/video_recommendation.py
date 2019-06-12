import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def video_recommendation(input_tag):

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 100)

    movies = pd.io.parsers.read_csv('/Users/zuimeihon/Desktop/TEDTalksDataMining/Code/mysite/polls/background/ted_main.csv')
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



    replaceList.append(input_tag)
    tfidf_matrix = tfidf.fit_transform(replaceList)
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    sim_scores = list(enumerate(cosine_sim[-1]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    a = random.randint(2,10)
    sim_scores = sim_scores[a:a+1]
    movie_indices = [i[0]for i in sim_scores]

    result = movies['url'].iloc[movie_indices].tolist()
    result2 = movies['tags'].iloc[movie_indices].tolist()

    result3 = result2[0].replace("[", "")
    result4 = result3.replace("'", "")
    result5 = result4.replace("]", "")
    result6 = result5.replace(", ", ",")
    result7 = result6.split(',')
    print(result7)
    print("下一个视频的tag<-")
    return result[0], result7 #return7 是一个list

