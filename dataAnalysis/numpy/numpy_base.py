import numpy as np
datal = [ [5.2, 3.0, 4.5] , [9.1, 0.1, 0.3]]
arrl = np.array(datal)
print(arrl)

print(arrl.ndim) # 2 - число осей (измерений) массива
print(arrl.size) # 6 - количество всех элементов массива
print(arrl.shape) # (2, 3) - форма массива, кортеж N чисел
print(arrl.dtype) # float64 - объект, описывающий тип элементов массива
print(arrl.itemsize) # 8 - размер каждого элемента в байтах
print(np.zeros(10)) # массив из десяти 0
print(np.ones((2,2))) # массив 2на2 из 1

#numpy.arange(start, stop, step)
print(np.arange(15)) # массив от 0 до 14

print(np.linspace(0, 1, 25)) # массив от 0 до 1 из 25 элементов
print(np.eye(3)) # единичная матрица 3на3

# операции между массивами и скалярами
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr * arr)
print(arr - arr)
print(1/arr)
# случайные массивы
print(np.random.randn(3,2))
print(np.random.randint(0, 1000, 4)) # от 0 до 1000 4 элемента

# индексирование - похоже со списками
print(np.arange(15)[8:12]) # [ 8  9 10 11]
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2]) # [7 8 9]
print(arr2d[0, 2]) # 3
print(arr2d[0][2]) # 3

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d[1,1][2]) # 12
print(arr3d[:1,:1,1:]) # [[[2 3]]]

# булевое индексирование
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(names == 'Bob') # [ True False False  True False False False]

mask = (names == 'Bob') | (names == 'Will')
print(mask) # [ True False  True  True  True False False]
print(names[mask]) # ['Bob' 'Will' 'Bob' 'Will']

# транспонирование массивов
print(arr3d)
print(arr3d.shape) # (2, 2, 3)
print(arr3d.T)
print(arr3d.T.shape) # (3, 2, 2)

# поэлементные операции над массивами
# – векторные обертки вокруг простых функций,

# которые принимают одно или несколько скалярных значений и порождают один или несколько скалярных результатов
print(np.sqrt(arr3d)) # кв корень из каждого элемента матрицы
print(np.exp(arr3d)) # exp каждого элемента

# математические и статистические операции
arr = np.random.randn(5, 4)
print(arr)
print(arr.shape) # (5,4)
print(arr.mean) # среднее значение
print(arr.sum())
print(np.max(arr))
print(arr.sum(axis = 0)) #  сумма по 0му измерению

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr)

# кумулятивная сумма элементов по заданной оси
print(arr.cumsum(axis = 0)) # cumsum(array, axis=None, dtype=None, out=None)

# кумулятивное произведение элементов по заданной оси
print(arr.cumprod(axis = 0))

# сортировка
arr = np.random.randn(8)
print(arr)
print(arr.sort())

arr = np.random.randn(5,3)
print(arr)
arr.sort(0)
print(arr)
arr.sort(1)
print(arr)

#возвращает копию
arr = np.random.randn(5,3)
print(arr)
print(np.sort(arr))

arr = np.sort(arr)
print(arr)

# хранение массивов на диске в двоичном формате¶
# np.SAVE() и np.LOAD() - основные функции для эффективного сохранения и загрузки данных с диска в .npy.
# По умолчанию массивы хранятся в несжатом двоичном формате в файле .npy.

# np.SAVEZ() чтоб сохранить несколько массивов в zip-архив в формате .npz
arr = np.arange(10)
print(arr)
np.save('some_array', arr)
np.load( 'some_array.npy')

np.savez('array_archive.npz', a=arr, b=arr)
arch = np.load('array_archive.npz')

print(arch['b'])