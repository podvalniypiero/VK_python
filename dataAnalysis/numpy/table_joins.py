# способы объединения таблиц в библиотеке Pandas
# функции merge(), join() и concat()
import pandas as pd
raw_data = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
df_a.index = [0,1,2,3,4]
print(df_a)
print(df_a.head(2))
print(df_a.tail(2))
print(df_a.columns)
print(df_a.info())

raw_data = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
df_b.index = [2,3,4,5,6]
print(df_b)

raw_data = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_n = pd.DataFrame(raw_data, columns = ['subject_id','test_id'])
print(df_n)

# Concat() используется для объединения таблиц по вертикальной или горизонтальной оси.

# по строке axis=0
df_new = pd.concat([df_a, df_b], axis = 0)
print(df_new)
# по столбцам axis=1
df_new_ = pd.concat([df_a, df_b], axis = 1)
print(df_new_)

#Concat(), но только с помощью атрибута "INNER" - только те , что есть в обоих таблицах
df_new_ = pd.concat([df_a, df_b],axis = 1, join='inner')
print(df_new_)

#Append() - частный случай метода Concat() с параметрами (axis=0, join='OUTER') - вообще все строки из двух таблиц
print(df_a._append(df_b))

#Метод Join основан на объединении таблиц через индексы (способ объединения указывается с помощью параметра how = ['left','right','inner','outer']).
# df_a.join(df_b,how = 'left')
print(df_a.join(df_b,rsuffix='_right_table',how = 'left'))

# Merge используется для объединения таблиц по любым колонкам с помощью методов left_on и right_on.
print(df_new)
print(pd.merge(df_new, df_n, on='subject_id'))

print(pd.merge(df_new, df_n, left_on='subject_id', right_on='subject_id'))

print(pd.merge(df_a, df_b, on='subject_id', how='left'))
print(pd.merge(df_a, df_b, on='subject_id', how='right'))

print(pd.merge(df_a, df_b, right_index=True, left_index=True))