# Классы: магические методы
# Группы:
# 1 - сравнение
# 2 - арифметики
# 3 - представления
# 4 - вызова
# 5 - контекста
a = 3
b = 1
if __name__ == '__main__':
    print(a == b)
    print(a.__eq__(b)) # ==

    print(a > b)
    print(a.__gt__(b))

    print(a + b)
    print(a.__add__(b))

class Counter:
    def __init__(self, count):
        self.count = count
    def increment(self):
        self.count += 1
    def get(self):
        return self.count
    def __str__(self): # метод группы представления
        return(f"Counter with count of {self.count}")

    # методы группы сравнения
    def __eq__(self, other):
        return self.count == other.count

    def __lt__(self, other):
        return self.count < other.count
    # методы группы арифметики
    def __add__(self, other):
        return self.count + other.count
    def __sub__(self, other):
        return self.count - other.count
    def __mul__(self, other):
        return self.count * other.count

    # метод вызова
    def __call__(self, *args, **kwargs):
        self.increment()

    # методы группы контекста
    def __enter__(self): # когда необходимо сделать какое-то действие В КОНТЕКСТЕ
        self.count = 1000 # действие
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.count = 0

if __name__ == '__main__':
    print(Counter(2))
    print(Counter(3) == Counter(2))
    print(Counter(3) < Counter(2))
    print(Counter(3) + Counter(2))
    print(Counter(3) - Counter(2))
    print(Counter(3) * Counter(2))

    # call можно вызвать экземпляр класса как f
    counter = Counter(5)
    counter()
    print(counter) # Counter with count of 6

    with counter: # значение counter в блоке with В КОНТЕКСТЕ
        print(counter) # Counter with count of 1000

    # значение counter при выходе ИЗ КОНТЕКСТА
    print(counter) # Counter with count of 0
