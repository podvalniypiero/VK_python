# FUNCTION DEFINITION
#def f(pos_only_1, pos_only_2, /, pos_or_keyword, *, keyword_only_1, keyword_only_2):
def phone(model, charge = 100, storage = "128 Gb", status = "working"):
    if not 0 <= charge <= 100:
        print("Incorrect charge data!")
        return
    print(
        f"This {model} is {charge} % charged."
        f" It has {storage} of storage, current status is '{status}'."
    )

phone("IPhone", 86)

def func(val, var=[]):
    var.append(val)
    return var
# a = []
# func(1, a)
# func(3, a)
# func(5, a)
# print(a)
a = func(1)
b = func(3)
c = func(5)

print(a,b,c) #[1, 3, 5] [1, 3, 5] [1, 3, 5]

# решить эту проблему - создание аргумента списка var по умолчанию во время объявления функции единожды - None
def func(val, var=None):
    if var is None:
        var = []
    var = var or [] # x OR y <=> x is True than x else y
    # x AND y <=> x is False then x else y
    var.append(val)
    return var
a = func(1)
b = func(3)
c = func(5)

print(a,b,c) #[1] [3] [5]

def pos_only_arg(arg, /): #функция принимает только позиционные аргументы, вызвать типо fun(arg = 133) НЕЛЬЗЯ
    print(arg)

def keywords_only_arg(*, arg): #функция принимает только непозиционные аргументы, вызвать типо fun(133) НЕЛЬЗЯ
    print(arg)
def combined_arg(pos_only, /, standard, *, keywords_only): #функция принимает только позиционные аргументы, вызвать типо fun(arg = 133) НЕЛЬЗЯ
    print(pos_only, standard, keywords_only)

# standard можно передать как позиционный так и не позиционный
combined_arg(1, 22, keywords_only = 'string')
combined_arg(1, standard=22, keywords_only = 'string')

params = ["Iphone", 86, "512 Gb", "Turned off"]
phone(*params)

# передавать параметры словарем
dict_params = {"model": "Iphone", "charge": 86, "storage": "512 Gb", "status": "Turned off"}
phone(**dict_params)

params = ["Iphone", 86]
dict_params = {"storage": "512 Gb", "status": "Turned off"}
phone(*params, **dict_params)

def all_args(*args, **kwargs):
    print(args)
    print(kwargs)
# полезна при определении декораторов функции
# можно передавать любое число аргументов, как позиционных так и именованных
all_args(1, 2, 3, 4, a=1, b=2, c=3)

def plus(a, b):
    return a + b

c = plus(1, 2)
print(c)
