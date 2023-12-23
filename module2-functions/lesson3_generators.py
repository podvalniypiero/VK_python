# GENERATORS
# ГЕНЕРАТОРНЫЕ ФУНКЦИИ И ГЕНЕРАТОРНЫЕ ВЫРАЖЕНИЯ - способы создания генераторов

# функции
# def create_generator(start = 0):
#     num = start
#     while True:
#         yield num
#         num += 1
#
# generator = create_generator(7) # числа будут выводиться с 7
#
# for i in generator:
#     print(i)
#     if i >= 10:
#         break
# # GENERATOR 3 чисел
# def gen_three():
#     yield 1
#     yield 2
#     yield 3
#
# # for i in gen_three():
# #     print(i)
#
# # Можем получать каждое следующее значение с помощью NEXT - итерация с помощью next
# generator = gen_three()
# print(next(generator))
# print(next(generator))
# print(next(generator))
# # print(next(generator)) если выйдем за пределы generator'a, то есть сделаем yield 4,
# # то вызовем error traceback - StopIteration
# generator_2 = gen_three() # еще один instance генератора, порождает новый генератор, который не связан с предыдущим
# print(next(generator_2))
# # цикл for работает как while+next, цикл for работает со всеми структурами, по которым можно итерироваться
#
# a = [9, 10, 11]
# it = iter(a)
# print(next(it))
# print(next(it))
# print(next(it))
# # print(next(it)) тоже будет error StopIteration
# it_new = iter(a)
# print(next(it_new)) # выведет 9, 0ой элемент
# a.insert(0, -1)
# print(next(it_new)) # выведет 9, так как в прошлой итерации выводил 0ой элемент, теперь выведет 1ый
# a.insert(0, -2)
# a.insert(0, -3)
# print(a) # [-3, -2, -1, 9, 10, 11]
# print(next(it_new)) # выведет -1, 2ой элемент
#
# # выражения
# generator = (x for x in range(20) if x % 2 == 0) # четные числа до 20
# # +++ генераторы не вычисляют все значения за раз, а делают это по одному по мере нужды,
# # => ленивые вычисления помогают экономить оперативную память
# # => если нужно проитерироваться по каким-то данным, которые по частям помещаются в память, но все вместе уже не влезают
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# # МЕТОДЫ генераторов
# # CLOSE()
# def create_generator(start = 0):
#     num = start
#     while True:
#         yield num
#         num += 1
#
# gen = create_generator()
# for i in gen:
#     print(i)
#     if i >= 7:
#         gen.close()
# # print(next(gen)) ошибка StopIteration
#
# # THROW()
# def create_generator(start = 0):
#     num = start
#     while True:
#         yield num
#         num += 1
#
# gen = create_generator()
# for i in gen:
#     print(i)
#     if i >= 5:
#         gen.throw(ValueError("Unexpected value > 5"))
# # print(next(gen))

# SEND()
def create_my_generator():
    for x in range(10):
        if x % 2 == 0:
            val = yield x**2
            print(f"`{val}` was sent to generator, current state: {x}")
        else:
            val = yield -x
            print(f"`{val}` was sent to generator, current state: {x}")
gener = create_my_generator()
first_val = next(gener)
print(first_val)

second_val = gener.send("Out val") # передает инфо в генератор и проводит похожее на next, передает следующую итерацию и возвращает результат этой операции

print(next(gener))# при вызове через next/for не удастся передать значение в генератор, как с .send() - будет 'None'
