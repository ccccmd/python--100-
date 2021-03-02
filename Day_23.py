# -*- coding:utf-8 -*-
# 打印菱形
mul = '*'
num = int(input("请输入菱形层数:"))
for i in range(1, int(num / 2) + 2):
    print(" " * (int(num / 2) + 1 - i),end="")
    for j in range(1, i + 1):
        print(mul + " ",end="")
    # print(mul * i)
    print()
for i in range(int(num / 2) + 2, num + 1):
    print(" " * (i - int(num / 2) - 1),end="")
    for j in range(1, num - i + 2):
        print(mul + " ", end="")
    print()
    # print(mul * (num + 1 - i))