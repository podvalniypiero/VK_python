# DATA COLLECTIONS
# DICTIONARIES изменяемая структура как и list
a = dict(one=1, two=2, three = 3 ) # словарь: ключ - значение
b = {'one': 1, 'two': 2, 'three': 3}
c = dict([('two', 2),('one', 1),('three', 3)])
d = dict({'three': 3, 'one': 1, 'two': 2})
e = dict({'one': 1, 'three': 3}, two =2 )
print(a == b == c == d ==e)

for key, value in a.items(): # распаковка переменных в key, value
    print(value)

for x in a.items():
    print(x)

# создание словаря ключ : значение - x : 2**x
f = {x : 2 ** x for x in range(10) }
print(f)

# создание словаря из словаря - выборка нечетных ключей
g = {k : v for k, v in f.items() if k % 2 == 1 }
print(g)

# ПОМЕНЯТЬ местами значение : ключ
g = {v : k for k, v in f.items() }
print(g)

#len
print(len(g), len(f))
#in входит ли ключ
print(1 in g, 2 in g, 2 not in g, 11 in g, 16 in g, 32 in g)

# обращение по key
print(g[4], g[1])

# если не уверены, что значение с таким key существует и хотим получить -1 ВМЕСТО ОШИБКИ в этом случае
#DICT.GET(KEY,IF_Error_Value)
print(g.get(10,-1), g.get(2, -1))

# изменяемость - его элементы можно менять
g[10] = 1024
print(g)

# UPDATE - исходный словарь.update(словарь с новыми значениями)
a = {'one': 1, 'two': 2, 'three': 3}
b = {'two': -2, 'three': -3, 'four': -4}
a.update(b)
print(a)

# DEL
del a["one"]
print(a)

# dict.POP(key) получить value по key - в dict этого элемента уже не будет, тк его POPнули
value = a.pop('two')
print(value, a)

value = a.pop('two', None)
print(value, a)

print(a.keys())
print(a.values())
print(a.items()) # пары (key, value)

# copy() clear()
b = a.copy()
a.clear()
print(a,b)

print(bool(a), bool(b))

# mutable список, словарь - immutable строки, кортежи, range
# неизменяемые коллекции в отличие от изм-х имеют встроенный метод hash(), это свойство дает им
# возможность быть ключом в структуре данных словарь и такие контейнеры мб членами структуры множеств
hash(1)
hash('abbbbb')
hash((1,2,3))
# hash[1,2,3] от СПИСКА получить НЕ можем - тк список может измениться в любой момент
# и hash от него тоже поменяется
# у изменяемых структур данных НЕТ hash'а

d = {(1,2,3): "123", (1,2, range(10)): "12"} # главное, чтобы key был НЕизменяемым, тк dict будет брать hash(key)
print(d)

# SET и FROZEN SET
a = {1, 2, 3, 4, 1, 2, 3, 4}
b = {1 , 2 , 3}
print(a)
print(set([1, 2, 3, 4]))
print(1 in a, 10 in a, 11 not in a)

print( a < {1, 2, 3, 4, 5, 6}) # a является подмножеством того что справа
print( a >= {1, 2, 3}) # a содержит либо совпадает с множеством

print( a | b)
print(a & b)
print(a - b)
print(b - a)
print( a ^ b ) # симметричная разность - элементы есть только в a или только в b, но не там и там

# discard()
a.add(10)
a.remove(2)
print(a)
a.discard(3) # как remove только он не упадет с ошибкой если не найдет такой элемент
a.discard(33)
print(a)

val = a.pop() # удаляет произвольный элемент
print(val, a)

# copy() clear()
b = a.copy()
a.clear()
print(a,b)

# FROZEN SET неизменяемая версия SET - эту структуру можно использовать в качестве key в dict
с = frozenset([1, 2, 3, 4, 3, 1, 2, 2])
print(c)