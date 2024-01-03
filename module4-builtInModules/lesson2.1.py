# Написать функцию fill_specializations, которая принимает список кортежей из специальности
# и имени и возвращает словарь, где в качестве ключей специальности, а в качестве значений
# - списки имен. Желательно, чтобы это было реализовано через словарь со значением по умолчанию.
from typing import List, Tuple
import collections

def fill_specializations(specializations: List[Tuple[str, str]]):
    res = collections.defaultdict(list)
    for specialization, name in specializations:
        res[specialization].append(name)
    return dict(res)

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
