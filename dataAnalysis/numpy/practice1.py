import numpy as np

array = np.arange(10,501) # массив от 50 до 100
print(array)
print(array * array - 234) # возвести каждый элемент вектора в квадрат и вычесть 234
print((array * array - 234).sum()) # сумма всех элементов такого вектора
