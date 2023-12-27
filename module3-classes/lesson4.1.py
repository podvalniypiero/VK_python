# В классе Dictionary реализуйте методы __call__ и __init__:
# В __init__(self, dictionary) объявите словарь в качестве атрибута
# В методе call реализуйте поиск в словаре по ключу

class Dictionary:
   def __init__(self, dictionary):
       self.dictionary = dictionary

   def __call__(self, key):
       return self.dictionary[key]

   # dictionary = Dictionary({1: 2, 2: 1, 3: 3})
   # print(dictionary(1))

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)