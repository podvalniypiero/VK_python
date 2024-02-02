import pandas as pd
import numpy as np
# %matplotlib inline
import matplotlib.pyplot as plt

# DataSet https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction
df = pd.read_csv('files/heart.csv', sep = ',')
print(df.head(2))
print(df.info())
print(df.describe())
print(df.columns)

# Реализация функции plot в pandas основана на библиотеке matplotlib.
df['Cholesterol'] = np.where(df['Cholesterol']==0, np.nan, df['Cholesterol'])
df['RestingBP'] = np.where(df['RestingBP']==0, np.nan, df['RestingBP'])
df['FastingBS'] = np.where(df['FastingBS']==0, np.nan, df['FastingBS'])

# ОДНОМЕРНЫЕ данные - plot.bar(), plot.line(), plot.area(), plot.hist()
fig = plt.figure(figsize= (14,5))
df['ChestPainType'].value_counts().plot.bar()
#Bar Chart (столбчатая диаграмма) - классический интсрумент для отображения информации по категориям
plt.show()

fig = plt.figure(figsize= (14,5))
df['ChestPainType'].value_counts().sort_index().plot.bar() #.sort_index() просортирует от A до Z стобцы диаграммы
plt.show()

#Можно посмотреть относительные наблюдения
fig = plt.figure(figsize= (14,5))
(df['ChestPainType'].value_counts() / len(df)).plot.bar()
plt.show()

# groupby позволяет группировать данные по одному или нескольким столбцам и вычислять различные статистики для каждой группы
print(df.groupby(['HeartDisease'])[['Age', 'Cholesterol']].mean())

# stacked - параметр - будут столбцы совмещенные или нет
df.groupby(['HeartDisease'])[['Age','Cholesterol']].mean().plot.bar(figsize=(14,5),stacked = False)
plt.show()

df.groupby(['HeartDisease'])[['Age','Cholesterol']].mean().plot.bar(figsize=(14,5),stacked = True)
plt.show()

df['Cholesterol_bin'] = df['Cholesterol']//10 * 10

#plot.line() - используется при большом количестве вариантов категориальной переменной (более 20 значений)
fig = plt.figure(figsize= (14,5))
chart = df['Cholesterol_bin'].value_counts().sort_index().plot.line()
plt.show()

fig = plt.figure(figsize= (14,5))
chart = df['Cholesterol_bin'].value_counts().sort_index().plot.area(alpha = 0.5) # будет раскрашено под графиком полупрозрачно

#Гистограмма - классический инстрмуент для визуализации интервальных данных
#Визуально похожа на столбчатую диаграмму,гистограмма разбивает данные на равные интервалы и рисует частоты в каждом из столбцов
fig = plt.figure(figsize= (14,5))
df['Age'].plot.hist(bins= 10)
plt.show()

# параметр bins = количество столбцов
fig = plt.figure(figsize= (14,5))
df['Age'].plot.hist(bins = 2)

# ДВУМЕРНЫЕ данные - plot.scatter(), plot.hexbin()

df.plot.scatter(x='Cholesterol', y='Age',figsize=(14,5)) #Используется для того, чтобы показать зависимость одного показателя от другого
plt.show()

df.plot.hexbin(x='Cholesterol', y='Age',figsize=(20,8), gridsize = 30,
                                   cmap ='Blues')
plt.show()