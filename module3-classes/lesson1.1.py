# Реализуйте 3 метода в классе “Counter”:
# __init__(self, initial_count) - Этот метод нужен для инициализации класса с изначальным параметром “изначальный подсчет”
# increment(self) - Этот метод должен делать +1 к нашему счетчику подсчетов
# get(self) - Этот метод должен возвращать подсчет

class Counter:

    def __init__(self, initial_count):
        self.initial_count = initial_count
    def increment(self):
        self.initial_count +=1
    def get(self):
        return self.initial_count

    # counter = Counter(0)
    # counter.increment()
    # print(counter.get())

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)