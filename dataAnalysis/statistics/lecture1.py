# Выборка, генеральная совокупность, статистические меры

import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
import pandas as pd

np.random.seed(1234)
# два наших теоретических распределения генеральных совокупностей (в реальной жизни обычно к ним у нас доступа не бывает)
# 1 - Пример формирования генеральной совокупности с нормальным распределением.
norm_rv1 = stats.norm(loc=35, scale = 10)
# scale - стандартное отклонение
# loc - среднее

#генерирует случайные значения из распредления norm_rv1
gen_pop = norm_rv1.rvs(size=10000)

fig = plt.figure(figsize=(14, 7))
ax1 = plt.subplot(111)
plt.hist(gen_pop, 50, alpha=0.5)
plt.show()

# 2 - Пример с логнормальным распредлением.
ln_distrib = stats.lognorm(0.5, loc = 25, scale = 10)
gen_pop_ln = ln_distrib.rvs(size=10000)

fig = plt.figure(figsize=(14, 7))
ax1 = plt.subplot(111)
plt.hist(gen_pop_ln, 100, alpha=0.5)
plt.show()

#Описательная статистика
# Меры концентрации:
# Медиана — это такое число выборки, что ровно половина из элементов выборки больше него,
# а другая половина меньше него.
median = np.median(gen_pop)
median_ln = np.median(gen_pop_ln)

fig = plt.figure(figsize=(20, 10))
ax1 = plt.subplot(111)
plt.hist(gen_pop, 50, alpha=0.8)
line1 = plt.axvline(median, label=('Медиана = '+ str(round(median, 1))),
                    color='blue', linestyle='dashed', linewidth=3.5)

ax1.legend(handles=[line1], fontsize = 20)
plt.show()


fig = plt.figure(figsize=(20, 10))
ax1 = plt.subplot(111)
plt.hist(gen_pop_ln, 50, alpha=0.8)
line1 = plt.axvline(median_ln, label=('Медиана = '+ str(round(median_ln, 1))),
                    color='blue', linestyle='dashed', linewidth=3.5)

ax1.legend(handles=[line1], fontsize = 20)
plt.show()

# Мода — значение во множестве наблюдений, которое встречается наиболее часто.
dscrt_lst = np.random.randint(0,100,size = 1000)

fig = plt.figure(figsize=(24, 6))
ax1 = plt.subplot(121)
plt.hist(dscrt_lst, 100, alpha=0.8)
plt.show()
mode = stats.mode(dscrt_lst)
print(mode)

#Квантиль — значение, которое заданная случайная величина не превышает с фиксированной вероятностью.
# Если вероятность задана в процентах, то квантиль называется процентилем или перцентилем.

print(np.percentile(gen_pop, 75))
print(stats.scoreatpercentile(gen_pop, 75))

df_box_plot = pd.DataFrame()
df_box_plot['gen_pop'] = gen_pop
df_box_plot['gen_pop_ln'] = gen_pop_ln

fig = plt.figure(figsize=(20, 10))
sns.boxplot(data=df_box_plot, orient="h")
plt.show()

# Среднее арифметическое
# При работе с генеральной совокупностью данных:
# среднее - 𝜇 =1𝑁∑𝑁𝑖=1(𝑥𝑖), где N - объем генеральной совокупности.

mean = np.mean(gen_pop)
print(mean)

# При работе с выборкой меры концентрации начинают называться выборочными, потому что оценку меры мы производим по выборке.
# выборочное среднее - НЕ 𝑋=1/𝑛∑𝑛 𝑖=1 (𝑥𝑖), здесь n - объем выборки.
n = 20
sample = np.random.choice(gen_pop, n, replace = False)
sample_mean = np.mean(sample)
print(sample_mean)

# Границами ящика служат первый и третий квартили (25-й и 75-й процентили соответственно),
# линия в середине ящика — медиана (50-й процентиль).
# Концы усов — края статистически значимой выборки (без выбросов),
# и они могут определяться несколькими способами.
# Наиболее распространённые значения, определяющие длину «усов»:
#
# Минимальное и максимальное наблюдаемые значения данных по выборке (в этом случае выбросы отсутствуют);
# Разность первого квартиля и полутора межквартильных расстояний; сумма третьего квартиля и полутора межквартильных расстояний.

# Меры разброса
#
# Для генеральной совокупности данных:
#
# дисперсия -  𝜎2=1/𝑁 ∑𝑁 𝑖=1(𝑥𝑖−𝜇)^2
#
# среднеквадратическое отклонение -  𝜎= sqrt(1/𝑁 ∑𝑁 𝑖=1(𝑥𝑖−𝜇)^2)

