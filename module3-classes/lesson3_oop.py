# ООП
# 1 - Наследование – переиспользовать методы в классах – создать новый класс и отнаследоваться от предыдущего класса, его атрибуты и методы
# Наследоваться можно от класса, который на уровень выше в иерархии классов

# class Cat:
#     def __init__(self):
#         self.legs_count = 4
# class Dog:
#     def __init__(self):
#         self.legs_count = 4
class FourLegsAnimal:
    def __init__(self):
        self.legs_count = 4
class Cat(FourLegsAnimal):
    pass
class Dog(FourLegsAnimal):
    pass
# 2 - Инкапсуляция – сокрытие атрибутов от внешнего воздействия, те вне методов класса
# 3 - Полиморфизм - способность взаимодействовать с данными разных типов с разными классами,
# которые имеют общую природу, которая заложена в родительском классе

class Counter:
    def __init__(self, initial_count):
        self.count = initial_count

    def increment(self):
        self.count += 1
    def get(self):
        return self.count
class SquaredCounter(Counter): # написали super, взяли у него метод get и возвели в квадрат
    # super - ключевое слово, которое обозначает родительский класс - частично переиспользуем функциональность
    # в родительском классе, но переопределяем метод
    # super позволяет использовать родительские методы при переопределении дочерних
    def get(self):
        # return self.count ** 2
        return super().get() ** 2

class DoubleCounter:
    def __init__(self, initial_count):
        self.count = initial_count
    def double_increment(self):
        self.count += 2
class CounterWithDouble(Counter, DoubleCounter):
    pass
class CounterMixin:
    def increment(self):
        super().increment()
        super().increment()
class CounterWithMixin(CounterMixin, Counter):
    # порядок приближения методов – в 1ом приближении берется метод от самого левого предка
    pass


if __name__ == '__main__':
        # cat = Cat()
        # dog = Dog()
        # print(cat.legs_count)  # 4, атрибут legs_count и его значение подтянулись

    counter = Counter(2)
    counter.increment()
    print(counter.get())

    counter = SquaredCounter(2)
    counter.increment()
    print(counter.get())

# множественное наследование
    counter = CounterWithDouble(2)
    counter.increment()
    counter.double_increment()
    print(counter.get())

    counter = CounterWithMixin(2)
    counter.increment() # здесь метод increment используется от метода CounterMixin
    print(counter.get())




