# ВСТРОЕННЫЕ FUNC

# 1) группа приведения типов: int,float,str,byte,bool - неявные преобразования типов
a = 1


if __name__ == '__main__':
    # pass
    print(float(a))
    print(str(a))
    print(bool(a))
    b = 3.0
    print(int(a) + b) # 4.0 неявное преобразование во float

# 2) группа встроенных коллекций: dict, list, set, frozenset, tuple
d = dict(a=1, b=2)
d1 = {"a": 3, "b": 4}
if __name__ == '__main__':
    print(d, d1)

l = list(range(10)) # список, в который передали генератор от 0 до 9
if __name__ == '__main__':
    print(l)

# передача аргументов в list явно
l1 = [1,2,3,4,5]
if __name__ == '__main__':
    print(l1)
# SET - множество, принимает любой итерируемый объект и возвращает множество с УНИКАЛЬНЫМИ элементами итерируемого объекта
# изменяемый - НЕЛЬЗЯ использовать как ключ в словаре
s = set(range(10))
s1 = set([1,1,2,2,3,3]) # {1, 2, 3} => SET хранит только УНИКАЛЬНЫЕ значения
if __name__ == '__main__':
    print(s)
    print(s1)
    print(1 in s) # True
    s1.add(100)
    s1.remove(3)
    print(s1)

# FROZENSET - множество, принимает любой итерируемый объект и возвращает множество с элементами итерируемого объекта, которое уже нельзя модифицировать
# неизменяемый - можно использовать как ключ в словаре
fs = frozenset(s)
if __name__ == '__main__':
    print(fs)
    # fs.add(100) # 'frozenset' object has no attribute 'add'
    # fs.remove(3) # 'frozenset' object has no attribute 'remove'

# TUPLE - принимает любой итерируемый объект и возвращает кортеж и элементами интерируемого объекта
t = tuple(range(10)) # неявно, функция tuple требует, чтобы объект был итерируемым
t1 = (5,15,20)
if __name__ == '__main__':
    print(t)
    print(t1)

# 3) группа math функций: abs, pow, min, max, divmod, round
a = -1.0
b = 3
c = 4
d = [1,2,0,-1] #list
e = 1.234
if __name__ == '__main__':
    print(abs(a))
    print(pow(b,c, 10)) # b*c и от результата взять mod 10
    print(min(b,c), max(b,c)) # от позиционных элементов, которые являются не итерируемыми объектами
    print(max(d), min(d)) # от непозиционных - элемента, который является итерируемым объектом

    print(divmod(b,c)) # выдает кортеж (b div c, b mod c)

    print(round(e,2)) # 1.23

# 4) группа функций для работы с генераторами и итераторами:
# enumerate - при прохождении по итерируемому объекту получать номер элемента в итерируемом объекте
l = [2,4,6]
if __name__ == '__main__':
    for i, el in enumerate(l):
        print(i,el)
        # 0 2
        # 1 4
        # 2 6
# zip - одновременно проходиться по нескольким итерируемым объектам
# - вывести все индексы списка по какому-то условию
l = [2,5,6]
l1 = []
l2 = []

if __name__ == '__main__':
    for i, el in enumerate(l):
        l1.append(i)
        l2.append(el)
    for i, el in zip(l1, l2): # можно проходиться по нескольким итерируемым объектам сразу,
        # но если длина объектов разная, то zip дойдет до конца самого короткого элемента и остановит обход
        if el % 2 == 0:
            print(i,el)
            # 0 2
            # 2 6

# filer - проходиться по всем элементам итерируемого объекта и забирать только те элементы, которые подходят по критерию первого параметра в функции
l = [-2, -1, -100, 5, 6, 0]
def f(a):
    return a > 0
if __name__ == '__main__':
    for el in filter(f,l):
        print(el)
# sorted - отсортировать объект по критерию, по умолчанию - по возрастанию, reversed = True - сортировка в обратном порядке
l = [4, 6, 3]
if __name__ == '__main__':
    for i in sorted(l, reverse=True):
        print(i)

l = ["ab", "a", 'abcd', 'abc']
if __name__ == '__main__':
    for i in sorted(l, key=len, reverse=True):
        print(i)

l = [(5,6), (1,2), (3,4)]
if __name__ == '__main__':
    for i in sorted(l, key=lambda x: x[1], reverse=True): # отсортировать по второму элементу кортежа по убыванию
        print(i)

# reversed
l = [1, 2, 3, 4]
t = (5, 6, 7, 8)
if __name__ == '__main__':
    for el in reversed(l):
        print(el)
# all - все элементы объекта true ИЛИ объект пуст
# any - true, если хотя бы 1 элемент объекта true - проверить, все ли элементы массива отрицательны?
l = [-1, 2, 3, 4]
def f(a):
    return a < 0
if __name__ == '__main__':
    print(any(map(f, l)))
    print(all(map(f, l)))

# sum - возвращает сумму всех элементов итерируемого объекта
l = [-1, 2, 3, 4]

if __name__ == '__main__':
    print(sum(l))
# len - возвращает длину итерируемого объекта
l = [-1, 2, 3, 4]

if __name__ == '__main__':
    print(len(l))

# 5) группа функций для работы с областью видимости
# locals - возвращает словарь с результатом - локальные переменные, которые используются
# globals - возвращает словарь с результатом - глобальные переменные, которые используются
l = [-1, 2, 3, 4]
def f():
    a = 1
    b = 2
    print(locals()) # {'a': 1, 'b': 2}
if __name__ == '__main__':
    f()
    print(globals())

# 6) type
l = [-1, 2, 3, 4]
def f():
    a = 1
    b = 2
    print(locals()) # {'a': 1, 'b': 2}
if __name__ == '__main__':
    print(type(f)) # <class 'function'>
    print(type(l)) # <class 'list'>
    a = 1
    print(type(a)) # <class 'int'>