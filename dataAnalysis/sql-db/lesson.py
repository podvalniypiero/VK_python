import sqlite3
import pandas as pd

connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()
query = """select "Albumid", "Title", "Artistid" from albums order by title limit 3;"""
albums = cursor.execute(query).fetchall()
print(albums)
print(pd.DataFrame(albums))
cursor.close()

# connection.commit()
connection.close()
# Проще воспользоваться методом pandas - read_sql_query.
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()
dfalbum = pd.read_sql_query(query, connection)
print(dfalbum)
cursor.close()

# connection.commit()
connection.close()
# Синтаксис языка SQL
# REATE TABLE
# CREATE TABLE [IF NOT EXISTS]  [schema_name].table_name ( column_1 data_type PRIMARY KEY, column_2 data_type NOT NULL, column_3 data_type DEFAULT 0, table_constraints  ) [WITHOUT ROWID];
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

query = """CREATE TABLE managers (
            contact_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE 
        );"""
_ = cursor.execute(query).fetchall()

connection.commit()
connection.close()
# Для обеспечения категорной целостности в языке SQL существуют спецификации PRIMARY KEY (первичный ключ) и UNIQUE (уникальный ключ).
#
# PRIMARY KEY не может быть NULL
# PRIMARY KEY может быть только один
connection = sqlite3.connect("chinook.db")
query = """SELECT  * FROM managers"""
managers = pd.read_sql_query(query, connection)
connection.close()
print(managers)

# INSERT¶
# Вставка новых записей в таблицу.
#
#  INSERT INTO table1 (column1,column2 ,..) VALUES     (value1,value2 ,...),    (value1,value2 ,...),     ...    (value1,value2 ,...);
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

query = """INSERT INTO managers (first_name, last_name, email, phone)
            VALUES
                ('Buddy', 'Rich', 'buddyrich@gmail.com', '79671950123'),
                -- ('Sam', 'Johnes', 'sam@gmail.com', NULL)
                -- ('Sam', 'Johnes', 'sam@gmail.com', '79671950123')
                ('Sam', 'Johnes', 'sam@gmail.com', '79671950125')
                ;"""
_ = cursor.execute(query).fetchall()

connection.commit()
# Если отсутствует список столбцов, то список вставляемых значений должен быть полный, то есть обеспечивать значения
# для всех столбцов таблицы. При этом порядок значений должен соответствовать порядку, заданному оператором CREATE TABLE для таблицы, в которую вставляются строки.
query = """SELECT  * FROM managers"""
managers = pd.read_sql_query(query, connection)
print(managers)

# UPDATE
#  UPDATE table SET column_1 = new_value_1,     column_2 = new_value_2 WHERE     search_condition  ORDER column_or_expression LIMIT row_count OFFSET offset;
query = """UPDATE managers SET first_name = 'Ivan' WHERE phone = '79671950125';"""
_ = cursor.execute(query).fetchall()

connection.commit()
query = """SELECT  * FROM managers"""
managers = pd.read_sql_query(query, connection)
print(managers)

# DELETE
query = """DELETE FROM managers WHERE phone = '79671950123';"""
_ = cursor.execute(query).fetchall()

connection.commit()
query = """SELECT  * FROM managers"""
managers = pd.read_sql_query(query, connection)
print(managers)

# DROP
# DROP TABLE [IF EXISTS] [schema_name.]table_name;
query = """DROP TABLE IF EXISTS managers;"""
_ = cursor.execute(query).fetchall()

connection.commit()
connection.close()

# SELECT
# Оператор SELECT осуществляет выборку из базы данных.
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

query = """SELECT  * FROM employees"""
df = pd.read_sql_query(query, connection)
print(df.head(3))

query = """SELECT LastName, FirstName, BirthDate FROM employees"""
df = pd.read_sql_query(query, connection)
print(df.head(3))

# DISTINCT
# Только уникальные значения.
query = """SELECT City FROM employees"""
df = pd.read_sql_query(query, connection)
print(df.shape)
print(df)

