# def average(string):
#     str = string.split(" ")
#     str = list(map(int, str))
#     avg = sum(str) / len(str)
#     return avg
#
# input = input()
# while input != '':
#     avg = average(input)
#     print(avg)
#     input = str(input())

def average(numbers):
    numbers_list = numbers.split()
    numbers_list = list(map(int, numbers_list))
    sum_numbers = sum(numbers_list)
    avg = sum_numbers / len(numbers_list)
    return avg
input_string = input()
while input_string != '':
    avg = average(input_string)
    print(avg)
    input_string = input()


