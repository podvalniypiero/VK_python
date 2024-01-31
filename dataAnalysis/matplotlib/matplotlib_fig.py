# -*- coding: utf-8 -*-
# Matplotlib - библиотека 2D графики (линейные графики, точечные диаграммы, гистограммы и круговые диаграммы)
# модуль pyplot - отображение разных графиков
# Корректное отображение графиков прямо в jupyter'e
# Все функции matplotlib API, в частности plot и close, находятся в модуле matplotlib.pyplot
# Корректное отображение графиков прямо в jupyter'e

# Все функции matplotlib API, в частности plot и close, находятся в модуле matplotlib.pyplot

import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
# FIGURE() - построить график
#1
fig = plt.figure()
ax1 = fig.add_subplot(221) #1ый подграфик
ах2 = fig.add_subplot(222) #2ой подграфик
ax3 = fig.add_subplot(223) #3ий подграфик
ax4 = fig.add_subplot(224) #4ый подграфик

plt.show()
plt.close()

#2
fig = plt.figure()
ax1 = fig.add_subplot(221) # обращаемся к 1ому под-графику исходя их того что у него сетка состоит из 2 строк и 2 столбцов
ах2 = fig.add_subplot(222) # обращаемся к 2ому под-графику исходя их того что у него сетка состоит из 2 строк и 2 столбцов
ax3 = fig.add_subplot(212) # обращаемся к 2ому под-графику при этом исходя из того что 2 строки и 1 столбец (основание шире)


plt.show()
plt.close()

#3
fig = plt.figure()
ax1 = fig.add_subplot(221) # 2 строки, 2 столбца
ах2 = fig.add_subplot(122) # 1 строка, 2 столбца (выше)
ax3 = fig.add_subplot(223)

plt.show()
plt.close()
