#Перед вам класс ContextDictionary, в котором уже реализованы несколько методов:
# __init__: в нем объявлен атрибут self.dictionary, который равен None
# put(self, key, value), который кладет значение value по ключу key в self.dictionary, когда этот атрибут является словарем, то есть в контексте with
# get(self, key), который забирает значение по ключу key в self.dictionary, когда этот атрибут является словарем, то есть в контексте with
# Вам нужно дополнить его, реализовав магические методы контекста:
# __enter__: здесь во время контекста наш атрибут self.dictionary превращается в словарь
# __exit__: в нем атрибут self.dictionary вновь равен None
# Таким образом мы хотим смоделировать поведение класса в контексте with.

class ContextDictionary:
    def __init__(self):
        self.dictionary = None

    def __enter__(self):
        self.dictionary = {}

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dictionary = None

    def put(self, key, value):
        self.dictionary[key] = value

    def get(self, key):
        return self.dictionary[key]
# context_dictionary = ContextDictionary()
# with context_dictionary:
#     context_dictionary.put(2,3)
#     print(context_dictionary.get(2))
# print(context_dictionary.dictionary is None)

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
