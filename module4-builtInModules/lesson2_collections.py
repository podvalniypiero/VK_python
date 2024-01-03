# Модули для работы с коллекциями и функциями

# collections, functools, itertools
# 1 - module collections
# класс Counter - обычный словарь, который в качестве параметра принимает любой итерируемый объект и делает
# подсчет элементов в этом итерируемом объекте. Метод mostcommon - какие ключи обладают наибольшей частотой

import collections
l1 = [1,1,2,2,3,4]
counter = collections.Counter(l1) # словарь, в котором в качестве ключей указаны уникальные значения,
# а в качестве значений - подсчеты этих уникальных значений

# класс Deque двухсторонняя очередь - принимает любой итерируемый объект и работает с ним почти как со списком
# за CONST время!
deq = collections.deque(l1)

# добавлять элементы в список
deq.append(5) # deq.append(element) - добавить В КОНЕЦ за const время
deq.appendleft(-5) # deq.appendleft(element) - добавить В НАЧАЛО за const время

# доставать элементы из списка (модификация списка)
a = deq.pop() # из конца
b = deq.popleft() # из начала

default_dict_list = collections.defaultdict(list)
default_dict_set = collections.defaultdict(set)

# ChainedMap - цепной словарь, чтоб объединять в себе словари и искать значение по ключам
# последовательно от словаря к словарю
d1 = {0:1, 1:2}
d2 = {4:5, 6:7}
chained_map =collections.ChainMap(d1, d2)

if __name__ == '__main__':
    print(counter) # Counter({1: 2, 2: 2, 3: 1, 4: 1})
    print(counter.most_common(2)) # [(1, 2), (2, 2)]

    print(deq) # объект deque, который содержит в себе список deque([-5, 1, 1, 2, 2, 3, 4, 5])
    print(a)
    print(b)
    print(deq) # эти элементы удалились из списка после pop()

    default_dict_list[1].append(0)
    print(default_dict_list) # defaultdict(<class 'list'>, {1: [0]})

    default_dict_set[1].add(10)
    print(default_dict_set) # defaultdict(<class 'set'>, {1: {10}})

    print(chained_map) # ChainMap({0: 1, 1: 2}, {4: 5, 6: 7})
    print(chained_map[4]) # 5, значение по ключу 4
    print(chained_map[1])  # 2, значение по ключу 1

