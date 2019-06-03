import pandas as pd
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import KMeans
from yellowbrick.cluster import SilhouetteVisualizer

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
km = KMeans(n_clusters=8).fit(tfidf_matrix)
print(km.labels_.tolist())

joblib.dump(km, modelURL)

model = MiniBatchKMeans(8)
visualizer = SilhouetteVisualizer(model)

visualizer.fit(tfidf_matrix)
visualizer.poof()
