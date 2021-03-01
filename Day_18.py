# -*- coding:UTF-8 -*-
# 求s=a+aa+aaa+aaaa+...的值，其中a是一个数字

from functools import reduce
n = int(input())
a = int(input())
Tn = 0
Sn = []
for i in range(n):
    Tn = Tn + a
    Sn.append(Tn)
    a = a * 10
print(Sn)
Sn = reduce(lambda x, y : x + y, Sn)
print(Sn)