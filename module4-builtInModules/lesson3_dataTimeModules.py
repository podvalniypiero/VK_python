# Модули для работы с датой и временем
# библиотека DateTime
# модули: time (время без даты), date (дата без времени), datetime
import datetime
d = datetime.date(2023, 6, 23)
d_today = datetime.date.today()

t = datetime.time(23, 59, 59)
dt = datetime.datetime(2023, 6, 23, 23, 59, 59)
dt_now = datetime.datetime.now()
time_now = dt_now.time()

# timedelta() сдвигать время
delta = datetime.timedelta(days = 5)

# форматировать время datetime.datetime.strftime()
string_from_dt = datetime.datetime.strftime(dt_now, '%Y-%d-%m %H:%M:%S') # тут все всегда с маленькой/большой буквы, это правило

# парсинг даты и времени из строки datetime.datetime.strptime(string_data, format)
dt_from_string = datetime.datetime.strptime(string_from_dt, '%Y-%d-%m %H:%M:%S')
if __name__ == '__main__':
    print(d) # 2023-06-23
    print(d_today)
    print(t)
    print(dt)
    print(dt_now)
    print(time_now)

    print(dt_now + delta) # +5 суток
    print(dt_now - delta)  # -5 суток

    print(string_from_dt)
    print(dt_from_string)

    print(dt_from_string + delta) #операцию можно сделать только с объектом даты, не со строкой
