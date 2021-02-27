# -*- coding:utf-8 -*-
# 斐波那契数列
def fibnoici(n):
    if n == 1 or n == 2:
        return 1
    return fibnoici(n - 1) + fibnoici(n - 2)

n = input()
print(fibnoici(n))