# Написать функцию most_common_months, которая принимает в качестве параметра список строк,
# которые являются датами формата “ГГГГ-ММ-ДДTЧЧ-ММ-СС” и некоторое целое число n, и выводит топ n самых
# частых месяцев этих дат.
# Желательно, чтобы это было реализовано через Counter из модуля collections.

import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    month = []
    for date in dates:
        dt = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        month.append(dt.month)  # добавляем в список month от этой даты только month

    counted_month = Counter(month)  # количество вхождений каждого месяца в список
    moda = counted_month.most_common(n)  # n самых частых месяцев в списке

    return [month for month, _ in moda]


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
