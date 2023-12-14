a = 1
a += 2
a -= 1
a *= 3
a /= 3

print(a)
print(abs(-3.25))
print(min(1,2,33,-10))
print(max(1,2,33,-10))

print("Деление нацело 5//2:", 5//2)
print(round(4.5))
print("Остаток от деления (mod) 5 mod 2:", 5%2)
print("Возведение в степень 2^10:", 2**10)

# Побитовые операции
print("Побитовое ИЛИ 01 ИЛИ 10, сложение каждого бита:", 1 | 2 )
# Оператор OR ЭТО ДРУГОЕ
print(1 or 2)

import math
# ceil округлит к большему целому, а floor – к меньшему
print(math.ceil(3.14), math.floor(3.67))

from math import log,exp
from math import e as exp_const
print(log(exp_const**10), log(exp(10)))

# STRING
print("abc" + "123")
print("Maxa" * 3)
a = (
    "Python "
    "is "
    'exciting'
)
print(a)
print(a[0], a[4])
print(a[0:4])
print(len(a))

for symbol in a[6:13:2]:
    print(symbol)

print( "is" in a)
print( "Is" in a)
print(a.split(" "))
print(a.replace("exciting", "a must"))
print(a.lower())
print(a.upper().isupper())
print(a.find("i"))

#FORMATTING DATA: %s %d, {}, {var} + f functional strings
print("Hello, %s %d" % ("Maria", 22))
print("Hello, {} {}".format("Maria", 22))

var1 = "Maria"
var2 = 22
print(f"Hello, {var1} {var2}")

#FORMATTING NUMBERS
# :fill align sign # 0 width sep .precision type
var = 123
print(f"{12000:+,}")
print(f"{12000:+,}")

print(f"{3:$=+5}") #5 это длина желаемой строки, $ это чем дополняем до длины 5, в 5 входит знак +

print(f"{3:$>+5}") # > это дополнить СЛЕВА
print(f"{3:$<+5}")
print(f"{3:+05}")
print(f"{3:05}")

#TYPE
# b — binary
# o — octal
# x or X — hex
# '#' — special mod ( add 0b, 0o, 0x or 0X to start)

i = 13
print(f"Binary: {i:b}, octal: {i:o}, hex: {i:x} or {i:X}")
print(f"With modificators: Binary: {i:#b}, octal: {i:#o}, hex: {i:#x} or {i:#X}")

a = 123.456
print(f"{a:.2f}") # length of number
print(f"{a:.1f}")
print(f"{a:.0f}")

print(f"{a:10.2f}") # выравнивание строки до 10 символов - по умолчанию строка дополнится пробелами
print(f"{a:#>10.2f}") # дополнит строку # слева до 10 символов
print(f"{a:0<10.2f}") # дополнит строку НУЛЯМИ СПРАВА до 10 символов

print(f"{a:.0e}") #EXPоненциальный формат
print(f"{a:.2e}")
print(f"{a:.0g}") #Научный формат
print(f"{a:.2g}") 