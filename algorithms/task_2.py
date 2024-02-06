# Считываем входные данные
N = int(input("Введите число N: "))
numbers = list(map(int, input("Введите числа из колоды: ").split()))

# Вычисляем сумму всех чисел из колоды
total_sum = sum(numbers)

# Вычисляем сумму всех возможных чисел от 1 до N
expected_sum = (N * (N + 1)) // 2 * 4

# Находим разницу между суммой всех возможных чисел и суммой чисел из колоды
missing_number = expected_sum - total_sum

print("Число на потерянной карте:", missing_number)