#дисперсия
var_ = np.var(gen_pop)
print(var_)
#среднеквадратическое отклонение
std_ = np.std(gen_pop)
print(std_)

# Оценка среднеквадратического отклонения через выборочное среднеквадратическое отклонение:
#
# 𝑆=sqrt(1/𝑛−1 ∑𝑛 𝑖=1(𝑥𝑖− НЕ 𝑋)^2)
#
# По интуиции - разброс значений в пределах выборки никогда не бывает столь большим, как во всей совокупности,
# и деление не на n, а на n – 1 компенсирует возникающее занижение оценки стандартного отклонения.
std_sample = np.std(sample,
                    ddof = 1)
print(std_sample)

iterations = 1000
n = 20

std_sample_l = []
std_sample_l_corrected = []

for i in range(iterations):
    sample = np.random.choice(gen_pop, n, replace=False)
    std_sample = np.std(sample)
    std_sample_corrected = np.std(sample, ddof=1)

    std_sample_l.append(std_sample)
    std_sample_l_corrected.append(std_sample_corrected)


fig = plt.figure(figsize=(20, 10))

ax1 = plt.subplot(111)
plt.hist(std_sample_l, alpha=0.5, bins = 30)
plt.hist(std_sample_l_corrected,  alpha=0.5, bins = 30)

line1 = plt.axvline(std_, color='black', linestyle='dashed', linewidth=4.5,
                    label = 'std генеральной совокупности')
line2 = plt.axvline(np.mean(std_sample_l), color='blue', linestyle='dashed', linewidth=4.5,
                    label = 'std выборки')
line3 = plt.axvline(np.mean(std_sample_l_corrected), color='orange', linestyle='dashed', linewidth=4.5,
                   label = 'std выборки скорректированное')

plt.legend() #описание на графике
plt.show()

# Стандартная ошибка среднего в математической статистике — величина, характеризующая
# стандартное отклонение выборочного среднего, рассчитанное по выборке размера n из генеральной совокупности.
#
# истинная стандартная ошибка - 𝜎𝑥¯=𝜎/sqrt(𝑁)
# оценка стандартной ошибки по выборке - 𝑆𝑥¯=𝑆/sqrt(𝑛)
n = 20
sample = np.random.choice(gen_pop, n, replace = False)
#оценка стандартной ошибки по выборке
print(stats.sem(sample))

fig = plt.figure(figsize=(10, 5))
ax1 = plt.subplot(111)
plt.hist(gen_pop, 50, alpha=0.8)
line1 = plt.axvline(mean, label=('Среднее = '+ str(round(mean, 1))),
                    color='blue', linestyle='dashed', linewidth=3.5, alpha = 0.4)
ax1.legend(handles=[line1], fontsize = 15)
plt.show()


n = 100
for i in range(5):
    sample = np.random.choice(gen_pop, n, replace = False)
    sample_mean = np.mean(sample)
    sem = stats.sem(sample)
    fig = plt.figure(figsize=(8, 4))

    ax1 = plt.subplot(111)
    plt.hist(sample, 20, alpha=0.8)
    line1 = plt.axvline(sample_mean, label=('Выборочное среднее = '+ str(round(sample_mean, 1))),
                        color='blue', linestyle='dashed', linewidth=3, alpha = 0.4)
    line2 = plt.axvline(mean, label=('Истинное среднее = '+ str(round(mean, 1))),
                        color='orange', linestyle='dashed', linewidth=3, alpha = 0.4)
    line3 = plt.axvline(mean, label=('Выборочная стандартная ошибка среднего = '+ str(round(sem, 1))),
                        color='black', linestyle='dashed', linewidth=3, alpha = 0.0)
    ax1.legend(handles=[line1, line2, line3], fontsize = 10)
    plt.show()

# Чем больше выборка, тем точнее оценка среднего и тем меньше его стандартная ошибка.
# Чем больше изменчивость исходной совокупности, тем больше изменчивость выборочных средних, поэтому
# стандартная ошибка среднего возрастает с увеличением стандартного отклонения совокупности.

# В отличие от стандартного отклонения стандартная ошибка среднего ничего не говорит о разбросе данных,
# — она лишь показывает точность выборочной оценки среднего.

# Свойства статистических оценок
# Оценка называется несмещенной, если ее математическое ожидание равно истинному значению оцениваемого параметра.
#
# Более слабым условием является асимптотическая несмещенность, которая означает, что математическое ожидание
# оценки сходится к истинному значению параметра с ростом объема выборки.
#
# Будем использовать генеральную совокупность со средним:
iterations = 5000
n = 20

