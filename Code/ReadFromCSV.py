import pandas as pd
import sys
sys.path.append('/Users/houqinhan/TEDDataMining/TEDDataMining/model')
import TEDDataMining.model.VideoModel
import ast


# read data from csv file
df = pd.read_csv('/Users/houqinhan/TEDTalksDataMining/TEDTalksDataMining/Data/ted_main.csv', header=None, sep=',')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 100)

# simple process
lessDf = df.drop([1, 6, 7, 4, 8, 9, 14], axis=1)
lessDf = lessDf.rename(columns={0: 'comments', 2: 'duration', 3: 'event', 5: 'languages', 10: 'ratings', 11: 'related_talks', 12: 'speaker_occupation', 13: 'tags', 15: 'url', 16: 'views'})
finalDf = lessDf.drop(index=[0])
print(finalDf.head(1))

# change data format
finalDf['comments'] = pd.to_numeric(finalDf['comments'], errors='coerce')
finalDf['duration'] = pd.to_numeric(finalDf['duration'], errors='coerce')
finalDf['languages'] = pd.to_numeric(finalDf['languages'], errors='coerce')
finalDf['views'] = pd.to_numeric(finalDf['views'], errors='coerce')

print(type(finalDf['comments']))

# for ele in finalDf['ratings']:
#     ele[0]
# print(finalDf['ratings'][1])
# print(type(finalDf['ratings'][1]))
# finalDf['ratings'] = ast.literal_eval(finalDf['ratings'])
# print(type(finalDf['ratings']))
# def getLabel(labelArray):
#
#     for i in labelArray:
#         if i == "\'":





