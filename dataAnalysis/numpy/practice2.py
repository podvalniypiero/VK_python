import pandas as pd
import numpy as np
ml = pd.read_csv('files/orders.csv', sep = ',').drop_duplicates()
print(ml)

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