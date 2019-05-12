import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
from scipy import stats
import seaborn as sns
import ast

pd.set_option('display.max_columns', None)
data=pd.read_csv("C:/Users/w/a1/ted_main.csv")
df = data.dropna() #clean
#print(df.isnull().any())

df.columns = ['comments','description','duration','event','film_date','languages','main_speaker','name','num_speaker','published_date','ratings','related_talks','speaker_occupation','tags','title','url','views']
df2 = df
df.drop(['description', 'name', 'speaker_occupation','url','num_speaker', 'ratings','related_talks','speaker_occupation','tags' ],axis= 1,inplace=True)
df = df[['title','main_speaker', 'views','comments','event', 'duration','film_date', 'published_date', 'languages']]
df['film_date'] = df['film_date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
df['published_date'] = df['published_date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))

#################################################################################################基本情况, 平均数
#print(df.head(5))
#print(df.describe())

#################################################################################################播放量分析
#播放量最多的10个节目
a = df.sort_values("views",inplace=False,ascending=False)
a = a[['title', 'main_speaker', 'views', 'comments','published_date']]
#print(a.head(10))

#播放量数据分析
df['views'].describe()

# 播放量box图
sns.boxplot(df['views'])
#plt.show()

#播放量直方图
plt.hist(df.views, range=(0,3000000), bins=100, rwidth=1)
#plt.show()

###############################################################################################评论量分析
#评论量最多的10视频
a = df.sort_values("comments",inplace=False,ascending=False)
a = a[['title', 'main_speaker', 'views', 'comments','published_date']]
#print(a.head(10))

#评论量数据分析
df['views'].describe()

# 评论量box图
sns.boxplot(df['views'])
#plt.show()

#评论量直方图
plt.hist(df.views, range=(0,500), bins=100, rwidth=1)
#plt.show()


#####################################################################################################浏览量与评论量的关系

a = sns.jointplot(x = 'views', y = 'comments', data = df)
#plt.show()

b = df[['views', 'comments']].corr()
#print(b)

#####################################################################################################语言的分析

a = df['languages'].describe()
#print(a)

a = sns.jointplot(x = 'views', y = 'languages', data = df)
#plt.show()

b = df[['views', 'languages']].corr()
#print(b)

#####################################################################################################时长分析

df['duration'] = df['duration']/60
a = df['duration'].describe()
#print(a)

a = sns.jointplot(x = 'views', y = 'duration', data = df)
#plt.show()

b = df[['views', 'duration']].corr()
#print(b)

# 最短的演讲
df[df['duration'] == min(df['duration'])]

####################################################################################################主要演讲者
speaker_df = df.groupby('main_speaker').count().reset_index()[['main_speaker', 'comments']]
speaker_df.columns = ['主要演讲者', '演讲次数']
speaker_df = speaker_df.sort_values('演讲次数', ascending=False)
speaker_df.head(10)
#print(speaker_df.head(10))

 ###################################################################################################ted events
events_df = df[['title', 'event']].groupby('event').count().reset_index()
events_df.columns = ['event', 'talks']
events_df = events_df.sort_values('talks', ascending=False)
s = events_df.head(10)
#print(s)

#################################################################################################### tags 分析
df['tags'] = df['tags'].apply(lambda x: ast.literal_eval(x))
