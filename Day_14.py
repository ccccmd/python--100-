# -*- coding:utf-8 -*-
# 将一个正整数分解质因数

num = int(input("请输入一个正整数"))
sum = 2
while num != 1:
    if num % sum == 0:
        print(sum, end="  ")
        num = int(num / sum)
    else:
        sum = sum + 1