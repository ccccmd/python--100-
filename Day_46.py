# -*- coding:utf-8 -*-
# python 实现矩阵相加
import numpy as np
x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

y = np.array([[4, 5, 6],
              [7, 8, 9],
              [1, 2, 3]])

z = x + y
print(z)