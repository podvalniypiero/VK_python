#Python 3.7.4
def validate_input(arr):
    letters = []
    numbers = []
    # анализ того, что пришло на вход от пользователя, сколько букв и сколько цифр
    # возвращает boolean, равно ли количество букв количеству цифр

    for item in arr:
        if item.isalpha():
            letters.append(item)
        elif item.isdigit():
            numbers.append(item)
        else:
            return False

    return len(letters) == len(numbers)


def alternate(arr):
    letters = []
    numbers = []

    for item in arr:
        if item.isalpha():
            letters.append(item)
        elif item.isdigit():
            numbers.append(item)

    result = []
    for i in range(len(letters)):
        result.append(letters[i])
        result.append(numbers[i])

    return result

print("""\n\t\t||Здравствуйте, это программа, анализирующая введённый массив из букв и цифр||
||Программа преобразует введенный массив таким образом, что буквы и цифры в нем чередуются, начиная с буквы||\n""")

N = input("Введите количество элементов массива, число должно быть целым положительным и четным: ")
arr = []
# блок кода с необходимыми для корректной работы программы проверками
if not (N.isdigit()):
    print("Это должно быть число!")
elif (int(N) <= 0):
    print("Количество элементов в массиве должно быть неотрицательным числом!")

elif (int(N))%2:
    print("Количество элементов в массиве должно быть четным!")

else:
    print("Отлично, количество элементов в массиве:", N)
    N = int(N)
    for _ in range(N):
       arr.append(input("Введите элемент массива: "))

if validate_input(arr):
    result_arr = alternate(arr)
    print("Результирующий массив:", result_arr)
else:
    print("Количество букв и цифр должно быть равным!")
