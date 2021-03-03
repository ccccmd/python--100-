# -*- coding:utf-8 -*-
# 求100以内的素数
import math
def sushu(n):
    if n == 1 or n == 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 1
    return 0
for i in range(1, 101):
    if sushu(i) == 0:
        print(i)
        