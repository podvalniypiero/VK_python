# Написать функцию parse_time, которая принимает строку в качестве параметра,
# которая является временем формата “ГГГГ ММ ДД ЧЧ ММ СС” и парсит эту строку в объект
# datetime.datetime и сдвигает ее на один день вперед.
import datetime

string_datetime = input()

def parse_time(s):
    dt_from_s = datetime.datetime.strptime(s, '%Y %m %d %H %M %S')
    delta = datetime.timedelta(days=1)
    new_dt = dt_from_s + delta

    return (new_dt.day)

print(parse_time(string_datetime))