# -*- coding:utf-8 -*-
# python实现两个矩阵相加
X = [[1, 2, 3],
     [2, 3, 4],
     [3, 4, 5]]
Y = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
for i in range(len(X[0])):
    for j in range(len(X)):
        X[i][j] += Y[i][j]
print(X)