query = """SELECT DISTINCT City FROM employees"""
df = pd.read_sql_query(query, connection)
print(df.shape)
print(df)

# ORDER BY
# Cортировка запроса по полю.
query = """SELECT City, BirthDate FROM employees ORDER BY BirthDate"""
df = pd.read_sql_query(query, connection)
print(df)

query = """SELECT City, BirthDate FROM employees ORDER BY 2 DESC"""
df = pd.read_sql_query(query, connection)
print(df)

# WHERE
# Задает условие на горизонтальную выборку.
query = """SELECT * FROM tracks WHERE UnitPrice > 0.99"""
df = pd.read_sql_query(query, connection)
print(df.head(2))

# AND, OR, NOT
query = """SELECT * FROM tracks WHERE UnitPrice > 0.99 
                                AND (Composer is NOT NULL OR GenreId = 18) 
                                AND NOT Name = 'Occupation / Precipice' """
df = pd.read_sql_query(query, connection)
print(df.head(2))

# BETWEEN, IN
query = """SELECT * FROM tracks WHERE UnitPrice BETWEEN 0.99 AND 1.5 
                                AND GenreId IN (10, 24)
                                ; """
df = pd.read_sql_query(query, connection)
print(df.head(2))

# Подвыборки
query = """ SELECT *
            FROM tracks 
            WHERE GenreId IN (SELECT GenreId 
                                FROM genres
                                WHERE Name = 'Opera') """
df = pd.read_sql_query(query, connection)
print(df)

# LIKE
# _ вместо любого единичного символа в проверяемом значении;
# % заменяет последовательность любых символов (число символов в последовательности может быть от 0 и более) в проверяемом значении.
query = """ SELECT DISTINCT Composer
            FROM tracks 
            WHERE Composer LIKE 'U_' """
df = pd.read_sql_query(query, connection)
print(df)

query = """ SELECT DISTINCT Composer
            FROM tracks 
            WHERE Composer LIKE 'U%' """
df = pd.read_sql_query(query, connection)
print(df)

query = """ SELECT DISTINCT Composer
            FROM tracks 
            WHERE Composer LIKE '%U%' """
df = pd.read_sql_query(query, connection)
print(df)

# Агрегаты SUM, MIN, MAX, AVG, COUNT
query = """ SELECT COUNT (DISTINCT Composer)
            FROM tracks 
            WHERE Composer LIKE '%U%' """
df = pd.read_sql_query(query, connection)
print(df)

query = """SELECT AVG(Milliseconds) 
            FROM tracks 
                                ; """
df = pd.read_sql_query(query, connection)
print(df.head(2))

# GROUP BY используется для объединения результатов выборки по одному или нескольким столбцам
query = """ SELECT *
            FROM tracks 
            WHERE Bytes = (SELECT MAX(Bytes)  
                                FROM tracks) """
df = pd.read_sql_query(query, connection)
print(df)

query = """ SELECT GenreId, AVG(Milliseconds)/60000 as length
            FROM tracks 
            GROUP BY 1
            ORDER BY 2 DESC"""
df = pd.read_sql_query(query, connection)
print(df)

# Если предложение WHERE определяет предикат для фильтрации строк, то предложение
# HAVING применяется после группировки для определения аналогичного предиката,
# фильтрующего группы по значениям агрегатных функций.
query = """ SELECT GenreId, AVG(Milliseconds)/60000 as length
            FROM tracks 
            GROUP BY 1
            HAVING length > 5
            ORDER BY 2 DESC"""
df = pd.read_sql_query(query, connection)
print(df)

# Выбор из нескольких источников
query = """ SELECT tracks.*,
                   genres.*
            FROM tracks 
            INNER JOIN genres ON tracks.Genreid = genres.Genreid
            WHERE genres.Name = 'Classical'
            """
df = pd.read_sql_query(query, connection)
print(df)

# Union
query = """ SELECT FirstName, LastName, 'Employee' AS Type
            FROM employees
            UNION
            SELECT FirstName, LastName, 'Customer'
            FROM customers;
            """
df = pd.read_sql_query(query, connection)
print(df)