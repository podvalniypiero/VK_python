# 3 базовых sequence type: LIST, TUPLE ( кортеж ), RANGE

# 1 – LIST
a = []
# или с помощью ключевого слова list
a = list()
a = [1, "ave", 13, "maria"]
print(a)
print(len(a))
print(a[2])

# 2 – TUPLE
b = ()
b = tuple()
b = (1, "ave", 13, "maria")
print(b)
print(len(b))
print(b[1])
print(b[-1]) #первый элемент с конца
print(b[-len(b)])

print(b[1:5:2])
#iteration
for x in a:
    print(x)
#входит ли элемент в список/кортеж
print(2 in b, 2 not in b)
print(13 in a)

a = [1,2,3,4,5,-2,2,2,2]
print(min(a),max(a))

# index первого вхождения
print(a.index(2))
# поиск с какого-то index
print(a.index(2,2))
#сколько раз входит в список
print(a.count(2),a.count(222))

#конкатенация
c = a + [222,3,66]
print(c)
# с = a * 3
# print(c) # НЕ РАБОТАЕТ

# FALSY
print(bool([]),bool(()))

print(bool([1, "ave"]),bool((1,"ave")))

### Операции, свойственные только для LIST
# изменяемость
d = [1,2,3,4,5]
d[0] = 2
print(d)
d[0:3] = [-3,-4,-5]
print(d)
del d[0:3] #удаление промежутка из list
del d[0]
print(d)

d.append(66)
print(d)
# append для НЕСКОЛЬКИХ значений
d.extend([6,77,7,88,8,99,9])
print(d)
d +=[1010]
print(d)

d*=2
print(d)

d.insert(0,1) # на какой index ставим, что ставим
print(d)

# POP() достает крайний элемент с конца и ВОЗВРАЩАЕТ его
print(d.pop())
print(d.pop(), d)
print(d.pop(2)) # достанет элемент с этим index

#REMOVE() удалить по значению
d.remove(5)
print(d)

#SORT() по возрастанию
d.sort()
print(d)

#REVERSE() - можно сначала применить sort() а затем reverse() - получим сортировку по убыванию
d.reverse()
print(d)

#COPY(), CLEAR()
e = d.copy()
d.clear()
print(d,e)

f = [[0,1]] * 3 #делает копию элементов
print(f)
f[0][0] = 11
print(f)

# РАСПАКОВКА переменных
var1,var2,var3 = [1,33,["ave","maria"]]
print(var1, var2, var3)

var1,var2,(var3_1, var3_2) = [1,33,["ave","maria"]]
print(var1, var2, var3_1, var3_2)

#LIST из range 10 (0-9)
a = list(range(10))
print(a)

#FOR циклы
b = [ 2 ** x for x in a if x%2 == 0]
print(b)

c = tuple(int(x) for x in "a1b2c3def" if x.isdigit())
print(c)

# JOIN() и SPLIT()
strings = ["Hello", "World", "2023" ]

joined = " ".join(strings)
print(joined)
print(joined.split())

joined = "...".join(strings)
print(joined)
print(joined.split("..."))