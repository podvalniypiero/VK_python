# Функция `map()` изначально принимает два аргумента: функцию и последовательность.
# Она применяет переданную функцию к каждому элементу в последовательности и возвращает новую последовательность
# с примененными значениями. Для реализации данной функции в Python, нужно создать генераторную функцию,
# которая будет принимать ту же структуру аргументов. Внутри этой функции мы должны итерироваться по элементам
# последовательности, применять функцию к каждому элементу и использовать ключевое слово `yield`
# для генерации нового значения.
def map(func, seq):
   for item in seq:
       yield func(item)

func_in, seq_in = eval(input()), eval(input())

for x in map(func_in, seq_in):
   print(x)