std_sample_l = []
std_sample_l_corrected = []

est = []
est_1 = []

for i in range(iterations):
    sample = np.random.choice(gen_pop, n, replace=False)
    std_sample = np.std(sample)
    std_sample_corrected = np.std(sample, ddof=1)

    std_sample_l.append(std_sample)
    std_sample_l_corrected.append(std_sample_corrected)

    if i % 20 == 0:
        est.append(np.abs(np.mean(std_sample_l) - std_))
        est_1.append(np.abs(np.mean(std_sample_l_corrected) - std_))
fig = plt.figure(figsize=(12, 6))
plt.plot(est)
plt.plot(est_1)
plt.show()
# Состоятельность – при бесконечном расширении выборки оценка приходит к истинному значению.
est = []
for i in range(10,5000, 10):
    sample = np.mean(np.random.choice(gen_pop, i, replace = False))
    est.append(sample)
plt.figure(figsize=(14,8))
plt.plot(est, c='grey', alpha = 0.5)
plt.hlines(mean, 0, 500, color='blue', lw=2, label = 'среднее генеральной совокупности')
plt.xlabel('количество наблюдений * 10', size=12)
plt.legend()
plt.show()

#Пример несостоятельной оценки:
est = []
for i in range(10,5000, 10):
    sample = np.mean(np.random.choice(gen_pop, i, replace = False)) * (np.sqrt(i)/i) + 30
    est.append(sample)
plt.figure(figsize=(9,5))
plt.plot(est, c='grey', alpha = 0.5)
plt.hlines(mean, 0, 500, color='blue', lw=2, label = 'среднее генеральной совокупности')
plt.xlabel('количество наблюдений * 10', size=12)
plt.legend()
plt.show()

# Несмещенная оценка называется эффективной среди рассматриваемых оценок, если она имеет
# минимальную дисперсию.
#
# Опять будем оценивать среднее генеральной совокупности по выборке:
#
# 𝜃1=1/𝑛 ∑𝑛 𝑖=1 (𝑥𝑖)
# 𝜃2=𝑀𝑒(𝑥𝑖)
n = 20
est_1 = []
est_2 = []

for i in range(1000):
    est_1.append(np.mean(np.random.choice(gen_pop, n, replace=False)))
    est_2.append(np.median(np.random.choice(gen_pop, n, replace=False)))

df_box_plot_est = pd.DataFrame()
df_box_plot_est['est_1'] = est_1
df_box_plot_est['est_2'] = est_2

fig = plt.figure(figsize=(12, 6))
sns.boxplot(data=df_box_plot_est, orient="h", showmeans=True)
plt.show()
mean_1 = np.mean(est_1)
mean_2 = np.mean(est_2)

print(f'Среднее по выборкам оценки 1 - {round(mean_1,1)}')
print(f'Среднее по выборкам оценки 2 - {round(mean_2,1)}')

var_1 = np.var(est_1)
var_2 = np.var(est_2)

print(f'Дисперсия по выборкам оценки 1 - {round(var_1,1)}')
print(f'Дисперсия по выборкам оценки 2 - {round(var_2,1)}')

# Обе оценки состоятельны и несмещенные, при этом оценка среднего генеральной совокупности через
# среднее является эффективной оценкой, так как дисперсия первой оценки меньше.
#
# При этом, если требуется сравнить оценки, которые не обязательно являются несмещенными,
# то вычисляют величину MSE (среднеквадратическую ошибку). Эффективной в этом случае называют ту оценку,
# у которой MSE минимальна.
#
# 𝑀𝑆𝐸= (∑𝑛 𝑖=1 (𝜃̂−𝜃)^2 )/𝑛
#
# Для несмещенных оценок MSE совпадает с дисперсией.

# Эмпирические функции распределения cdf и pdf
# Для работы с оценкой статистических критериев используется ряд функций:
#
# pdf - функция плотности вероятности - показывает вероятность распредления случайной величины;
# cdf - это кумулятивная функция распределения дает интегральную картину распределения вероятности,
# задает вопрос: «Какова вероятность того, что результат окажется меньше или равен такому-то?».
fig = plt.figure(figsize=(14, 6))
x = np.linspace(gen_pop.min(), gen_pop.max(), 100)
mu = gen_pop.mean()
sigma = gen_pop.std()
y_pdf = stats.norm.pdf(x, mu, sigma)
y_cdf = stats.norm.cdf(x, mu, sigma)

plt.plot(x, y_cdf, label='cdf', color = 'r')
plt.legend()
plt.twinx()
plt.plot(x, y_pdf, label='pdf', color = 'b')
plt.legend()
plt.show()