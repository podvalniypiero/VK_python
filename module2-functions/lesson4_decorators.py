# DECORATORS
# декоратор – это функция, которая принимает функцию в качестве аргумента и возвращает функцию как результат.
# Декоратор – это специальная функция, которая принимает на вход другую функцию и возвращает новую функцию,
# обернутую вокруг исходной. Он позволяет добавить дополнительную функциональность к функции, не изменяя ее код.
def my_decorator(func):
    print("Before wrapper def")

    def wrapper():
        print("Before func call")
        func()
        print("After func call")

    print("After wrapper def")
    return wrapper # возвращаем именно func, а не ее вызов

@my_decorator
def my_func():
    print("hello world")
my_func()

# my_func = my_decorator(my_func) аналогично @my_decorator
print("_______________________")
my_func_decorated = my_decorator(my_func) # вызываем декоратор от нашей функции - объявляли декорированную func
print("_______________________")
my_func_decorated() # здесь мы уже вызываем декорированную func: то, что внутри def wrapper()
print("_______________________")

# к func можно применять сразу несколько декораторов, декораторы будут накладываться снизу вверх

def my_decorator1(func):
    def wrapper():
        print("Before func call 1")
        func()
        print("After func call 1")
    return wrapper

def my_decorator2(func):
    def wrapper():
        print("Before func call 2")
        func()
        print("After func call 2")
    return wrapper

@my_decorator2 # все, функция декорируется нашим декоратором
@my_decorator1 # все, функция декорируется нашим декоратором
def my_func(): # это будет логика func() во wrapper()
    print("hello world")
# my_func = my_decorator2(my_decorator1(my_func)) аналогично @my_decorator2 и @my_decorator1
my_func() # вызываем декорированную функцию

# decorators with ARGUMENTS
def my_decorator(func):
    def wrapper(*args,**kwargs): # позволяет во wrapper принимать любое количество arg в любом виде
        print("Before func call")
        # func(*args,**kwargs)
        tmp = func(*args,**kwargs)
        print("After func call")
        return tmp
    return wrapper
@my_decorator
def phone(model, charge = 100, storage = "128 Gb", status = "working"):
    if not 0 <= charge <= 100:
        print("Incorrect charge data!")
        return
    print(
        f"This {model} is {charge} % charged."
        f" It has {storage} of storage, current status is '{status}'."
    )
phone("iPhone")

# параметризованный decorator
def my_decorator_n(number=1):
    def my_decorator(func):
        def wrapper(*args,**kwargs): # позволяет во wrapper принимать любое количество arg в любом виде
            print(f"Before func call {number}")
            # func(*args,**kwargs)
            tmp = func(*args,**kwargs)
            print(f"After func call {number}")
            return tmp
        return wrapper
    return my_decorator
@my_decorator_n(123) # @my_decorator_n(number = 123)
def phone(model, charge = 100, storage = "128 Gb", status = "working"):
    if not 0 <= charge <= 100:
        print("Incorrect charge data!")
        return
    print(
        f"This {model} is {charge} % charged."
        f" It has {storage} of storage, current status is '{status}'."
    )
phone("iPhone")

# phone = my_decorator_n(number=123)(phone)

# АННОТАЦИЯ для декорированных func
# при попытке получить аннотацию декорированной func мы получим аннотацию обёртки, так как по сути мы вызываем её
# подключаем библиотеку functools и пишем встроенную функцию wraps
# в виде декоратора и передаём в аргументы func: @functools.wraps(func) перед def wrapper():
import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # позволяет во wrapper принимать любое количество arg в любом виде
        print("Before func call")
        tmp = func(*args, **kwargs)
        print("After func call")
        return tmp
    return wrapper

def phone(model: str, charge: int=100, storage:str = "128 Gb", status:str = "working"):
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