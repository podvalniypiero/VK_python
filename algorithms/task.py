from scipy.optimize import linprog

# Коэффициенты функции прибыли (минимизация, поэтому знаки противоположны)
c = [-500, -1200]

# Коэффициенты ограничений
A = [[4/3, 2], [4/3, 1.5]]
b = [180, 165]

# Границы для переменных x и y
x_bounds = (0, None)  # x может быть от 0 до бесконечности
y_bounds = (0, None)  # y может быть от 0 до бесконечности

# Решение задачи линейного программирования
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Расчет максимальной прибыли
max_profit = -result.fun
max_x, max_y = result.x

print(max_profit, max_x, max_y)
