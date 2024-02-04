import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns
df = pd.read_csv('files/heart.csv', sep = ',')
df['Cholesterol'] = np.where(df['Cholesterol']==0, np.nan, df['Cholesterol'])
df['RestingBP'] = np.where(df['RestingBP']==0, np.nan, df['RestingBP'])
df['FastingBS'] = np.where(df['FastingBS']==0, np.nan, df['FastingBS'])

fig = plt.figure(figsize= (14,5))
sns.countplot(x =  df['ChestPainType'])
#pandas bar = seaborn countplot
#с seaborn нет в агрегации с помощью value_counts
plt.show()

fig = plt.figure(figsize= (20,10))
ax1 = fig.add_subplot(221)
sns.kdeplot(df.Age.dropna())
#В статистике - оценка плотности ядра - один из вариантов сглаживания
# метод .kdeplot() позволяет делать сглаживание по распределению
ax2 = fig.add_subplot(222)
df['Age'].value_counts().sort_index().plot.line()
plt.show()


# с помощью .kdeplot() можно делать концентрические визуализации
fig = plt.figure(figsize= (14,5))
sns.kdeplot(x = 'Age', y = 'Cholesterol', data = df, color='r',shade=True)
plt.show()

fig = plt.figure(figsize= (14,5))
sns.kdeplot(x = 'Age', y = 'Cholesterol', data = df, color='r',shade=False)
plt.show()

#Аналог гистограммы .histplot()
fig = plt.figure(figsize= (14,5))
sns.histplot(df['Age'],kde = True) # kde - параметр сглаживания
plt.show()

#Аналог scatterplot .joinplot()
sns.jointplot(x='Age', y='Cholesterol', data=df, kind = 'hex',gridsize=20)
plt.show()

# .boxplot() - ящики с усами
plt.figure(figsize=(20,12))
sns.boxplot(y="Age", x="Cholesterol", data=df[df.Age.isin(np.arange(20,40,1))], orient="h")
plt.show()

# .violinplot() - склейка
fig = plt.figure(figsize= (14,5))
sns.violinplot(y="MaxHR", x="Sex",hue = 'HeartDisease', split = True, data=df)
plt.show()

fig = plt.figure(figsize= (14,5))
sns.violinplot(y="MaxHR", x="Sex",hue = 'HeartDisease', split = False, data=df) # части violin будут отдельными
plt.show()

# большая таблица графиков
cols = ['Oldpeak', 'MaxHR',  'Cholesterol', 'RestingBP', 'Age']
sns_plot = sns.pairplot(df[cols])
plt.show()

#Корреляция признаков
print(df[cols].dropna().corr())

#Тепловая карта .heatmap()
fig = plt.figure(figsize= (14,5))
sns.heatmap(df[cols].dropna().corr(), cmap = 'Blues')
plt.show()