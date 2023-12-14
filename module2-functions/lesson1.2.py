def process_string(string):
# Проверяем первый символ строки
    if string.startswith("!"):
# Если первый символ "!", приводим строку к верхнему регистру
        string=string[1:].upper()
    else:
# Иначе приводим строку к нижнему регистру
        string=string.lower()
# Удаляем символы "!@#%"
    string = ''.join(char for char in string if char not in "!@#%!")
    return string

input_string = input()
while input_string != '':
    res = process_string(input_string)
    print(res)
    input_string = input()
