# Написать функцию changed_div, которая считает отношение делителя к частному.
# Желательно, чтобы случай с нулевым делимым должен быть обработан с помощью try-except:
# при ошибке ZeroDivisionError должен возвращаться делитель


numerator, denominator = int(input()), int(input())

def changed_div(numerator, denominator):
    try:
        res = numerator/denominator

    except ZeroDivisionError:
        res = denominator
    return res

print(changed_div(numerator, denominator))