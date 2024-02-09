import numpy as np
import statistics

math_grades = [85, 90, 78, 92, 88, 85, 76, 98, 94, 87]
std_dev = np.std(math_grades, ddof=1)
print("Выборочное стандартное отклонение оценок студентов по математике:", std_dev, round(std_dev, 3))

std_dev_ = np.std(math_grades)
print("Выборочное стандартное отклонение оценок студентов по математике:", std_dev_, round(std_dev_, 3))

std_st = statistics.stdev(math_grades)
print("Выборочное стандартное отклонение оценок студентов по математике:", std_st, round(std_st, 3))

mean = np.mean(math_grades)
print("Выборочное среднее арифметическое оценок студентов по математике:", mean, round(mean, 1))

mean_st = np.mean(math_grades)
print("Выборочное среднее арифметическое оценок студентов по математике:", mean_st, round(mean_st, 1))

median = np.median(math_grades)
print("Выборочная медиана оценок студентов по математике:", median, round(median, 1))
