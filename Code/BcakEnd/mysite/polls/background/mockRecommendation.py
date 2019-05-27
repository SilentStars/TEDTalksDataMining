import pandas as pd
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import ast
import numpy as np

pd.set_option('display.max_columns', None)
data=pd.read_csv("ted_main.csv")
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
print(df.head(5))
print(df.describe())