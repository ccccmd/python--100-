# -*- coding:utf-8 -*-
# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第3个月后每个月又生一对
# 兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 1:1    2:1    3:2    4:3    5:5    6:8
n = int(input())
def fibonaici(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonaici(n - 1) + fibonaici(n - 2)
print(fibonaici(n))
