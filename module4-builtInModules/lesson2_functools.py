# 2 - module functools

import functools
import time

def lt(a, b):
    return a < b
lt_fixed = functools.partial(lt, b=0) # делать f  с меньшим числом аргументов и fix количеством параметров

# декоратор запоминания lru_cache()
# запоминать результаты выполнения f при вызове с тем же набором параметров
@functools.lru_cache()
def sum_nums(n):
    s = 0
    for i in range(n):
        s += i
    return s
@functools.total_ordering
# применяется именно к классу, а не к методам
# достаточно определить методы == и <
class Counter:
    def __init__(self, count):
        self.count = count
    def __eq__(self, other):
        return self.count == other.count
    def __lt__(self, other):
        return self.count < other.count

if __name__ == '__main__':
    print(lt_fixed(-1)) # a, сравниваем с b=0 => True/False

    #добавим временные метки, чтобы посмотреть, что f запоминает в lru_cache()
    start = time.time()
    sum_nums(1000000)
    print(time.time() - start)

    start = time.time()
    sum_nums(1000000)
    print(time.time() - start)

    # декоратор total_ordering, можем делать любые операции сравнения, прописав 2 из них
    print(Counter(2) >= Counter(2))
    print(Counter(2) <= Counter(-2))
    print(Counter(2) != Counter(-2))
