# Классы: декораторы методов
# декораторы позволяют модифицировать методы классов
# 1) декоратор property: декоратор-property и iter deleter декоратор
# 2) static метод
# 3) class метод

class Temperature:
    def __init__(self, celcius):
        self._celcius = celcius
    @property
    def celcius(self):
        return self._celcius
    @celcius.setter # можем менять логику изменений атрибутов через декоратор property и setter property метода
    def celcius(self, value):
        if value < -273:
            self._celcius = 0
        else:
            self._celcius = value

    @staticmethod # писать методы, которым
    # 1 - не нужна info в () об экземплярах классов
    # - не нужно передавать в метод ключевое слово, представляющее класс - cls или экземпляр класса - self
    # 2 - не нужно модифицировать эти экземпляры
    # можем убирать ключевое слово self из метода, если мы не хотим модифицировать класс\знать информацию о классе
    def print_temp_class():
        print("I am temperature class")

class Circle:
    pi = 3.14

    @classmethod # 1 - можем знать info об атрибутах класса
    # 2 - вызывать некоторые методы, не используя сами экземпляры классов

    def area(cls, radius):
        return cls.pi * radius ** 2

if __name__ == '__main__':
    temperature = Temperature(23)
    temperature.celcius = -10 # нежелательное присваивание атрибутов
    print(temperature.celcius)
    temperature.print_temp_class()

    circle = Circle()
    print(circle.area(2)) # получаем результат вызовом ЭКЗЕМПЛЯРА класса (без @classmethod)

    print(Circle.area(2)) # получаем результат вызовом напрямую самого МЕТОДА класса