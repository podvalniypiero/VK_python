# Напишите функцию g вложенную в f, в которой переменная b типа int, полученная со стандартного ввода
# в объемлющей области видимости увеличивается на 10.

def g():
   b = int(input())
   def h():
       nonlocal b
       b += 10
   h()
   print(b)
g()