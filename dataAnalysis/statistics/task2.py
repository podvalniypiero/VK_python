from scipy.stats import mannwhitneyu

algorithm_a_times = [3.2, 5.1, 4.3, 6.7, 7.9, 4.8, 5.6, 6.2, 5.9]
algorithm_b_times = [2.9, 4.5, 6.1, 5.8, 4.2, 5.3, 4.7, 6.5, 6.8]

statistic, p_value = mannwhitneyu(algorithm_a_times, algorithm_b_times, alternative='two-sided')

print('Значение статистики:', statistic, 'Значение p-value:', p_value)

# Если p-value < выбранного уровня значимости (обычно 0.05), то отвергаем нулевую гипотезу
# в пользу альтернативной, и можем сделать вывод о наличии статистически значимой разницы в производительности алгоритмов.