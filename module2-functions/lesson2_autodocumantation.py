# AutoDocumentation, function description

def phone(model: str, charge: int=100, storage:str = "128 Gb", status:str = "working")-> None: # такая конструкция
    # называется тайпинг - ничего не возвращает
    #аннотация функции
    """
    :param model: model of phone e.g. "IPhone", "Samsung", etc.
    :param charge: percent of charge available
    :param storage: overall storage size
    :param status: system status of phone
    :return: None
    This function displays info about phone.

    """
    if not 0 <= charge <= 100:
        print("Incorrect charge data!")
        return
    print(
        f"This {model} is {charge} % charged."
        f" It has {storage} of storage, current status is '{status}'."
    )

help(phone)

def important_func():
    ...
# или pass
important_func() # можем вот так объявить func, если пока не знаем что писать (с помощью ... чтоб не выдало error)

# С точки зрения объектов в языке Python, func это объект 1го порядка
# значит с func можно делать то же самое, что и с объектами
# можно записывать в переменные
# можно передавать как аргументы других func

phone_copy = phone
print(phone_copy("CopyPhone"))

# анонимные или lambda-func - передача их как доп аргументы в другие func, в методы, в классы
l_func = lambda x: 2 ** x

def func(x):
    return 2 ** x

a = [1,2,3,4,5]
b = sorted(a, key = lambda x: -x) # сортировка по убыванию
print(b)

# рекурсивный вызов func
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(factorial(3))

def factorial_no_recursion(n): # без рекурсии, безопасный вариант: нет угрозы переполнения стека
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result
print(factorial_no_recursion(-1))

#Поданные на вход строки преобразовать к верхнему регистру,
# если первым строки является символ ‘!’, иначе привести к нижнему.
# В первом случае также убрать лидирующий ‘!’
seq = 'HJJJ'
for i in map(lambda x: x[1:].upper() if x[0] == "!" else x.lower(), seq):
    print(i)

