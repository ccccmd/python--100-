# -*- coding: UTF-8 -*-
# 有四个数字1234，能组成多少个不相同且无重复数字的三位数？
sum = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if(i != j) and (i != k) and (k != j):
                print(i * 100 + j * 10 + k)
                sum = sum + 1
print("共有%d个三位数" %sum)

