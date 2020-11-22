'''
Вносимые параметры
vibor - выборка
m - среднее
disp - дисперсия
znachenie - значение, которое необходимо рассчитать
sd - среднеквадратическое отклонение
n - кол-во элементов выбоки
se - стандартная ошибка среднего
'''
from scipy import stats
import numpy as np



# Расчет среднего
def m(vibor):
    return sum(vibor)/len(vibor)

# Дисперсия
def disp(m, vibor):
    return sum([(i - m) ** 2 for i in vibor]) / (len(vibor) - 1)

# среднеквадратическое отклонение
def sd(disp):
    return disp**0.5

# z интервал
def z_int(znachenie, m, se):
    return (znachenie - m) / se

# стандартная ошибка среднего
def se(sd, n):
    return sd / (n ** 0.5)

# 95% интервал
def int_95(se):
    return 1.96*se

# 99% интервал
def int_99(se):
    return 2.58 * se

# Расчет значения p
def p_value(z_stat, alternative='two-sided'):
    if alternative == 'two-sided':
        return 2 * (1 - stats.norm.cdf(np.abs(z_stat)))

    if alternative == 'less':
        return stats.norm.cdf(z_stat)

    if alternative == 'greater':
        return 1 - stats.norm.cdf(z_stat)

