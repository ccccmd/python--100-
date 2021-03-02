# -*- coding:utf-8 -*-
# 求n的阶乘
def jiecheng(n):
    if n != 1:
        return n * jiecheng(n - 1)
    else:
        return 1

n = input()
print(jiecheng(n))