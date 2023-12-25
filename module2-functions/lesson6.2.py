# Написать функцию get_indexes которая принимает два списка и возвращает список индексов,
# в которых элемент из первого списка меньше элемента из второго списка по данному индексу.
# Желательно проходиться сразу по двум массивам одновременно (вспомните функцию zip).
# Для нахождения индексов можно использовать enumerate вместе с zip.

from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    indexes = []
    for index, (num1, num2) in enumerate(zip(nums1, nums2)):
        if num1 < num2:
            indexes.append(index)
    return indexes

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)