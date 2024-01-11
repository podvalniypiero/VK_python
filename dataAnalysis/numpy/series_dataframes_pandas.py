# pandas - panel datas - панельные данные получены в ходе исследования и структурированы в виде таблиц
# основные структуры -
# Series (объект, похожий на 1мерный массив - наличие ассоциативных меток-индексов вдоль каждого элемента из списка -> ассоциативный массив или словарь)
# и DataFrame

# SERIES
# Структура/объект Series представляет из себя объект, похожий на одномерный массив (питоновский список, например),
# но отличительной его чертой является наличие ассоциированных меток, т.н. индексов,
# вдоль каждого элемента из списка. Такая особенность превращает его в ассоциативный массив или словарь в Python.
import pandas as pd
import numpy as np

my_series = pd.Series([5, 6, 7, 8, 9, 10])
print(my_series)
print(my_series.index) # итератор с шагом 1 RangeIndex(start=0, stop=6, step=1)
print(my_series.values)
my_series2 = pd.Series([5, 6, 7, 8, 9, 10],
                       index=['a', 'b', 'c', 'd', 'e', 'f'])
print(my_series2)
print(my_series2.index)
print(my_series[4])
print(my_series[[4]]) # 4 9  - индекс элемент
print(my_series2['a'])

mask = my_series > 7
print(mask)
print(my_series[mask])

my_series2[['a', 'b', 'f']] = 0
print(my_series2)
my_series2[(my_series2 > 0)]
my_series2 > 0

my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
print(my_series3)

my_series3.name = 'numbers'
my_series3.index.name = 'letters'
print(my_series3)

# PANDAS DATAFRAME
# Объект DataFrame лучше всего представлять себе в виде обычной таблицы и это правильно, ведь DataFrame
# является табличной структурой данных. В любой таблице всегда присутствуют строки и столбцы.
# Столбцами в объекте DataFrame выступают объекты Series, строки которых являются их непосредственными элементами.

df = pd.DataFrame({
    'city': ['Moscow', 'Krasnodar', 'Belgorod', 'Kazan'],
    'delivery_time': [25, 29, 32, 30],
    'couriers': [11440, 784, 112, 998]
})
print(df)
print(df.delivery_time)
print(type(df.delivery_time))

print(df['delivery_time'])
print(df[['delivery_time']])

df.index = ['Msc', 'Krd', 'Blg', 'Kzn']
print(df)

# ИМПОРТ данных
# pd.read_csv('filename')
# pd.read_excel('filename')
# pd.read_sql(query,connection_object)
# pd.read_table(filename)
# pd.read_json(json_string)
# pd.read_html(url)
# pd.read_clipboard()
# pd.DataFrame(dict)

ml = pd.read_csv('files/orders_history.csv', sep = ',')
print(ml.head(2)) # выведет 0 и 1 строки

# pandas может работать с очень большими файлами
# можно считывать chunk'ами, если файл настолько большой, что не помещается в оперативной памяти компьютера
c_size = 10000
for gm_chunk in pd.read_csv('files/orders_history.csv',
                            sep = ',',
                            chunksize=c_size):
    print(gm_chunk.shape)


# ЭКСПОРТ данных
# df.to_csv(filename)
# df.to_excel(filename)
# df.to_sql(table_name, connection_object)
# df.to_json(filename)
# df.to_html(filename)
# df.to_clipboard()

# Доступ к данным
# Доступ к строкам по индексу возможен несколькими способами:
# методы:
# .loc - используется для доступа по СТРОКЕ
# .iloc - используется для доступа по ИНДЕКСУ - числовому значению (начиная от 0)

print(df.loc['Msc'])
print(df.iloc[1])
print(type(df.iloc[0])) # каждая строка имеет индекс типа серии

#индекс + колонки
print(df.loc[['Msc', 'Kzn'], 'couriers'])
print(df.iloc[[0,1],[1]])
print(df[df.delivery_time > 30][['city', 'couriers']])
print(df[(df.delivery_time >= 25) | (df.city == 'Msc')][['city','delivery_time']])

filters = (df.city == 'Moscow')
print(df[filters])

# НОВАЯ колонка
df['delivery_time_hours'] = df['delivery_time'] / 60
print(df)

# УДАЛЕНИЕ
# при дропе колонок необходимо в том или ином виде перезаписывать данные в исходном датафрейме

# df.drop(['delivery_time_hours'], axis = 1 )
# # если удаляем колонку, то axis = 1, если строку, то axis = 0
#
# df.drop(['delivery_time_hours'], axis='columns',inplace =True) # вот так исходный dataframe ИЗМЕНИТСЯ

#!!!
df = df.drop(['delivery_time_hours'], axis=1) # либо просто переопределить dataframe вот так
print(df)

# ИЗМЕНИТЬ НАЗВАНИЕ колонок
df = df.rename(columns={'couriers': 'num_of_couriers'})
print(df)

# dataframe.NLARGEST(N, 'column_name') - n САМЫХ БОЛЬШИХ показателей из колонки - нет нужды в сортировке
print(df.nlargest(3,'delivery_time'))# по параметру delivery_time

# dataframe.NSMALLEST(N, 'column_name') - n САМЫХ МАЛЕНЬКИХ показателей из колонки - нет нужды в сортировке
print(df.nsmallest(3,'delivery_time'))

# ПЕРЕИМЕНОВАТЬ ВСЕ колонки
df.columns = ['City', 'Delivery_Time', 'Number_of_Couriers']
print(df)