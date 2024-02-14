# Пайплайн проверки статистических гипотез
# Статистическая гипотеза — это некоторое предположение о свойствах генеральной совокупности, которое необходимо проверить.
#
# Проверка статистических гипотез – это процедура проверки действительны ли результаты, полученные на выборке, и для генеральной совокупности.
#
# Ошибка первого рода — ситуация, когда отвергнута правильная нулевая гипотеза (англ. type I errors, α errors, false positive, ошибочное отвержение).
#
# Ошибка второго рода — ситуация, когда принята неправильная нулевая гипотеза (англ. type II errors, β errors, false negative, ошибочное принятие). Величина 1 – β называется мощностью критерия.
# Уровень значимости — допустимая для данной задачи вероятность ошибки первого рода (ложноположительного решения, false positive), то есть вероятность отклонить нулевую гипотезу, когда на самом деле она верна.

# Статистические критерии. ANOVA - проверка гипотезы с использованием анализа дисперсии

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import itertools
import scipy
import tqdm
from scipy import stats
import random
distrib = stats.norm(loc = 35, scale = 10)
gen_pop = distrib.rvs(size=10000)

fig = plt.figure(figsize=(14, 7))
ax1 = plt.subplot(111)
plt.hist(gen_pop, 100)
plt.show()
# Извлечем из нашей совокупности 3 случайные подгруппы
# по 50 заказов в каждой - пусть это будут наблюдения, полученные в реальном эксперименте.
np.random.seed(3106)
sample_groups = []
for i in range(3):
    sample_groups.append(np.random.choice(gen_pop, size = 50).astype(int))
sample_groups = np.array(sample_groups)
sample_groups
# Рассчитаем:
#
# среднее каждой выборки и стандартное отклонение (голубые линии на графике)
# среднее средних и стандартное отклонение средних (оранжевая линия на графике)
x = np.mean(sample_groups,axis = 1)
y = np.arange(sample_groups.shape[0])
e = np.std(sample_groups,axis = 1)

fig = plt.figure(figsize=(14, 7))
plt.errorbar(x, y, xerr = e, linestyle='None', marker='o')
plt.errorbar( np.mean(x), y.shape[0] ,xerr =  np.std(x), linestyle='None', marker='o')

plt.show()
# 1) формулируются гипотезы Н0 и Н1;
#
# H0 - выборки взяты из одного распределения (средние всех выборок равны)
#
# H1 - выборки взяты из разных распределений (хотя бы пара средних различается между собой)
#
# 2) фиксируется уровень значимости критерия значимости
#
# Зададим α на уровне значимости 5%.
#
# 3)выбирается статистический критерий для проверки гипотезы;
#
# Будем использовать ANOVA.
#
# 4) по выборочным данным вычисляется значение K-наблюдаемое по распределению выбранной статистики
num_of_groups = sample_groups.shape[0]
#Рассчитаем среднее по всем наблюдениям:
X_mean = sample_groups.mean()
print(X_mean)
# Рассчитаем среднее для каждой группы
group_means = sample_groups.mean(axis = 1)
group_means_reshaped = group_means.reshape(num_of_groups, 1)

# SSW
SSW  = np.sum((sample_groups  - group_means_reshaped)**2)
print(SSW)

# SSB
group_lengths = [x.shape[0] for x in sample_groups]
SSB  = np.sum((group_means - X_mean)**2 * group_lengths)
print(SSB)

# F
m = num_of_groups
N = np.sum(group_lengths)

F = (SSB/(m-1))/(SSW/(N-m))
print(F)
# Воспользуемся пакетом stats для аналогичного расчета:
F, p = stats.f_oneway(*sample_groups)
# F-наблюдаемое
print(F)
# 5) с учетом выбранного уровня значимости вычисляется критическая область и область принятия гипотезы, то есть находится K-критическое
# F-критическое
F_critical = scipy.stats.f.ppf(q=1-.05, dfn = m, dfd = N - m)
F_critical
# 6) найденное значение K-наблюдаемое критерия сравнивается с K-критическое и по результатам сравнения делается вывод
print(F < F_critical)

# Вывод: Мы не можем отвергнуть гипотезу H0
print(p)
print(p > 0.05)

# Теперь давайте попробуем разобраться, откуда взялось распределение F, с которым мы работали.

# Будем из нашей генеральной совокупности извлекать выборки и считать F. Выборки будут также размером 50 и количество выборок будет равно 3, то есть по аналогии с тем же дизайном эксперимента, который мы проводили выше.
def calculate_random_sample_group(sz = 50):
    sample_groups = []
    for i in range(num_of_groups):
        sample_groups.append(np.random.choice(gen_pop,  size = sz))
    F, _ = stats.f_oneway(*sample_groups)
    return sample_groups, F

Fs = []
sgs = []
for i in tqdm.tqdm(range(10000)):
    sg,F = calculate_random_sample_group()
    Fs.append(F)
    sgs.append(sg)
# Распределение приняло опредленную форму, такое распредление называется распредление Фишера,
# на основе рассчитанных статистик по нему мы как раз и принимали решения.
fig, ax = plt.subplots(figsize=(10, 6))
plt.hist(Fs,bins = 100)
plt.show()