# -*- coding:UTF-8 -*-
# 求完全数
from functools import reduce
n = int(input())
lst = []
for i in range(1, n + 1):
    for j in range(1, i):
        if i % j == 0:
            lst.append(j)
    if lst != []:
        if reduce(lambda x, y: x + y, lst) == i:
            print(i)
    lst = []

