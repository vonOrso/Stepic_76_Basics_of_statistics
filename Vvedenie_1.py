import defs
import numpy

# # 1.5.4
# vibor = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
# n = len(vibor)
# sredn = sum(vibor)/n
# disp = sum([(i-sredn)**2 for i in vibor])/(n-1)
# srednekvadr = disp**0.5
# print(srednekvadr)

# # 1.7.2
# isp = 186.2
# m = 175
# se = 8
# z = (isp - m) / se
# print(z)

# # 1.8.2
# disp = 4
# sd = disp**0.5
# n = 100
# se = sd/(n**0.5)
# print(se)

# # 1.9.4
# m = 10
# sd = 5
# n = 100
# se = sd/(n**0.5)
# interval = 2.58*se
# print(m - interval, m + interval)

# # 1.10.3
# m1 = 18.5
# m2 = 20
# sd = 4
# n = 64
# se = sd/(n**0.5)
# interval = 1.96*se
# print(m1 - interval, m1 + interval)
# print(m2 - interval, m2 + interval)

# # 1.10.6
# sd = 9
# m = 115
# n = 144
# znach = 118
# print(defs.p_value(defs.z_int(znach,m,defs.se(sd,n))))

# # 2.2.3
# m = 89.9
# sd = 11.3
# n = 20
# k = 2.093
# interval = k*sd/(n**0.5)
# print(m-interval,m+interval)

# # 2.2.4
# m1, m2 = 45, 34
# sd1, sd2 = 9, 10
# n = 100
# se = (((sd1**2)/n)+((sd2**2)/n))**0.5
# t = (m1 - m2) / se
# step_svobod = 100+100-2
# print(t)

# # 3.1.5
# x = [4,5,2,3,1]
# y = [2,1,4,3,5]
# print(numpy.corrcoef(x, y)[0, 1])

# # 3.3.3
# mx, my = 15, 10
# dx, dy = 25, 36
# rxy = 0.25
# sdx = defs.sd(dx)
# sdy = defs.sd(dy)
# b1 = (sdy/sdx) * (rxy)**0.5
# print(b1)

# # 3.7.2
# hsgrad = 62
# poverty = 64.78 - 0.62 * hsgrad
# print(poverty)

'''
Это просто построение трехмерного графика из первой лекции разделе 3.8
код взят из комментариев и автору поставлен лайк
что бы график можно было "покрутить" надо убрать галочку с:
File -> Settings -> Tools -> Python Scientific -> Show plots in tool window
'''
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# data = pd.read_csv('http://d396qusza40orc.cloudfront.net/statistics/lec_resources/states.csv')
# data_crop = data[['white', 'hs_grad', 'poverty']]
# data_crop.head()
# white, hs_grad, poverty = [column for column in data_crop.values.T]
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(xs=white, ys=poverty, zs=hs_grad)
# ax.set_xlabel('White(%)')
# ax.set_ylabel('Poverty(%)')
# ax.set_zlabel('Higher education(%)')
# plt.show()

# # 3.8.3
# cost = 10
# books = 8
# receipts = 150
# promotion = (receipts-7.68 - 3.66*cost - 0.82*books)/7.62
# print(promotion)

# # 3.9.3
# print(68.7 - 0.06*50 - 0.05*80 - 0.57*90)

