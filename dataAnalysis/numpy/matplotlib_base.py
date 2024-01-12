# -*- coding: utf-8 -*-
# Matplotlib - библиотека 2D графики (линейные графики, точечные диаграммы, гистограммы и круговые диаграммы)
# модуль pyplot - отображение разных графиков
# Корректное отображение графиков прямо в jupyter'e
# Все функции matplotlib API, в частности plot и close, находятся в модуле matplotlib.pyplot
# Корректное отображение графиков прямо в jupyter'e

# Все функции matplotlib API, в частности plot и close, находятся в модуле matplotlib.pyplot
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


fig, ax = mpl.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
# FIGURE() - построить график
# fig = plt.figure()
# ax1 = fig.add_subplot(221)
# ах2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(223)
# ax4 = fig.add_subplot(224)
#
# plt.show()
# plt.close()
