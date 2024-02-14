# Доверительные интервалы - с их помощью получают количественную оценку (проверка гипотез - это качественная оценка)
# интервал, в пределах которого с заданной вероятностью лежат выборочные оценки статистической характеристики генеральной совокупности
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
import numpy as np
import itertools
import scipy
import tqdm
from scipy import stats
import random

# Необходимо найти доверительный интервал для времени доставки заказа курьерами.
sample = [32.8, 44.3, 29. , 23.5, 26.7, 39. , 36.2, 25.6, 37.9, 36.5, 43.8,
       59.7, 37.7, 38.4, 32.1, 28.2, 34.4, 22.1, 12.6, 26.9, 29.9, 55.5,
       34.1, 22.4, 25.4, 40. , 22.5, 38.8, 43.6, 34.4]
# Установим уровень значимости α = 5%.
import statsmodels.stats.api as sms

t = sms.DescrStatsW(sample)
print(t)
print(t.tconfint_mean(alpha=0.05, alternative='two-sided')) # доверительный интервал (30.088604935631402, 37.51139506436859) - время доставки от 30 до 38 мин

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h
# То есть, с 95% вероятностью можно утверждать, что время доставки будет от 30 до 38 минут.

print(mean_confidence_interval(sample))


# Доверительный интервал для разности средних
# Необходимо найти доверительный интервал разности времени доставки заказов курьерами на велосипедах и на самокатах.
# Установим уровень значимости α = 5%.
sample_vel = [32.8, 44.3, 29. , 23.5, 26.7, 39. , 36.2, 25.6, 37.9, 36.5, 43.8,
       59.7, 37.7, 38.4, 32.1, 28.2, 34.4, 22.1, 12.6, 26.9, 29.9, 55.5,
       34.1, 22.4, 25.4, 40. , 22.5, 38.8, 43.6, 34.4]
sample_sam = [34.2, 35.4, 53.2, 37.8, 34.6, 31.4, 35.8, 40.4, 32.4, 29.8, 30.9,
       52.5, 44. , 32.3, 39.3, 31.7, 48.3, 34.7, 41.1, 52.3, 38.8, 55.8,
       35.4, 32.3, 31.4, 37.6, 33.3, 42.9, 48.9, 39.2]
cm = sms.CompareMeans(sms.DescrStatsW(sample_vel),
                      sms.DescrStatsW(sample_sam))
print(cm.tconfint_diff(usevar='unequal'))
# C 95% вероятностью можно утверждать, что доставка заказов на велосипеде быстрее, чем на самокате от 10 до 1 минуты.

# Доверительный интервал для долей
# 1 - для доли
import statsmodels
print(statsmodels.stats.proportion.proportion_confint(400,800))
# 2 - для разницы долей
def proportions_diff_confint_ind(sample1, sample2, alpha=0.05):
    # PPF - оппределяет значение функции по заданной вероятности

    # Z-критерий имеет нормальное распределение
    z = stats.norm.ppf(1 - alpha / 2.)

    p1 = float(sum(sample1)) / len(sample1)
    p2 = float(sum(sample2)) / len(sample2)

    left_boundary = (p1 - p2) - z * np.sqrt(p1 * (1 - p1) / len(sample1) + p2 * (1 - p2) / len(sample2))
    right_boundary = (p1 - p2) + z * np.sqrt(p1 * (1 - p1) / len(sample1) + p2 * (1 - p2) / len(sample2))

    return (left_boundary, right_boundary)

survey_1 = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1,
       1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0,
       0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0,
       1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1,
       1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0]
survey_2 = [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0,
       1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1,
       0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1,
       0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0,
       1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0]
print(proportions_diff_confint_ind(survey_1, survey_2))

# 3 - Для разницы долей со связанными наблюдениями
def proportions_confint_diff_rel(sample1, sample2, alpha=0.05):
    z = stats.norm.ppf(1 - alpha / 2.)
    sample = zip(sample1, sample2)
    n = len(sample)

    f = sum([1 if (x[0] == 1 and x[1] == 0) else 0 for x in sample])
    g = sum([1 if (x[0] == 0 and x[1] == 1) else 0 for x in sample])

    left_boundary = float(f - g) / n - z * np.sqrt(float((f + g)) / n ** 2 - float((f - g) ** 2) / n ** 3)
    right_boundary = float(f - g) / n + z * np.sqrt(float((f + g)) / n ** 2 - float((f - g) ** 2) / n ** 3)
    return (left_boundary, right_boundary)


response_times = [150, 130, 140, 160, 180, 170, 190, 200, 175, 165]
t1 = sms.DescrStatsW(response_times)
print(t1)
print(t1.tconfint_mean(alpha=0.05, alternative='two-sided'))

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h
# То есть, с 95% вероятностью можно утверждать, что время доставки будет от 30 до 38 минут.

print(mean_confidence_interval(response_times))