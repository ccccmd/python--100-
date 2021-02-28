# -*- coding:utf-8 -*-
# 输出9*9乘法口诀表

# 1 * 1 = 1
# 1 * 2 = 2 2 * 2 = 4

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %d" %(i, j, i*j), end="  ")
    print()