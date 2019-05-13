import pandas as pd
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import ast
import numpy as np

pd.set_option('display.max_columns', None)
data=pd.read_csv("C:/Users/w/a1/ted_main.csv")
df = data.dropna() #clean
#print(df.isnull().any())

df.columns = ['comments','description','duration','event','film_date','languages','main_speaker','name','num_speaker','published_date','ratings','related_talks','speaker_occupation','tags','title','url','views']
df2 = df.copy()
df.drop(['description', 'name', 'speaker_occupation','url','num_speaker', 'ratings','related_talks','speaker_occupation','tags' ],axis= 1,inplace=True)
df = df[['title','main_speaker', 'views','comments','event', 'duration','film_date', 'published_date', 'languages']]
df['film_date'] = df['film_date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
df['published_date'] = df['published_date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))

#################################################################################################基本情况, 平均数
print("基本情况")
print(df.describe())
corr = df.corr()
sns.set(style="white")
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
#################################################################################################播放量分析
#播放量最多的10个节目
a = df.sort_values("views",inplace=False,ascending=False)
a = a[['title', 'main_speaker', 'views', 'comments','published_date']]
print("Most viewed videos")
#播放量数据分析
print(df['views'].describe())

# 播放量box图
sns.boxplot(df['views'])
#plt.show()

#播放量直方图
plt.hist(df.views, range=(0,3000000), bins=100, rwidth=1)
plt.xlabel(u"views")# plots an axis lable
plt.ylabel(u"number")
plt.title(u"View histogram")
#plt.show()

###############################################################################################评论量分析
#评论量最多的10视频
a = df.sort_values("comments",inplace=False,ascending=False)
a = a[['title', 'main_speaker', 'views', 'comments','published_date']]
print("Most commented videos")
print(a.head(10))

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
plt.title("relationship between views and comments")
#plt.show()

b = df[['views', 'comments']].corr()
print("correlation between views and comments")
print(b)

#####################################################################################################语言的分析

a = df['languages'].describe()
print("language discrible")
print(a)

a = sns.jointplot(x = 'views', y = 'languages', data = df)
#plt.show()

b = df[['views', 'languages']].corr()
print("correlation between views and languages")
print(b)

#####################################################################################################时长分析

df['duration'] = df['duration']/60
a = df['duration'].describe()
print("duration describe")
print(a)

a = sns.jointplot(x = 'views', y = 'duration', data = df)
#plt.show()

b = df[['views', 'duration']].corr()
print("correlation between views and duration")
print(b)

# 最短的演讲
df[df['duration'] == min(df['duration'])]

####################################################################################################主要演讲者
speaker_df = df.groupby('main_speaker').count().reset_index()[['main_speaker', 'comments']]
speaker_df.columns = ['主要演讲者', '演讲次数']
speaker_df = speaker_df.sort_values('演讲次数', ascending=False)
showdata = speaker_df.head(10)
print("speakers who publised most videos")
print(speaker_df.head(10))

 ###################################################################################################ted events
events_df = df[['title', 'event']].groupby('event').count().reset_index()
events_df.columns = ['event', 'talks']
events_df = events_df.sort_values('talks', ascending=False)
s = events_df.head(10)
print("ted events describtion")
print(s)

#################################################################################################### tags 分析
# 将字符串型的list转变成list
df2['tags'] = df2['tags'].apply(lambda x: ast.literal_eval(x))
# 将每个视频的标签拆开
s = df2.apply(lambda x: pd.Series(x['tags']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'theme'
# 将拆分好的标签加回原数据集
theme_df = df2.drop('tags', axis = 1).join(s)
print("标签数量：{}".format(len(theme_df['theme'].value_counts())))
#most popular tags
pop_themes = pd.DataFrame(theme_df['theme'].value_counts()).reset_index()
pop_themes.columns = ['theme', 'talks']
print("most popular themes")
print(pop_themes.head(10))

#pie diagram
labels = pop_themes.head(10)['theme']
sizes = pop_themes.head(10)['talks']
explode = (0.1, 0, 0, 0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("most popular themes")
plt.show()
#######################################################################################################