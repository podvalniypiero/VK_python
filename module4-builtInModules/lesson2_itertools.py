# 3 - module itertools
import itertools

gen = range(10)
gen_islice = itertools.islice(gen, 2, 8, 2) # принимает любой итерируемый объект, начало, конец и шаг

# itertools.zip_longest() решает проблему zip отбрасывания хвостов,
# проходит до конца длины всех итерируемых объектов
l1 = [1, 2, 3]
l2 = [4, 5, 6, 7, 8]

if __name__ == '__main__':
    for el in gen_islice:
        print(el) # 2 4 6

    for el1, el2 in zip(l1, l2):
        print(el1, el2) # 1 4    2 5    3 6 - прошлись до min длины всех итерируемых элементов

    for el1, el2 in itertools.zip_longest(l1, l2):
        print(el1, el2) # 1 4    2 5    3 6    None 7    None 8

    # itertools.combinations(list, length)
    # возвращает все комбинации, которые можно получить из списка list длиной length
    for el1 in itertools.combinations(l1, 2):
        print(el1) # (1, 2)     (1, 3)     (2, 3)

    for el2 in itertools.combinations(l2, 3):
        print(el2)
