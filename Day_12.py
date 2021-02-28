# -*- coding:utf-8 -*-
# 判断101-200之间有多少个素数，并输出所有素数
import math
def prim(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return 1
    return 0
sum = 0
for i in range(101, 200):
    if prim(i) == 0:
        sum = sum + 1
        print(i, end=" ")

print()
print("共有%d个素数" %sum)
