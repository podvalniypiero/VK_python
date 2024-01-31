from numpy.random import randn
import matplotlib.pyplot as plt
import numpy as np

plt.rc('figure', figsize=(3, 3))

#define list of data
data = [2, 4, 4, 5, 6, 6, 7, 8, 9, 9, 9, 10, 12, 12, 14]
# plt.hist(data) по умолчанию будет синий цвет без контура
plt.hist(data, color = "lightblue", ec="green", lw= 5) # ec-обводка, lw-ширина краев
plt.show()

#создать гистограмму из списка данных, используя указанные диапазоны интервалов
#create list of data
x = [2, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 8, 12, 13]
#specify bin start and end points
bin_ranges = [0, 5, 10, 15]
#create histogram with 4 bins
# bins - количество ячеек
plt.hist (x, bins=bin_ranges, edgecolor='black')
plt.show()

#define data
x = [1, 2, 3, 4, 5, 6]
y = [8, 13, 14, 11, 16, 22]

# .xlabel('label'), ylabel('label')
#create scatterplot with axis labels
plt.plot(x, y)
plt.xlabel('X Variable')
plt.ylabel('Y Variable')
plt.show()
#save figure to PNG file
plt.savefig('my_plot.png')


fig = plt.figure(figsize=(14,5))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(122)
ax3 = fig.add_subplot(223)

# plt.plot(randn(100).cumsum(), 'k--')

# Метод fig.add_subplot возвращает объект AxesSubplot, что позволяет рисовать в любом подrрафике, вызывая методы этого объекта:
f = ax1.hist(randn(100), bins=20, color='b', alpha=0.5) #ax1 - объект гистограммы
# color - Yellow, Blue
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30)) # scatter - гистограмма
ax3.plot(randn(100).cumsum(), 'k--') # гистограмма ---- линией

plt.show()
plt.close()

print(f) # (array([....])) - параметры, по кот нарисована гистограмма

#Отдельно данный метод тоже будет работать, так как при необходимости он автоматически создаст рисунок и подграфик
plt.plot(randn(100).cumsum()) # нарисовать график без создания f и подграфиков

fig, axes = plt.subplots(2, 3) # сетка 2 строки, 3 столбца
fig.set_figheight(5) # height фигуры в inch
fig.set_figwidth(15) # width фигуры в inch

# к каждому объекту сетки можно обращаться через индекс - axes[0,1].
axes[0,1].scatter(np.arange(30), np.arange(30) + 3 * randn(30))
axes[1,1].bar(np.arange(10),  randn(10)) # гистограмма прямоугольниками

plt.show()
print(axes) # в объекте axes 6 подграфиков

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True) # shareX, shareY - делать общими для графиков оси X, Y или нет
fig.set_figheight(5)
fig.set_figwidth(15)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(randn(500), bins=50, color= 'r', alpha=0.5)

plt.subplots_adjust(wspace=0.0, hspace=0.0) # способ задания пустого пространства вокруг графиков
plt.show()

#Обратить внимание на общую ось
fig, axes = plt.subplots(2, 2, sharex=False, sharey=False)
fig.set_figheight(5)
fig.set_figwidth(15)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(randn(500), bins=50, color= 'r', alpha=0.5)
#Достаточно популярный способ задания пустого пространства вокруг графиков
plt.subplots_adjust(wspace=0.2, hspace=0.2)
plt.show()

#Сохранение рисунка
plt.savefig('figpath.png', dpi=400, bbox_inches= 'tight')
# bbox_inches= 'tight' убирает отступы вокруг рисунка
# аргумент dpi - увеличить размер рисунка

# Конфигурирование matplotlib
plt.rc('figure', figsize=(10, 10)) #задает глобально размер рисунка

font_options = {'family' : 'monospace'}
plt.rc('font', **font_options)