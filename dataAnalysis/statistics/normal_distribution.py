# Нормальное распределение и Центральная предельная теорема

# Правило 3х сигм - Вероятность того, что случайная величина отклонится от своего математического ожидания
# на большую величину, чем утроенное среднее квадратичное отклонение, стремится к нулю (только для нормального распределения).
#
# ЦПТ утверждает, что выборочные средние имеют приближенно нормальное распределение независимо от
# распределения исходной совокупности, из которой были извлечены выборки
# - Среднее значение всех возможных выборочных средних равно среднему исходной совокупности.
# - Стандартное отклонение всех возможных средних по выборкам данного объема, наз. стандартной ошибкой среднего,
# зависит как от стандартного отклонения совокупности, так и от объема выборки
#
# выборочное распределение, свойства:
#
# 1. Среднее значение выборочного распределения будет равно среднему значению
# распределения генеральной совокупности:
# х = μ
# 2. Дисперсия выборочного распределения будет равна дисперсии распределения генеральной совокупности,
# деленной на объем выборки:
# с 2 = σ 2 / п

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
from scipy import stats
import numpy as np
import pandas as pd

np.random.seed(1234)
# Рассмотрим логнормальное распределение.
ln_distrib = stats.lognorm(0.5, loc = 25, scale = 10)
gen_pop_ln = ln_distrib.rvs(size=10000)

fig = plt.figure(figsize=(14, 7))
ax1 = plt.subplot(111)
plt.hist(gen_pop_ln, 100)
plt.show()

# Будем генерировать из него выборки размером 20, считать среднее.
n = 20
avg = []
for i in range(1000):
    sample = np.random.choice(gen_pop_ln, n, replace = False)
    avg.append(np.mean(sample))


import matplotlib.animation as animation
def clt(current):
    # if animation is at the last frame, stop it
    plt.cla()
    if current == 1000:
        a.event_source.stop()

    plt.hist(avg[0:current], bins=20)
    plt.annotate('Выборка = {}'.format(current), [3, 27])

fig = plt.figure()

a = animation.FuncAnimation(fig, clt, interval=10)
save_count=10000
cache_frame_data=False


a.save('clt1.gif', writer='pillow', fps=10)
