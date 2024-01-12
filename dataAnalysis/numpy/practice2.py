import pandas as pd
import numpy as np
import timeit
ml = pd.read_csv('files/orders.csv', sep = ',').drop_duplicates()
print(ml)
print(ml.head(3))
print(ml.tail(2))

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
pd.set_option('display.precision', 0) # 0 знаков после запятой

print(ml.shape)
print(ml.shape[0])
print(ml.columns)
print(ml.describe()) # получить статистику
print(ml.describe(include=['object']))

print(ml.vendor_id.value_counts(dropna=False)[:10])
print(ml.info())

for dtype in [ 'float', 'int', 'object']:
    selected_dtype = ml.select_dtypes(include=[dtype])
    mean_usage_b = selected_dtype.memory_usage(deep=True).mean()
    mean_usage_mb = mean_usage_b / 1024**2
    print("Average memory usage for {} columns: {:03.2f} MB".format(dtype, mean_usage_mb))

# оптимизация памяти
# ml['price'] = ml['price'].astype('float32')
# print(ml.info())

# timeit(ml.groupby('vendor_id')['price'].mean().to_frame())

# группировка данных GROUPBY()
#ml.groupby(by=grouping_columns)[columns_to_show].function()
# ml.groupby(by='vendor_id')['price'].max()

# drop_duplicates() - удаляем все дубликаты строк в таблице, если они есть

# сколько уникальных городов представлено в датафрейме?
unique_cities = ml.city_id.unique()
print(unique_cities) # [23 25 26 24] - объект ndarray
print(unique_cities.size) # 4

# сколько ресторанов специализируются на рыбе?
filteredSpec = (ml.spec == 'Рыба')
print(ml[filteredSpec].vendor_id.unique().size) # 18

print(ml.dtypes) # типы всех столбцов

# какие столбцы имеют определенный тип - сколько столбцов определенного типа в датафрейме
print(ml.dtypes[ml.dtypes == 'float64'].size) # 2

# сколько дней у ресторана 40065 было менее 20 успешных заказов?
filteredMin20orders = ((ml.vendor_id == 40065) & (ml.successful_orders < 20))
print(ml[filteredMin20orders].date.unique().size) # 45