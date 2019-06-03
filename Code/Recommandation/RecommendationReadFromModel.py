from __future__ import print_function
import pandas as pd
from sklearn.externals import joblib
import ast
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 100)

modelURL = '/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/model_cluster.pkl'
TEDTalks = pd.io.parsers.read_csv('/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/ted_main.csv')

km = joblib.load(modelURL)
clusters = km.labels_.tolist()

# print(clusters)
title_list = TEDTalks['title'].to_list()
view_list = TEDTalks['views'].to_list()
comment_list = TEDTalks['comments'].to_list()
TEDTalks['tags'] = TEDTalks['tags'].apply(lambda x: ast.literal_eval(x))
tags_list = TEDTalks['tags'].to_list()
# print(TEDTalks['tags'])

videos = {'title': title_list, 'views': view_list, 'comments': comment_list, 'tags': tags_list, 'cluster': clusters}
frame = pd.DataFrame(videos, index=[clusters], columns=['title', 'views', 'comments', 'tags', 'cluster'])
print(frame['cluster'].value_counts())
# print(frame)

# fig = plt.figure(1, figsize=(20, 20))
# colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
# label_com = ['1', '2', '3', '4', '5', '6', '7', '8']
# ax1 = fig.add_subplot(111)
# for index in range

# X = frame[['views', 'comments']]
# plt.scatter(x = X.iloc[:,0], y = X.iloc[:,1], c = km.labels_, s=50, cmap='rainbow')
# plt.xlabel('views')
# plt.ylabel('comments')
# plt.axis([0, 3e6, 0, 300])
# plt.show()



# for i in range(num_clusters):
#     print("Cluster %d words:" % i, end='')
#
#     for ind in order_centroids[i, :6]:
#         print(" %s" % )
#     print()
#
#     print("Cluster %d titles:" % i, end='')
#     for title in frame.loc[i]['title'].values.tolist():
#         print(' %s,' % title, end='')
#     print()

