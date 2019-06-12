import pandas as pd
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import KMeans
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import SpectralClustering
from sklearn import metrics
import numpy as np
from yellowbrick.cluster import KElbowVisualizer

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 100)

movies = pd.io.parsers.read_csv('/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/ted_main.csv')
modelURL = '/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/model_cluster.pkl'
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

tfidf_matrix = tfidf.fit_transform(replaceList)
km = KMeans(n_clusters=9).fit(tfidf_matrix)
# print(km.labels_.tolist())

pred = SpectralClustering().fit_predict(tfidf_matrix)
print("Calinski-Harabasz Score", metrics.calinski_harabaz_score(tfidf_matrix.toarray(), pred))

# scores=[]
# s=dict()
# for index,gamma in enumerate((0.01,0.1,1,10)):
#     for index,k in enumerate((2, 3, 4, 5, 6, 7, 8)):
#         pred_y=SpectralClustering(n_clusters=k).fit_predict(tfidf_matrix)
#         print("Calinski-Harabasz Score with gamma=",gamma,"n_cluster=",k,"score=",metrics.calinski_harabaz_score(tfidf_matrix.toarray(),pred_y))
#         tmp=dict()
#         tmp['gamma']=gamma
#         tmp['n_cluster']=k
#         tmp['score']=metrics.calinski_harabaz_score(tfidf_matrix.toarray(),pred_y)
#         s[metrics.calinski_harabaz_score(tfidf_matrix.toarray(),pred_y)]=tmp
#         scores.append(metrics.calinski_harabaz_score(tfidf_matrix.toarray(),pred_y))
# print(np.max(scores))
# print("最大得分项：")
# print(s.get(np.max(scores)))

joblib.dump(km, modelURL)

model = KMeans(9)
visualizer = SilhouetteVisualizer(model)

visualizer.fit(tfidf_matrix)
visualizer.poof()


# visualizer_k = KElbowVisualizer(KMeans(), k=(4,15))
# visualizer_k.fit(tfidf_matrix)
# visualizer_k.poof()
